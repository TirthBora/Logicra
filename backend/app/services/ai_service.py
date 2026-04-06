from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def explain_code_ai(code: str, language: str) -> str:
    prompt = f"Explain this {language} code:\n\n``` {language}\n{code}\n```"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def translate_error_ai(error: str, language: str) -> Dict[str, str]:
    prompt = f"Translate this {language} error into plain English and suggest a fix:\n\n{error}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return {
        "explanation": response.choices[0].message.content,
        "fix_suggestion": "TODO: parse fix from AI response"
    }

