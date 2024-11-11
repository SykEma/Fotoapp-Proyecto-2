from PIL import Image

DIMENSIONES = {
    "Instagram": (1080, 1080),
    "X": (1200, 675),
    "Facebook": (1200, 628),
}

def resize_image(image_path, platform):
    try:
        if platform not in DIMENSIONES:
            raise ValueError(f"Plataforma '{platform}' no soportada.")
        
        with Image.open(image_path) as img:
            target_size = DIMENSIONES[platform]
            resized_img = img.resize(target_size, Image.LANCZOS)
            resized_image_path = f"redimensionada_para_{platform}.jpg"
            resized_img.save(resized_image_path)
        
        return resized_img  
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{image_path}'. Verifica que la ruta sea correcta.")
        return None

from PIL import Image, ImageEnhance

def adjust_contrast(image_path, low_contrast=0.5, high_contrast=2.0):
    try:
        with Image.open(image_path) as img:
            enhancer = ImageEnhance.Contrast(img)
            
            low_contrast_img = enhancer.enhance(low_contrast)
            low_contrast_path = "Bajo_Contraste.jpg"  
            low_contrast_img.save(low_contrast_path)

            high_contrast_img = enhancer.enhance(high_contrast)
            high_contrast_path = "Alto_Contraste.jpg"  
            high_contrast_img.save(high_contrast_path)
        
        print(f"Imágenes guardadas como '{low_contrast_path}' y '{high_contrast_path}'.")
        return low_contrast_img, high_contrast_img  
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{image_path}'. Verifica la ruta.")
        return None, None


from PIL import ImageFilter, ImageDraw, ImageFont

FILTROS = {
    "ORIGINAL": None,
    "BLUR": ImageFilter.BLUR,
    "CONTOUR": ImageFilter.CONTOUR,
    "DETAIL": ImageFilter.DETAIL,
    "EDGE ENHANCE": ImageFilter.EDGE_ENHANCE,
    "EDGE ENHANCE MORE": ImageFilter.EDGE_ENHANCE_MORE,
    "EMBOSS": ImageFilter.EMBOSS,
    "FIND EDGES": ImageFilter.FIND_EDGES,
    "SHARPEN": ImageFilter.SHARPEN,
    "SMOOTH": ImageFilter.SMOOTH
}

def apply_filter(image_path, filter_name):
    if filter_name not in FILTROS:
        raise ValueError("Filtro desconocido. Usa uno de los filtros nombrados en la lista.")
    
    with Image.open(image_path) as img:
        if FILTROS[filter_name] is not None:
            img = img.filter(FILTROS[filter_name])

        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()
        draw.text((10, 10), filter_name, font=font, fill="white")
        
        filtered_image_path = f"{filter_name.lower().replace(' ', '_')}.jpg"
        img.save(filtered_image_path)
    
    return filtered_image_path, img


import cv2
import numpy as np
from PIL import Image

def create_sketch(image_path, persona=True):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    if persona:
        blurred_img = cv2.GaussianBlur(img, (21, 21), 0)
        
        inverted_img = cv2.bitwise_not(blurred_img)
        
        sketch_img = cv2.divide(img, 255 - inverted_img, scale=256)
        
        highlighted_image_path = "boceto_persona.jpg"
        cv2.imwrite(highlighted_image_path, sketch_img)
        
        pil_image = Image.fromarray(sketch_img)  
        pil_image.show()  
        
        return highlighted_image_path
    else:
        return image_path










