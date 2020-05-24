import os
import sys
from guitarra import Guitarra
from violin import Violin


class Orquesta:
    pass


def main():
    #Para agregar el path completo a su archivo
    if os.name == 'nt':
        direc = sys.path[0] + "\\"
    else:
        direc = sys.path[0] + "/"

    sinfonica = Orquesta("Orquesta Sinfonica Nacional")

    #aqui agregue cualquier otro instrumento que quiera tocar
    guitarrita = Guitarra(direc + "guitarra.wav")
    sinfonica.agregarInstrumento(guitarrita)
    violincito = Violin(direc + "violin.mp3")
    sinfonica.agregarInstrumento(violincito)

    sinfonica.ejecutar()


# Los achivos de musica se integran del path completo
if __name__ == "__main__":
    main()
