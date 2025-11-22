
import os
from google import genai
from google.genai import types
from PIL import Image
from dotenv import load_dotenv



def read_image(PIL_IMAGE_PATH: str) -> str:
    answer = None
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")

    client = genai.Client(api_key=api_key)

    try:
        PIL_IMAGE = Image.open(PIL_IMAGE_PATH)
    except FileNotFoundError:
        print("arquivo não encontrado")
        return answer

    prompt = ("Extraia o texto da imagem. Formate a saída do texto extraido como um txt.")

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                prompt,
                PIL_IMAGE
            ]
        )
        answer=response.text
        return answer
    except Exception as e:
        print(f"Ocorreu um erro na API:{e}")
        return answer

if __name__ == "__main__":
    PIL_IMAGE_PATH = r"C:\Users\gabri\Modus\src\OCR\testes\notafiscal1.jpg"
    answer = read_image(PIL_IMAGE_PATH)
    print(answer)