import PyInstaller.__main__
import os
import sys
import shutil

sound_dir = os.path.join(os.path.dirname(__file__), 'sound')
if not os.path.exists(sound_dir):
    os.makedirs(sound_dir)

sound_file = os.path.join(sound_dir, '2.wav')
if not os.path.exists(sound_file):
    print(f"ADVERTENCIA: No se encuentra el archivo de sonido en {sound_file}")
    print("Por favor, asegúrate de colocar el archivo 2.wav en la carpeta sound")
    sys.exit(1)

icon_path = os.path.join(os.path.dirname(__file__), 'icons', '1.ico')

PyInstaller.__main__.run([
    'py.py',
    '--onefile',
    '--windowed',
    f'--icon={icon_path}',
    '--name=THO_OPTIMIZER_V2',
    '--add-data=matrix_background.py;.',
    '--add-data=icons;icons',
    '--add-data=sound/2.wav;sound/',  
    '--uac-admin',
    '--clean',
    '--noupx',
    '--hidden-import=win32api',
    '--hidden-import=win32security',
    '--hidden-import=win32con',
    '--hidden-import=psutil',
])
