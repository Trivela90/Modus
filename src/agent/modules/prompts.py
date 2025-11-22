from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
FILES_BASE_PATH = BASE_DIR / ".." / ".." / "prompts"

def load_prompt(prompt_name: str) -> str:
    with open(f"{FILES_BASE_PATH}/{prompt_name}.txt", "r") as file:
        return file.read()
    
basic_extraction_prompt = load_prompt("basic_extraction")
extraction_from_unstructured_prompt = load_prompt("extraction_from_unstructured")