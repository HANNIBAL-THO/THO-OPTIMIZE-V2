# THO OPTIMIZER V2

<div align="center">

[![YouTube Tutorial](https://img.shields.io/badge/YouTube-Tutorial-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/@TODO-HACK-OFFICIAL)
[![Discord](https://img.shields.io/badge/Discord-Unete-7289DA?style=for-the-badge&logo=discord)](https://discord.gg/4svwzsy3UP)

![THO OPTIMIZER V2](vdo/v.mp4)

*Una potente herramienta de optimización para Windows*

</div>

## 🚀 Características

- 🎮 Optimización para gaming
- ⚡ Mejoras de rendimiento del sistema
- 🔧 Optimización de servicios
- 💾 Limpieza y mantenimiento
- 🛡️ Ajustes de seguridad
- 🌐 Optimización de red
- 🎨 Mejoras visuales
- 🔋 Gestión de energía

## 📋 Requisitos Previos

- Windows 10/11
- Python 3.8 o superior
- Git (opcional)
- Privilegios de administrador

## ⚙️ Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/HannibalTHO/THO-OPTIMIZER-V2.git
cd THO-OPTIMIZER-V2
```

2. Crear un entorno virtual:
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## 🛠️ Compilación

1. Asegúrate de tener todos los archivos necesarios:
```bash
dir
```

2. Instala PyInstaller si aún no lo tienes:
```bash
pip install pyinstaller
```

3. Compila el proyecto:
```bash
pyinstaller --noconfirm --onefile --windowed --icon=icons/icon.ico --add-data "icons;icons/" --name "THO-Optimizer" main.py
```

4. El ejecutable se encontrará en la carpeta `dist`:
```bash
cd dist
THO-Optimizer.exe
```

## 📝 Notas de Compilación

- El ejecutable final estará en la carpeta `dist`
- Asegúrate de tener todos los recursos (imágenes, iconos) en la carpeta `icons`
- La compilación puede tardar unos minutos
- El archivo ejecutable será independiente y no necesitará Python instalado
