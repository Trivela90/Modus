

from transformers import pipeline
from PIL import Image


ocr = pipeline("image-to-text", model="datalab-to/chandra")

PIL_IMAGE_PATH = "C:/Users/gabri/Modus/OCR/testes/notafiscal1.jpg"
PIL_IMAGE = Image.open(PIL_IMAGE_PATH)

result = ocr(PIL_IMAGE)
print(result)
#cria batch para enviar para modelo
# batch = [
#     BatchInputItem(
#         image=PIL_IMAGE,
#         prompt_type="ocr_layout"
#     )
# ]

# result = generate_hf(batch, model)[0]
# markdown = parse_markdown(result.raw)
