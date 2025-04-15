# THO OPTIMIZER V2

<div align="center">

[![YouTube Tutorial](https://img.shields.io/badge/YouTube-Tutorial-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/@TODO-HACK-OFFICIAL)
[![Discord](https://img.shields.io/badge/Discord-Unete-7289DA?style=for-the-badge&logo=discord)](https://discord.gg/4svwzsy3UP)

<img src="icons/1.ico" width="150" height="150" alt="THO Optimizer Logo">

<video width="720" height="405" controls>
    <source src="./vdo/v.mp4" type="video/mp4">
    Tu navegador no soporta la etiqueta de video.
</video>

*Una potente herramienta de optimización para Windows*

</div>

## 🚀 Características

### 🎮 Optimización para Gaming
- Mejora el rendimiento en juegos
- Optimiza la prioridad de GPU
- Reduce la latencia del sistema
- Configura Windows para gaming

### ⚡ Mejoras de Rendimiento
- THO NORMAL: Optimización básica del sistema
- THO FULL: Optimización completa
- THO EXTREMO: Máximo rendimiento
- THO FPS BOOST: Mejora de FPS en juegos

### 🔧 Optimización de Servicios
- Desactiva servicios innecesarios
- Optimiza servicios de Windows
- Mejora el arranque del sistema
- Reduce el consumo de recursos

### 💾 Limpieza y Mantenimiento
- THO TEMP: Limpia archivos temporales
- THO RAM: Optimiza la memoria RAM
- Limpieza del registro
- Mantenimiento automático

### 🛡️ Ajustes de Seguridad
- THO DEFENDER: Optimiza Windows Defender
- Mejora la protección del sistema
- Configuración de firewall
- Actualizaciones de seguridad

### 🌐 Optimización de Red
- THO RED: Mejora la conexión
- Reduce la latencia
- Optimiza DNS
- Mejora el rendimiento online

### 🎨 Mejoras Visuales
- THO VISUAL: Optimiza efectos visuales
- Mejora el rendimiento gráfico
- Reduce efectos innecesarios
- Optimiza la interfaz

### 🔋 Gestión de Energía
- THO BATERIA: Optimiza el consumo
- Mejora la duración de la batería
- Perfiles de energía personalizados
- Balance rendimiento/consumo

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
