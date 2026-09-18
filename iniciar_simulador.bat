@echo off
title Simulador de Notariado - El Salvador (CSJ)
color 1F
cd /d "%~dp0"

echo =========================================================================
echo       SIMULADOR DE EXAMEN DE NOTARIADO DE EL SALVADOR (CSJ)
echo =========================================================================
echo.
echo Ubicacion: %CD%
echo Iniciando servidor web de estudio...
echo Accede en tu navegador a: http://127.0.0.1:5000
echo.
echo Para detener el servidor, presiona Ctrl + C en esta ventana.
echo =========================================================================
echo.
start http://127.0.0.1:5000
python app.py
pause
