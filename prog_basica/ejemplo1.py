gof = "God of war"
halo = "Halo"
botw = "Zelda - Breath of the wild"

def videoJuego(opcion):
    print("Deberías jugar " + str(opcion))


def run():
    menu = """1) PlayStation 4 \n2) Xbox One \n3) Nintendo Switch """
    print(menu)
    opcion = int(input("¿Cuál de estás es tu consola favorita?: "))
    if opcion==1:
        videoJuego(gof)
    elif opcion==2:
        videoJuego(halo)
    elif opcion==3:
        videoJuego(botw)
    else:
        print("Has escogido una opción inválida")


if __name__ == "__main__":
    run()

#linea 26
#linea 27
#linea 28
#linea 29
#linea 30