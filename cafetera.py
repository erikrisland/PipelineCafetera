class Vaso:
    def __init__(self, tamaño, cantidad_cafe):
        self.tamaño = tamaño 
        self.cantidad_cafe = cantidad_cafe  

class Azucarero:
    def __init__(self, cantidad_azucar):
        self.cantidad_azucar = cantidad_azucar  

    def usar_azucar(self, cucharadas):
        if cucharadas <= self.cantidad_azucar:
            self.cantidad_azucar -= cucharadas
            return cucharadas  
        elif self.cantidad_azucar > 0:
            return self.cantidad_azucar  
        else:
            return 0  

class Cafetera:
    def __init__(self, cantidad_cafe):
        self.cantidad_cafe = cantidad_cafe 

    def usar_cafe(self, onzas):
        if onzas <= self.cantidad_cafe:
            self.cantidad_cafe -= onzas
            return True
        else:
            print("No hay suficiente café")
            return False

class MaquinaDeCafe:
    def __init__(self, cafetera, azucarero, vasos_pequeños, vasos_medianos, vasos_grandes):
        self.cafetera = cafetera
        self.azucarero = azucarero
        self.vasos_pequeños = vasos_pequeños  
        self.vasos_medianos = vasos_medianos  
        self.vasos_grandes = vasos_grandes 

    def hay_vasos(self, tamaño):
        if tamaño == "pequeño":
            return len(self.vasos_pequeños) > 0
        elif tamaño == "mediano":
            return len(self.vasos_medianos) > 0
        elif tamaño == "grande":
            return len(self.vasos_grandes) > 0
        return False

    def preparar_cafe(self, tamaño_vaso, cucharadas_azucar):
        if not self.hay_vasos(tamaño_vaso):
            print(f"No hay vasos de tamaño {tamaño_vaso} disponibles.")
            return False 

        if tamaño_vaso == "pequeño":
            vaso = self.vasos_pequeños.pop(0)  
        elif tamaño_vaso == "mediano":
            vaso = self.vasos_medianos.pop(0) 
        else:
            vaso = self.vasos_grandes.pop(0)  

        if not self.cafetera.usar_cafe(vaso.cantidad_cafe):
            print("Operación cancelada: No hay suficiente café")
            return False  
        
        cantidad_azucar_disponible = self.azucarero.usar_azucar(cucharadas_azucar)
        
        if cantidad_azucar_disponible == 0:
            continuar_sin_azucar = input("No hay azúcar disponible. ¿Quieres continuar sin azúcar? (s/n): ").lower()
            if continuar_sin_azucar == 's':
                cucharadas_azucar = 0
                print("Preparando café sin azúcar...")
            else:
                print("Operación cancelada")
                return False 
        elif cantidad_azucar_disponible < cucharadas_azucar:
            continuar_con_restante = input(f"Solo hay {cantidad_azucar_disponible} cucharadas disponibles. ¿Quieres usar solo {cantidad_azucar_disponible}? (s/n): ").lower()
            if continuar_con_restante == 's':
                cucharadas_azucar = cantidad_azucar_disponible
                print(f"Preparando café con {cucharadas_azucar} cucharadas de azúcar...")
            else:
                print("Operación cancelada")
                return False 
        else:
            print(f"Preparando café con {cucharadas_azucar} cucharadas de azúcar...")
        
        print("Disfruta tu café!")
        return True  

def seleccionar_tamaño():
    print("Selecciona el tamaño de vaso:")
    print("1. Pequeño (3 oz)")
    print("2. Mediano (5 oz)")
    print("3. Grande (7 oz)")
    opcion = input("Elige una opción (1-3): ")
    
    if opcion == "1":
        return "pequeño"
    elif opcion == "2":
        return "mediano"
    elif opcion == "3":
        return "grande"
    else:
        print("Opción no válida")
        return seleccionar_tamaño()

def seleccionar_azucar():
    try:
        cucharadas = int(input("¿Cuántas cucharadas de azúcar deseas (0-5)? "))
        if 0 <= cucharadas <= 5:
            return cucharadas
        else:
            print("Cantidad no válida")
            return seleccionar_azucar()  
    except ValueError:
        print("Entrada no válida, por favor ingresa un número.")
        return seleccionar_azucar()  

def configurar_maquina():
  
    vasos_pequeños = [Vaso('pequeño', 3)] * 2  
    vasos_medianos = [Vaso('mediano', 5)] * 2  
    vasos_grandes = [Vaso('grande', 7)] * 3  
    
    cantidad_azucar = 8  

    return vasos_pequeños, vasos_medianos, vasos_grandes, cantidad_azucar

def ejecutar_maquina(maquina):
    while True:
        
        tamaño_vaso = seleccionar_tamaño()

        
        if not maquina.hay_vasos(tamaño_vaso):
            print(f"No hay vasos de tamaño {tamaño_vaso} disponibles. Volviendo al menú principal...\n")
            continue  

        
        cucharadas_azucar = seleccionar_azucar()
        
        
        if not maquina.preparar_cafe(tamaño_vaso, cucharadas_azucar):
            print("Volviendo al menú principal...\n")
            continue  
        print("\nVolviendo al menú principal...\n")


if __name__ == "__main__":

    vasos_pequeños, vasos_medianos, vasos_grandes, cantidad_azucar = configurar_maquina()
    
    cafetera = Cafetera(20)

    azucarero = Azucarero(cantidad_azucar)
    
    maquina = MaquinaDeCafe(cafetera, azucarero, vasos_pequeños, vasos_medianos, vasos_grandes)
    
    ejecutar_maquina(maquina)
