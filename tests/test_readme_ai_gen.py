from unittest.mock import MagicMock, patch

from readme_ai_gen import ai, scanner


def test_get_ignore_spec(tmp_path):
    gitignore = tmp_path / ".gitignore"
    gitignore.write_text("my_secret_file.txt\n")
    
    spec = scanner.get_ignore_spec(tmp_path)
    assert spec.match_file("my_secret_file.txt")
    assert spec.match_file("node_modules/index.js") # Default ignore
    assert not spec.match_file("main.py")

def test_scan_directory(tmp_path):
    # Setup dummy directory
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "main.py").write_text("print('hello')")
    (tmp_path / "node_modules").mkdir()
    (tmp_path / "node_modules" / "bad.js").write_text("ignore me")
    
    result = scanner.scan_directory(str(tmp_path))
    assert "main.py" in result
    assert "print('hello')" in result
    assert "bad.js" not in result

@patch('readme_ai_gen.ai.OpenAI')
def test_generate_readme(mock_openai):
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_message = MagicMock()
    mock_message.content = "# My Project\nAwesome stuff."
    mock_response.choices = [MagicMock(message=mock_message)]
    mock_client.chat.completions.create.return_value = mock_response
    mock_openai.return_value = mock_client
    
    with patch.dict('os.environ', {'OPENAI_API_KEY': 'fake-key'}):
        result = ai.generate_readme("context", "my_project")
        assert "My Project" in result
