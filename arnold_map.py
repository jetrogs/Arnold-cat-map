from PIL import Image
import numpy as np

def arnold_cat_map(img_array, iterations=1):
    """
    Mapa de Arnold
    """
    N = img_array.shape[0]  # Tamaño de la dimension de la imagen (ancho o alto)
    result = np.copy(img_array)  # Copia del arreglo
    
    for _ in range(iterations):
        temp = np.zeros_like(result)  # Arreglo temporal
        for x in range(N):
            for y in range(N):
                # Aplicación de las transformaciones del mapa de Arnold
                x_new = (x + y) % N
                y_new = (x + 2*y) % N
                temp[x_new, y_new] = result[x, y]  # Asignacion de los valores
        result = temp
    
    return result  # Retorna el arreglo de imagen

def main():
    # Carga de la imagen
    img = Image.open("imagen.jpg")
    
    # Conversión a arreglo
    img_array = np.array(img)
    
    # Verificación y ajuste si la imagen no es cuadrada
    height, width = img_array.shape[:2]
    if height != width:
        min_dim = min(height, width)
        img_array = img_array[:min_dim, :min_dim, :]  # Recorta la imagen al tamañomínimo
        height, width = min_dim, min_dim
    
    # Numero de iteraciones
    iterations = 120
    
    # Aplicacion del mapa
    scrambled_image = arnold_cat_map(img_array, iterations=iterations)
    
    # Conversión de nuevo a objeto de imagen
    img_scrambled = Image.fromarray(scrambled_image.astype('uint8'))  # Conversion
    img_scrambled.save(f"arnold_{iterations}.png")  # Guardado de la imagen
    print(f"Imagen guardada como arnold_{iterations}.png")

if __name__ == "__main__":
    main()
