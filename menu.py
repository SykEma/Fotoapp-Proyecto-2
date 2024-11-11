import fotoapp  

def main_menu():
    while True:
        print("\n--- Menú de opciones ---")
        print("1. Redimensionar imagen para red social")
        print("2. Ajustar contraste")
        print("3. Aplicar filtro")
        print("4. Identificar y resaltar persona")
        print("5. Salir")
        
        option = input("Selecciona una opción (1-5): ")
        
        if option == '1':
            image_path = input("Ingresa la ruta de la imagen: ")
            platform = input("Ingresa la red social: ")
            try:
                resized_image = fotoapp.resize_image(image_path, platform)
                print(f"Imagen guardada en: {resized_image}")
            except Exception as e:
                print(f"Error: {e}")

        elif option == '2':
            image_path = input("Ingresa la ruta de la imagen: ")
            try:
                low_contrast_img, high_contrast_img = fotoapp.adjust_contrast(image_path)
                print(f"Imágenes guardadas en: {low_contrast_img} y {high_contrast_img}")
            except Exception as e:
                print(f"Error: {e}")

        elif option == '3':
            image_path = input("Ingresa la ruta de la imagen: ")
            filter_name = input("Ingresa el filtro (ORIGINAL, BLUR, CONTOUR, etc.): ")
            try:
                filtered_image = fotoapp.apply_filter(image_path, filter_name)
                print(f"Imagen filtrada guardada en: {filtered_image}")
            except Exception as e:
                print(f"Error: {e}")

        elif option == '4':
            image_path = input("Ingresa la ruta de la imagen: ")
            persona = input("¿Es una persona? (sí/no): ").lower() == 'sí'
            try:
                highlighted_image = fotoapp.identify_person(image_path, persona)
                print(f"Imagen guardada en: {highlighted_image}")
            except Exception as e:
                print(f"Error: {e}")

        elif option == '5':
            print("Cerrando programa.")
            break

        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 5.")

if __name__ == "__main__":
    main_menu()
