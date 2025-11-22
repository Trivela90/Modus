from OCR.OCR import read_image

def image_text_extractor(state) -> str:
    image_path = state.get("image_path", "")
    if image_path == "":
        return {"extracted_text": ""}
    extracted_text = read_image(image_path)
    return {"extracted_text": extracted_text}