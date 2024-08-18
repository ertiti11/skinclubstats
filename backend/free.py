import random

# Definir probabilidades
probabilidad_cuchillo = 0.00437  # 0.163%
probabilidad_pistola = 1 - probabilidad_cuchillo  # Lo demás es para pistola

# Inicializar contador de iteraciones


# Bucle hasta que salga "cuchillo"
si = []
for i in range(10000):
    iteraciones = 0
    while True:
        iteraciones += 1
        palabra = random.choices(['cuchillo', 'pistola'], [probabilidad_cuchillo, probabilidad_pistola])[0]
        
        if palabra == 'cuchillo':
            print(f'¡Salió "cuchillo" después de {iteraciones} iteraciones!')
            si.append(iteraciones)
            break
print("la media de iteraciones es: ", sum(si)/len(si))
print(f"entre las 5 cajas se necesitan en promedio {(sum(si)/len(si))/5} iteraciones para obtener un cuchillo")