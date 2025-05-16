from PIL import Image
import numpy as np

def arnold_cat_map(img_array, iterations=1):
    """
    Aplica el mapa de Arnold
    """
    N = img_array.shape[0]
    result = np.copy(img_array)
    
    for _ in range(iterations):
        temp = np.zeros_like(result)
        for x in range(N):
            for y in range(N):
                x_new = (x + y) % N
                y_new = (x + 2*y) % N
                temp[x_new, y_new] = result[x, y]
        result = temp
    return result

def main():
    #Carga tu imagen
    img = Image.open("imagen.jpg")
    
    #Convierte a numpy array
    arr = np.array(img)
    
    #Comprueba que la imagen es cuadrada
    N, M = arr.shape[0], arr.shape[1]
    if N != M:
        min_dim = min(N, M)
        arr = arr[:min_dim, :min_dim]
        N = min_dim
    
    #Aplica el mapa de Arnold
    iteraciones = 120  # Número de iteraciones
    scrambled = arnold_cat_map(arr, iterations=iteraciones)
    
    #Convierte de nuevo a imagen y guarda
    img_scrambled = Image.fromarray(scrambled)
    img_scrambled.save(f"arnold_{iteraciones}.png")
    print(f"Imagen guardada como arnold_{iteraciones}.png")

if __name__ == "__main__":
    main()
