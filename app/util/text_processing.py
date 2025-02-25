import re

def clean_text(text: str) -> str:
    """
    Normaliza el texto eliminando caracteres especiales y espacios adicionales.
    """
    text = re.sub(r'\s+', ' ', text)  # Quitar espacios múltiples
    text = re.sub(r'[^\w\s]', '', text)  # Remover caracteres especiales
    return text.strip().lower()