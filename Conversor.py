import os
import shutil
import tkinter as tk
from tkinter import filedialog
from moviepy.editor import *
#import re
from pytube import YouTube
import os
#import moviepy.editor as mp

root = tk.Tk()
root.withdraw()

opcion = input("¿Desea convertir un video de youtube o un archivo local? (yt/l): ")

if opcion == "yt":
    link = input("Introduce el link del video: ")
    yt = YouTube(link)

    ys = yt.streams.get_highest_resolution()

    while True:
        nombreyt = input("Nombre del archivo para guardar: ")
        if nombreyt.strip() != "":
            break
        else:
            print("El nombre del archivo no puede estar en blanco. Por favor, inténtelo de nuevo.")

    print("Descargando...")

    ys.download()
    
    mp4_fileyt = ys.download(filename=nombreyt) 

    clip = VideoFileClip(mp4_fileyt)

    audioclip = clip.audio

    mp3_fileyt = nombreyt + ".mp3"
    audioclip.write_audiofile(mp3_fileyt)
    
    shutil.move(mp3_fileyt, "C:/Program Files/Soundpad/sounds")
    
    audioclip.close()
    VideoClip.close(self=clip)
    clip.close()
    os.remove(mp4_fileyt)

    print("Archivo guardado en mp3 en la ruta seleccionada")

    eliminar = input("¿Desea eliminar el archivo original? (s/n): ")

    if eliminar == "s":
        try:
            archivo_a_eliminar = ys.download()
            os.remove(archivo_a_eliminar)
            print("El archivo se eliminó")
        except Exception as e:
            print(f"No se puede eliminar el archivo: {e}")
    elif eliminar == "n":
        print("El archivo no se eliminó")
    else:
        print("Opción no válida")

elif opcion == "l":
    file_path = filedialog.askopenfilename()
    mp4_file = file_path

    while True:
        nombre = input("Nombre del archivo para guardar: ")
        if nombre.strip() != "":
            break
        else:
            print("El nombre del archivo no puede estar en blanco. Por favor, inténtelo de nuevo.")

    mp3_file = nombre + ".mp3"

    VideoClip2 = VideoFileClip(mp4_file)

    audioclip2 = VideoClip2.audio

    audioclip2.write_audiofile(mp3_file)

    audioclip2.close()

    VideoClip2.close()

    print("Conviertiendo...")

    shutil.move(mp3_file, "C:/Program Files/Soundpad/sounds")

    print("Archivo guardado en mp3 en la ruta seleccionada")

    eliminar = input("¿Desea eliminar el archivo original? (s/n): ")

    if eliminar == "s":
        try:
            archivo_a_eliminar = mp4_file
            os.remove(archivo_a_eliminar)
            print("El archivo se eliminó")
        except Exception as a:
            print(f"No se puede eliminar el archivo: {a}")
    elif eliminar == "n":
        print("El archivo no se eliminó")
    else:
        print("Opción no válida")

else:
    print("Opción no válida")

input("Presione cualquier tecla para salir...")
