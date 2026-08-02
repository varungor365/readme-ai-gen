import argparse
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

from . import __version__
from .ai import generate_readme
from .scanner import scan_directory

console = Console()

def print_banner():
    banner = f"""[cyan]🤖 readme-ai-gen v{__version__}[/cyan]
[dim]Generate trending-optimized READMEs using AI.[/dim]"""
    console.print(Panel(banner, border_style="cyan"))

def main():
    parser = argparse.ArgumentParser(description="Generate a beautiful README for your project.")
    parser.add_argument("--version", action="version", version=f"readme-ai-gen {__version__}")
    parser.add_argument("path", nargs="?", default=".", help="Path to the repository (default: current directory)")
    parser.add_argument("--output", "-o", default="README_GENERATED.md", help="Output file name (default: README_GENERATED.md)")
    
    args = parser.parse_args()
    
    load_dotenv()
    if not os.environ.get("OPENAI_API_KEY"):
        console.print("[red]❌ Error:[/red] OPENAI_API_KEY environment variable is not set.")
        console.print("Please set it or create a .env file.")
        sys.exit(1)
        
    print_banner()
    
    repo_path = Path(args.path).resolve()
    if not repo_path.is_dir():
        console.print(f"[red]❌ Error:[/red] Directory not found: {repo_path}")
        sys.exit(1)
        
    project_name = repo_path.name
    
    try:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
            console=console
        ) as progress:
            
            progress.add_task(description=f"Scanning codebase: [cyan]{project_name}[/cyan]...", total=None)
            context = scan_directory(str(repo_path))
            
            progress.add_task(description="Generating README using AI (this may take a minute)...", total=None)
            readme_content = generate_readme(context, project_name)
            
        output_path = repo_path / args.output
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(readme_content)
            
        console.print("\n[bold green]✅ README successfully generated![/bold green]")
        console.print(f"Saved to: [cyan]{output_path}[/cyan]")
        
    except Exception as e:  # noqa: BLE001
        console.print(f"\n[red]❌ Error:[/red] {e!s}")
        sys.exit(1)

if __name__ == "__main__":
    main()
