import os
from pathlib import Path

import pathspec


def get_ignore_spec(root_dir: Path) -> pathspec.PathSpec:
    """Reads .gitignore and returns a pathspec object. Also adds default ignores."""
    lines = [
        ".git/",
        "node_modules/",
        "venv/",
        "env/",
        "__pycache__/",
        "*.pyc",
        "dist/",
        "build/",
        "*.jpg", "*.png", "*.gif", "*.pdf", "*.wav", "*.mp3", "*.mp4", "*.zip", "*.tar.gz"
    ]
    
    gitignore_path = root_dir / ".gitignore"
    if gitignore_path.exists():
        with open(gitignore_path, "r", encoding="utf-8") as f:
            lines.extend(f.readlines())
            
    return pathspec.PathSpec.from_lines(pathspec.patterns.GitWildMatchPattern, lines)

def scan_directory(root_dir: str) -> str:
    """Scans the directory and returns a string representation of the codebase."""
    root_path = Path(root_dir)
    spec = get_ignore_spec(root_path)
    
    codebase_context = []
    
    # 1. First, gather the tree structure
    tree_lines = ["Directory Structure:"]
    for root, dirs, files in os.walk(root_dir):
        rel_root = Path(root).relative_to(root_path)
        if str(rel_root) != "." and spec.match_file(str(rel_root) + "/"):
            dirs[:] = []
            continue
            
        # Filter directories
        dirs[:] = [d for d in dirs if not spec.match_file(str(rel_root / d) + "/")]
        
        level = len(rel_root.parts)
        indent = "  " * level
        tree_lines.append(f"{indent}📁 {rel_root.name if str(rel_root) != '.' else root_path.name}")
        
        sub_indent = "  " * (level + 1)
        for f in sorted(files):
            rel_file = rel_root / f
            if not spec.match_file(str(rel_file)):
                tree_lines.append(f"{sub_indent}📄 {f}")
                
    codebase_context.append("\n".join(tree_lines))
    codebase_context.append("\n" + "="*40 + "\n")
    
    # 2. Then, gather file contents (limit total size to avoid massive prompts)
    total_chars = 0
    MAX_CHARS = 200000 # ~50k tokens
    
    codebase_context.append("File Contents:")
    for root, dirs, files in os.walk(root_dir):
        rel_root = Path(root).relative_to(root_path)
        
        # Filter dirs
        dirs[:] = [d for d in dirs if not spec.match_file(str(rel_root / d) + "/")]
        
        for f in sorted(files):
            rel_file = rel_root / f
            if spec.match_file(str(rel_file)):
                continue
                
            file_path = root_path / rel_file
            
            # Skip large files (> 500KB)
            if file_path.stat().st_size > 500_000:
                continue
                
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                    if total_chars + len(content) > MAX_CHARS:
                        codebase_context.append("\n... (Codebase too large, truncated) ...")
                        return "\n".join(codebase_context)
                        
                    codebase_context.append(f"\n--- {rel_file} ---\n{content}")
                    total_chars += len(content)
            except UnicodeDecodeError:
                # Binary file, skip
                pass
                
    return "\n".join(codebase_context)
