from pathlib import Path
import json

def load_debugging_prompt() -> dict:
    prompt_path = Path("utils/prompts/debugging_prompt.json")
    if not prompt_path.exists():
        raise FileNotFoundError(f"Debugging prompt file not found at {prompt_path}")
    
    with prompt_path.open('r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def build_debugging_prompt(code_or_error_log: str) -> str:
    data = load_debugging_prompt()
    system_instruction = data.get("system_instruction", "")
    user_prompt_template = data.get("user_prompt_template", "")
    
    prompt = f"{system_instruction}\n\n{user_prompt_template.format(code_or_error_log=code_or_error_log)}"
    return prompt

# Example usage:
# code_or_error_log = "print(Hello World)" 
# print(build_debugging_prompt(code_or_error_log))