from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, 
                              QWidget, QLabel, QMessageBox, QHBoxLayout, QTextEdit,
                              QStackedWidget)
from PySide6.QtCore import Qt, QPropertyAnimation, QRect, QEasingCurve, QSize, QUrl, QMetaObject, Q_ARG
from PySide6.QtGui import QFont, QColor, QIcon, QDesktopServices
from PySide6.QtMultimedia import QSoundEffect  
from matrix_background import MatrixBackground  
try:
    import win32security
    import win32api
    import win32con
except ImportError:

    pass

import os
import subprocess
import winreg
import ctypes
import sys
import psutil
import threading

class OptimizadorTHO(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TODO HACK OFFICIAL")
        self.setFixedSize(1200, 800)  
        
        self.setWindowOpacity(0)
        self.fade_in_animation = QPropertyAnimation(self, b"windowOpacity")
        self.fade_in_animation.setStartValue(0)
        self.fade_in_animation.setEndValue(1)
        self.fade_in_animation.setDuration(1000)
        self.fade_in_animation.start()
        
        self.log_console = QTextEdit()
        self.log_console.setReadOnly(True)
        self.log_console.setStyleSheet("""
            QTextEdit {
                background-color: rgba(0, 0, 0, 0.7);
                color: #2ecc71;
                border: 1px solid #2ecc71;
                border-radius: 5px;
                min-height: 150px;
            }
        """)
        
        self.elevar_privilegios()
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        self.background = MatrixBackground(self)
        self.background.resize(self.size())
        self.background.lower()  
        
        container = QWidget()
        container.setStyleSheet("background-color: rgba(0, 0, 0, 0.2);")  
        container_layout = QHBoxLayout(container)
        main_layout.addWidget(container)
        
        sidebar = QWidget()
        sidebar.setFixedWidth(200)
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setAlignment(Qt.AlignTop)
        
        sidebar.setStyleSheet("""
            QWidget {
                background-color: rgba(0, 0, 0, 0.85);
                border-right: 2px solid #2ecc71;
                padding: 10px;
                margin: 5px;
                border-radius: 10px;
            }
        """)
        
        self.crear_boton_nav("🏠 INICIO", self.mostrar_main, sidebar_layout)
        self.crear_boton_nav("ℹ️ CDT", self.mostrar_creditos, sidebar_layout)
        
        nav_style = """
            QPushButton {
                background-color: rgba(46, 204, 113, 0.1);
                color: #2ecc71;
                border: 2px solid #2ecc71;
                border-radius: 10px;
                text-align: left;
                padding: 15px;
                margin: 10px 5px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: rgba(46, 204, 113, 0.3);
                border-color: #27ae60;
            }
            QPushButton:pressed {
                background-color: rgba(46, 204, 113, 0.5);
            }
        """
        
        for btn in sidebar.findChildren(QPushButton):
            btn.setStyleSheet(nav_style)

        content_area = QWidget()
        content_layout = QVBoxLayout(content_area)
        
        self.stack = QStackedWidget()
        
        main_page = QWidget()
        main_page_layout = QVBoxLayout(main_page)
        
        titulo = QLabel("THO OPTIMIZER 2.0")
        titulo.setStyleSheet("color: #2ecc71; font-size: 28px; font-weight: bold;")
        main_page_layout.addWidget(titulo, alignment=Qt.AlignCenter)
        
        buttons_widget = QWidget()
        buttons_layout = QHBoxLayout(buttons_widget)
        buttons_layout.setSpacing(20)
        buttons_layout.setContentsMargins(20, 20, 20, 20)

        left_column = QWidget()
        left_layout = QVBoxLayout(left_column)
        left_layout.setSpacing(10)

        center_column = QWidget()
        center_layout = QVBoxLayout(center_column)
        center_layout.setSpacing(10)
        center_layout.setAlignment(Qt.AlignCenter)

        right_column = QWidget()
        right_layout = QVBoxLayout(right_column)
        right_layout.setSpacing(10)

        left_buttons = [
            ("🚀 THO NORMAL", self.optimizar_normal),
            ("⚡ THO FULL", self.optimizar_full),
            ("🔧 THO SERVICIOS", self.optimizar_servicios),
            ("🗑️ THO TEMP", self.limpiar_temporales),
            ("💾 THO RAM", self.optimizar_ram),
            ("🎮 THO GPU", self.optimizar_gpu),
            ("📊 THO GAME MODE", self.activar_modo_juego),
            ("🎯 THO FPS BOOST", self.optimizar_fps),
            ("⚡ THO AUDIO", self.optimizar_audio),
        ]

        center_button = [("💪 THO EXTREMO", self.optimizar_extremo)]

        right_buttons = [
            ("🔋 THO BATERIA", self.optimizar_bateria),
            ("🌡️ THO TEMPERATURA", self.optimizar_temperatura),
            ("🚄 THO RED", self.optimizar_red),
            ("🔒 THO SEGURIDAD", self.optimizar_seguridad),
            ("⚙️ THO SYSTEM", self.optimizar_sistema),
            ("💻 THO APPS", self.optimizar_apps),
            ("🛡️ THO DEFENDER", self.optimizar_defender),
            ("🎨 THO VISUAL", self.optimizar_visual),
            ("🔄 RESTAURAR", self.restaurar_sistema)
        ]

        for texto, funcion in left_buttons:
            btn = self.crear_boton_suave(texto, funcion)
            left_layout.addWidget(btn)

        texto, funcion = center_button[0]
        btn_extremo = self.crear_boton_suave(texto, funcion)
        btn_extremo.setStyleSheet("""
            QPushButton {
                background-color: rgba(46, 204, 113, 0.5);
                color: #2ecc71;
                border: 3px solid #2ecc71;
                padding: 10px;
                font-size: 18px;
                font-weight: bold;
                border-radius: 8px;
                min-height: 60px;
            }
            QPushButton:hover {
                background-color: rgba(46, 204, 113, 0.7);
                border: 4px solid #27ae60;
            }
        """)
        center_layout.addWidget(btn_extremo)

        for texto, funcion in right_buttons:
            btn = self.crear_boton_suave(texto, funcion)
            right_layout.addWidget(btn)

        buttons_layout.addWidget(left_column)
        buttons_layout.addWidget(center_column)
        buttons_layout.addWidget(right_column)
        main_page_layout.addWidget(buttons_widget)

        main_page_layout.addWidget(self.log_console)
        
        self.stack.addWidget(main_page)
        self.stack.addWidget(self.crear_pagina_creditos())
        
        container_layout.addWidget(sidebar)
        container_layout.addWidget(self.stack)

        self.success_sound = QSoundEffect(self)
        try:
 
            if getattr(sys, 'frozen', False):
          
                base_path = sys._MEIPASS
            else:
  
                base_path = os.path.dirname(os.path.abspath(__file__))
            
            sound_path = os.path.join(base_path, "sound", "2.wav")
            self.success_sound.setSource(QUrl.fromLocalFile(sound_path))
            self.success_sound.setVolume(1.0)
            self.success_sound.setLoopCount(1)
    
            if not os.path.exists(sound_path):
                print(f"No se encuentra el archivo de sonido en: {sound_path}")
        except Exception as e:
            print(f"Error al cargar sonido: {str(e)}")

    def reproducir_sonido_y_funcion(self, funcion):
        """Reproduce el sonido y ejecuta la función del botón"""
        try:
            if self.success_sound.isLoaded():
                self.success_sound.play()
            funcion()
        except Exception as e:
            print(f"Error al reproducir sonido: {str(e)}")
            funcion()

    def mostrar_mensaje(self, titulo, mensaje):
        QMessageBox.information(self, titulo, mensaje)

    def mostrar_error(self, titulo, mensaje):
        QMessageBox.critical(self, titulo, mensaje)

    def optimizar_normal(self):
        try:
            self.log("Iniciando optimización normal...")

            self.log("Iniciando limpieza del sistema...")
            os.system(r'cleanmgr /sagerun:1')

            self.log("Iniciando desfragmentación...")
            os.system(r'defrag C: /O')

            self.log("Limpiando archivos temporales...")
            os.system(r'del /s /f /q "%temp%\\*.*"')
            os.system(r'del /s /f /q "C:\\Windows\\Temp\\*.*"')

            self.log("Limpiando caché DNS...")
            os.system('ipconfig /flushdns')
            self.mostrar_mensaje("Éxito", "Optimización normal completada")
            self.log("Optimización normal completada exitosamente")
        except Exception as e:
            self.log(f"Error: {str(e)}")
            self.mostrar_error("Error", f"Error durante la optimización: {str(e)}")

    def optimizar_full(self):
        try:
            self.log("Iniciando optimización FULL...")

            commands = [
                ('cleanmgr /sagerun:1', "Limpieza del sistema"),
                ('defrag C: /O /D', "Desfragmentación profunda"),
                ('powercfg -h off', "Desactivando hibernación"),
                ('sfc /scannow', "Verificando archivos del sistema"),
                ('DISM /Online /Cleanup-Image /RestoreHealth', "Reparando imagen del sistema"),
                ('netsh winsock reset', "Reseteando Winsock"),
                ('netsh int ip reset', "Reseteando configuración TCP/IP"),
                (r'del /s /f /q "%temp%\\*.*"', "Limpiando temporales"),
                (r'del /s /f /q "C:\\Windows\\Temp\\*.*"', "Limpiando temporales de Windows")
            ]
            for cmd, desc in commands:
                self.log(f"Ejecutando: {desc}...")
                subprocess.run(cmd, shell=True)

            self.log("Optimizando registro...")
            self.modificar_registro_rendimiento()

            self.log("Optimizando servicios...")
            self.optimizar_servicios()
            self.mostrar_mensaje("Éxito", "Optimización FULL completada")
            self.log("Optimización FULL completada exitosamente")
        except Exception as e:
            self.log(f"Error: {str(e)}")
            self.mostrar_error("Error", f"Error durante la optimización: {str(e)}")

    def optimizar_extremo(self):
        try:
            self.log("Iniciando optimización EXTREMA...")
            
            self.worker_thread = threading.Thread(target=self._optimizar_extremo_thread)
            self.worker_thread.start()
            
            self.log("Optimización en progreso, por favor espere...")
            
        except Exception as e:
            self.log(f"Error: {str(e)}")
            self.mostrar_error("Error", f"Error durante la optimización: {str(e)}")

    def _optimizar_extremo_thread(self):
        try:

            self.optimizar_servicios_extremo()
            self.modificar_registro_rendimiento_extremo()
            
            QMetaObject.invokeMethod(self, "_optimizacion_completada", 
                                   Qt.ConnectionType.QueuedConnection)
        except Exception as e:

            QMetaObject.invokeMethod(self, "_mostrar_error_thread", 
                                   Qt.ConnectionType.QueuedConnection,
                                   Q_ARG(str, str(e)))

    def _optimizacion_completada(self):
        self.mostrar_mensaje("Éxito", "Optimización EXTREMA completada")
        self.log("Optimización EXTREMA completada exitosamente")

    def _mostrar_error_thread(self, error):
        self.mostrar_error("Error", f"Error durante la optimización: {error}")

    def modificar_registro_rendimiento(self):
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 
                               r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management",
                               0, winreg.KEY_ALL_ACCESS)
            winreg.SetValueEx(key, "IoPageLockLimit", 0, winreg.REG_DWORD, 983040)
            winreg.CloseKey(key)
        except Exception:
            pass

    def modificar_registro_rendimiento_extremo(self):
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 
                               r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management",
                               0, winreg.KEY_ALL_ACCESS)
            winreg.SetValueEx(key, "IoPageLockLimit", 0, winreg.REG_DWORD, 1966080)
            winreg.SetValueEx(key, "SystemCacheDirtyPageThreshold", 0, winreg.REG_DWORD, 1000)
            winreg.CloseKey(key)
        except Exception:
            pass

    def desactivar_servicios_innecesarios(self):
        servicios = [
            "DiagTrack",
            "SysMain",
            "WSearch",
        ]
        for servicio in servicios:
            os.system(f'net stop {servicio}')
            os.system(f'sc config {servicio} start=disabled')

    def restaurar_sistema(self):
        try:
            self.log("Iniciando restauración completa del sistema...")

            self.log("Restaurando configuración de energía...")
            os.system('powercfg -h on')  
            os.system('powercfg -restoredefaultschemes')  
            os.system('powercfg -setactive scheme_balanced')  

            self.log("Restaurando servicios de Windows...")
            servicios_default = [
                "DiagTrack",      
                "dmwappushservice", 
                "SysMain",        
                "WSearch",        
                "XboxGipSvc",     
                "XblAuthManager", 
                "XblGameSave",
                "TabletInputService",
                "Remote Registry",
                "PrintNotify",
                "fax",
                "Themes",         
                "Windows Update", 
                "Windows Time",   
                "Windows Search"  
            ]

            for servicio in servicios_default:
                os.system(f'sc config "{servicio}" start=auto')
                os.system(f'net start "{servicio}" >nul 2>&1')
                self.log(f"Servicio {servicio} restaurado")

            self.log("Restaurando configuración del registro...")
            try:
                key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 
                                   r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management",
                                   0, winreg.KEY_ALL_ACCESS)

                winreg.SetValueEx(key, "IoPageLockLimit", 0, winreg.REG_DWORD, 0)
                winreg.SetValueEx(key, "SystemCacheDirtyPageThreshold", 0, winreg.REG_DWORD, 0)
                winreg.SetValueEx(key, "LargeSystemCache", 0, winreg.REG_DWORD, 0)
                winreg.CloseKey(key)
            except Exception as e:
                self.log(f"Aviso: No se pudo restaurar algún valor del registro: {str(e)}")

            self.log("Restaurando configuración del sistema...")
            os.system('bcdedit /deletevalue useplatformclock')
            os.system('bcdedit /deletevalue disabledynamictick')
            os.system('bcdedit /deletevalue useplatformtick')

            self.log("Restaurando configuración de red...")
            os.system('ipconfig /flushdns')
            os.system('ipconfig /registerdns')
            os.system('netsh winsock reset')
            os.system('netsh int ip reset')

            self.log("Verificando integridad del sistema...")
            os.system('sfc /scannow')
            os.system('DISM /Online /Cleanup-Image /RestoreHealth')

            self.mostrar_mensaje("Éxito", "Sistema restaurado completamente a valores por defecto")
            self.log("Sistema restaurado a la configuración original exitosamente")

        except Exception as e:
            self.log(f"Error: {str(e)}")
            self.mostrar_error("Error", f"Error durante la restauración: {str(e)}")

    def activar_servicios(self):
        servicios = [
            "DiagTrack",
            "SysMain",
            "WSearch",
        ]
        for servicio in servicios:
            os.system(f'sc config {servicio} start=auto')
            os.system(f'net start {servicio}')

    def crear_boton_animado(self, texto, funcion):
        btn = QPushButton(texto)
        btn.clicked.connect(funcion)

        self.animation = QPropertyAnimation(btn, b"geometry")
        self.animation.setDuration(200)
        def on_hover():
            geometry = btn.geometry()
            self.animation.setStartValue(geometry)
            self.animation.setEndValue(QRect(geometry.x()-5, geometry.y()-5, 
                                           geometry.width()+10, geometry.height()+10))
            self.animation.start()
        def on_leave():
            geometry = btn.geometry()
            self.animation.setStartValue(geometry)
            self.animation.setEndValue(QRect(geometry.x()+5, geometry.y()+5, 
                                           geometry.width()-10, geometry.height()-10))
            self.animation.start()
        btn.enterEvent = lambda e: on_hover()
        btn.leaveEvent = lambda e: on_leave()
        return btn

    def crear_boton_suave(self, texto, funcion):
        btn = QPushButton(texto)
        btn.setFixedSize(280, 50)  
        btn.setStyleSheet("""
            QPushButton {
                background-color: rgba(46, 204, 113, 0.3);
                color: #2ecc71;
                border: 2px solid #2ecc71;
                padding: 10px;
                font-size: 16px;
                font-weight: bold;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: rgba(46, 204, 113, 0.5);
                border: 3px solid #27ae60;
            }
        """)

        btn.clicked.connect(lambda: self.reproducir_sonido_y_funcion(funcion))
        return btn

    def crear_boton_nav(self, texto, funcion, layout):
        btn = QPushButton(texto)
        btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #2ecc71;
                border: 2px solid #2ecc71;
                border-radius: 5px;
                text-align: left;
                padding: 10px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: rgba(46, 204, 113, 0.2);
            }
        """)
        btn.clicked.connect(funcion)
        layout.addWidget(btn)
        
    def crear_boton_social(self, texto, link):
        btn = QPushButton(texto)
        btn.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(link)))
        return btn

    def log(self, mensaje):
        if hasattr(self, 'log_console'):
            self.log_console.append(f"> {mensaje}")
        else:
            print(f"> {mensaje}")  
        
    def mostrar_main(self):
        self.stack.setCurrentIndex(0)

    def mostrar_creditos(self):
        self.stack.setCurrentIndex(1)

    def crear_pagina_creditos(self):        
        credits_page = QWidget()
        credits_layout = QVBoxLayout(credits_page)
        credits_layout.setSpacing(40)
        credits_layout.setContentsMargins(50, 50, 50, 50)
        
        credits_container = QWidget()
        credits_container.setFixedHeight(400)
        credits_container.setStyleSheet("""
            QWidget {
                background-color: rgba(0, 0, 0, 0.9);
                border: 4px solid #2ecc71;
                border-radius: 15px;
                padding: 40px;
            }
            QLabel {
                color: #2ecc71;
                font-weight: bold;
                background-color: rgba(0, 0, 0, 0.7);
                border-radius: 10px;
                padding: 20px;
            }
        """)
        credits_container_layout = QVBoxLayout(credits_container)
        credits_container_layout.setSpacing(30)
        
        titulo = QLabel("THO OPTIMIZER 2.0", alignment=Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 48px;")
        
        credits_text = QLabel("GITHUB BY: HANNIBAL THO", alignment=Qt.AlignCenter)
        credits_text.setStyleSheet("font-size: 32px;")
        
        paypal_text = QLabel("PayPal: cakarrota2022@gmail.com", alignment=Qt.AlignCenter)
        paypal_text.setStyleSheet("font-size: 24px;")
        
        for widget in [titulo, credits_text, paypal_text]:
            credits_container_layout.addWidget(widget)
        
        social_container = QWidget()
        social_container.setFixedHeight(150)
        social_container.setStyleSheet("""
            QWidget {
                background-color: rgba(0, 0, 0, 0.7);
                border: 4px solid #2ecc71;
                border-radius: 15px;
                padding: 20px;
            }
            QPushButton {
                background-color: rgba(46, 204, 113, 0.3);
                color: #2ecc71;
                border: 3px solid #2ecc71;
                border-radius: 12px;
                padding: 10px;
                font-size: 16px;
                font-weight: bold;
                min-width: 200px;
                max-width: 200px;
            }
            QPushButton:hover {
                background-color: rgba(46, 204, 113, 0.5);
                border: 4px solid #27ae60;
            }
        """)
        social_layout = QHBoxLayout(social_container)
        social_layout.setSpacing(50)  
        social_layout.setContentsMargins(40, 20, 40, 20)  
        social_layout.setAlignment(Qt.AlignCenter)

        botones_sociales = [
            ("🎮 DISCORD", "https://discord.gg/4svwzsy3UP"),
            ("📺 YOUTUBE", "https://www.youtube.com/@TODO-HACK-OFFICIAL"),
            ("💰 DONAR", "https://www.paypal.com/sendmoney?email=cakarrota2022@gmail.com")
        ]

        for texto, url in botones_sociales:
            btn = QPushButton(texto)
            btn.setFixedSize(200, 50)  
            btn.clicked.connect(lambda checked, u=url: QDesktopServices.openUrl(QUrl(u)))
            social_layout.addWidget(btn)

        credits_layout.addStretch(1)
        credits_layout.addWidget(credits_container)
        credits_layout.addWidget(social_container)
        credits_layout.addStretch(1)
        
        return credits_page

    def elevar_privilegios(self):
        try:

            if ctypes.windll.shell32.IsUserAnAdmin() == 0:
                self.log("Solicitando privilegios de administrador...")
                ctypes.windll.shell32.ShellExecuteW(
                    None, "runas", sys.executable, " ".join(sys.argv), None, 1
                )
                sys.exit()

            try:
                import win32security
                import win32api
                current = win32security.OpenProcessToken(
                    win32api.GetCurrentProcess(),
                    win32security.TOKEN_ADJUST_PRIVILEGES | win32security.TOKEN_QUERY
                )
                privilegios = [
                    "SeBackupPrivilege",
                    "SeRestorePrivilege",
                    "SeShutdownPrivilege",
                    "SeTakeOwnershipPrivilege",
                    "SeDebugPrivilege"
                ]
                for privilegio in privilegios:
                    try:
                        win32security.AdjustTokenPrivileges(
                            current, False,
                            [(win32security.LookupPrivilegeValue(None, privilegio),
                              win32security.SE_PRIVILEGE_ENABLED)]
                        )
                        self.log(f"Privilegio {privilegio} activado")
                    except Exception as e:
                        self.log(f"No se pudo elevar el privilegio {privilegio}")
                        
            except ImportError:
                self.log("Ejecutando con privilegios de administrador básicos")
        except Exception as e:        
            self.log(f"Error al elevar privilegios: {str(e)}")

    def optimizar_servicios(self):
        try:
            servicios_innecesarios = [
                "DiagTrack",  
                "dmwappushservice",  
                "SysMain",  
                "WSearch",  
                "XboxGipSvc",  
                "XblAuthManager",
                "XblGameSave",
                "TabletInputService",  
                "Remote Registry",  
                "PrintNotify",  
                "fax",  
            ]
            self.log("Verificando servicios innecesarios...")
            servicios_desactivados = 0
            
            for servicio in servicios_innecesarios:
                result = subprocess.run(f'sc query "{servicio}"', shell=True, capture_output=True)
                if result.returncode == 0:  
                    os.system(f'net stop "{servicio}" >nul 2>&1')
                    os.system(f'sc config "{servicio}" start=disabled >nul 2>&1')
                    servicios_desactivados += 1
                    self.log(f"Servicio {servicio} desactivado")

            if (servicios_desactivados > 0):
                self.log(f"Se desactivaron {servicios_desactivados} servicios innecesarios")
            else:
                self.log("No se encontraron servicios innecesarios para desactivar")
            
            self.log("THO SERVICIOS se aplicó correctamente")
            
        except Exception as e:
            self.log(f"Error: {str(e)}")
            self.mostrar_error("Error", f"Error durante la optimización de servicios: {str(e)}")

    def limpiar_temporales(self):
        try:
            self.log("Iniciando limpieza de archivos temporales...")
            
            rutas_temp = [
                os.environ.get('TEMP'),
                os.environ.get('TMP'),
                r'C:\Windows\Temp',
                r'C:\Windows\Prefetch',
                os.path.join(os.environ.get('LOCALAPPDATA'), 'Temp'),
                os.path.join(os.environ.get('APPDATA'), 'Temp')
            ]
            for ruta in rutas_temp:
                if ruta and os.path.exists(ruta):
                    self.log(f"Limpiando: {ruta}")
                    os.system(f'del /s /f /q "{ruta}\\*.*" >nul 2>&1')  
            
            self.log("THO TEMP se aplicó correctamente")
            
        except Exception as e:
            self.log(f"Error: {str(e)}")
            self.mostrar_error("Error", f"Error durante la limpieza: {str(e)}")

    def optimizar_ram(self):
        try:
            self.log("Optimizando memoria RAM...")
            
            ctypes.windll.psapi.EmptyWorkingSet(ctypes.c_int(-1))
            
            subprocess.run('ipconfig /flushdns', shell=True)
            
            os.system('powershell -Command "Clear-RecycleBin -Force" >nul 2>&1')
            
            self.log("THO RAM se aplicó correctamente")
            
        except Exception as e:
            self.log(f"Error: {str(e)}")
            self.mostrar_error("Error", f"Error durante la optimización de RAM: {str(e)}")

    def optimizar_gpu(self):
        try:
            self.log("Optimizando GPU...")
            
            shader_paths = [
                os.path.join(os.environ.get('LOCALAPPDATA'), 'NVIDIA\\GLCache'),
                os.path.join(os.environ.get('LOCALAPPDATA'), 'AMD\\GLCache'),
                os.path.join(os.environ.get('LOCALAPPDATA'), 'Intel\\GLCache')
            ]
            found_gpu = False
            for path in shader_paths:
                if os.path.exists(path):
                    found_gpu = True
                    self.log(f"Limpiando caché de shaders: {path}")
                    os.system(f'del /s /f /q "{path}\\*.*" >nul 2>&1')  
            
            if not found_gpu:
                self.log("No se encontró caché de GPU para limpiar")
            
            self.log("THO GPU se aplicó correctamente")
            
        except Exception as e:
            self.log(f"Error: {str(e)}")
            self.mostrar_error("Error", f"Error durante la optimización de GPU: {str(e)}")

    def optimizar_servicios_extremo(self):
        try:
            self.log("Iniciando optimización extrema del sistema...")
            
            registry_optimizations = [
                {
                    'path': r'SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management',
                    'values': {
                        'LargeSystemCache': (winreg.REG_DWORD, 1),
                        'SystemCacheDirtyPageThreshold': (winreg.REG_DWORD, 1000),
                        'IoPageLockLimit': (winreg.REG_DWORD, 983040)
                    }
                },
                {
                    'path': r'SYSTEM\CurrentControlSet\Control\PriorityControl',
                    'values': {
                        'Win32PrioritySeparation': (winreg.REG_DWORD, 38)
                    }
                },
                {
                    'path': r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile',
                    'values': {
                        'SystemResponsiveness': (winreg.REG_DWORD, 0),
                        'NetworkThrottlingIndex': (winreg.REG_DWORD, 4294967295)
                    }
                }
            ]

            for reg_key in registry_optimizations:
                try:
                    key = winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, reg_key['path'], 0, winreg.KEY_ALL_ACCESS)
                    for value_name, (value_type, value_data) in reg_key['values'].items():
                        winreg.SetValueEx(key, value_name, 0, value_type, value_data)
                    winreg.CloseKey(key)
                    self.log(f"Registro optimizado: {reg_key['path']}")
                except Exception as e:
                    self.log(f"Error al modificar registro {reg_key['path']}: {str(e)}")

            system_commands = [
                'powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61',
                'powercfg /setactive e9a42b02-d5df-448d-aa00-03f14749eb61',
                'bcdedit /set disabledynamictick yes',
                'bcdedit /set useplatformtick yes',
                'bcdedit /set useplatformclock false',
                'bcdedit /timeout 0',
                'bcdedit /set nx OptOut',
                'bcdedit /set bootux disabled',
                'bcdedit /set bootmenupolicy legacy',
                'bcdedit /set hypervisorlaunchtype off',
                'bcdedit /set tpmbootentropy ForceDisable',
                'bcdedit /set linearaddress57 OptOut',
                'bcdedit /set increaseuserva 268435328',
                'bcdedit /set firstmegabytepolicy UseAll',
                'bcdedit /set avoidlowmemory 0x8000000',
                'bcdedit /set nolowmem Yes'
            ]

            for cmd in system_commands:
                try:
                    subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    self.log(f"Comando ejecutado: {cmd}")
                except Exception as e:
                    self.log(f"Error al ejecutar comando {cmd}: {str(e)}")

            servicios_innecesarios = [
                "DiagTrack", "dmwappushservice", "SysMain", "WSearch", 
                "XboxGipSvc", "XblAuthManager", "XblGameSave", "TabletInputService",
                "Remote Registry", "PrintNotify", "fax", "WpnService", "RetailDemo",
                "DoSvc", "PcaSvc", "WMPNetworkSvc", "WerSvc", "MapsBroker",
                "iphlpsvc", "lmhosts", "SEMgrSvc", "BTAGService", "Browser",
                "BthAvctpSvc", "CDPUserSvc", "PimIndexMaintenanceSvc", "OneSyncSvc",
                "WpcMonSvc", "FontCache", "SharedAccess", "StorSvc", "PhoneSvc",
                "SCardSvr", "Spooler", "PrintNotify", "TapiSrv", "BITS", "BDESVC",
                "DusmSvc", "DPS", "WdiSystemHost", "WdiServiceHost"
            ]
            
            for servicio in servicios_innecesarios:
                try:
                    subprocess.run(f'net stop "{servicio}" /y', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    subprocess.run(f'sc config "{servicio}" start=disabled', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    self.log(f"Servicio desactivado: {servicio}")
                except Exception:
                    pass

            self.log("Optimización extrema completada exitosamente")
            self.mostrar_mensaje("Éxito", "Optimización extrema aplicada. Se recomienda reiniciar el sistema.")
            
        except Exception as e:
            self.log(f"Error en optimización extrema: {str(e)}")
            self.mostrar_error("Error", "Error durante la optimización extrema")

    def activar_modo_juego(self):
        try:
            self.log("Activando modo juego...")
            
            subprocess.run('powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c', shell=True)
            
            key = winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, 
                                   r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games",
                                   0, winreg.KEY_ALL_ACCESS)
            winreg.SetValueEx(key, "GPU Priority", 0, winreg.REG_DWORD, 8)
            winreg.SetValueEx(key, "Priority", 0, winreg.REG_DWORD, 6)
            winreg.SetValueEx(key, "Scheduling Category", 0, winreg.REG_SZ, "High")
            
            self.log("Modo juego activado correctamente")
            self.mostrar_mensaje("Éxito", "Modo juego activado")
            
        except Exception as e:
            self.log(f"Error: {str(e)}")
            self.mostrar_error("Error", "Error al activar modo juego")

    def optimizar_bateria(self):
        try:
            self.log("Optimizando configuración de batería...")
            
            subprocess.run('powercfg /setactive 381b4222-f694-41f0-9685-ff5bb260df2e', shell=True)
            
            subprocess.run('powercfg /change monitor-timeout-ac 10', shell=True)
            subprocess.run('powercfg /change monitor-timeout-dc 5', shell=True)
            
            self.log("Optimización de batería completada")
            self.mostrar_mensaje("Éxito", "Configuración de batería optimizada")
            
        except Exception as e:
            self.log(f"Error: {str(e)}")
            self.mostrar_error("Error", "Error al optimizar batería")

    def optimizar_temperatura(self):
        try:
            self.log("Optimizando temperatura del sistema...")
            
            self.limpiar_temporales()
            
            subprocess.run('powershell -Command "Get-WmiObject -Namespace root/wmi -Class MSAcpi_ThermalZoneTemperature"', shell=True)
            
            self.log("Optimización de temperatura completada")
            self.mostrar_mensaje("Éxito", "Sistema optimizado para mejor temperatura")
            
        except Exception as e:
            self.log(f"Error: {str(e)}")
            self.mostrar_error("Error", "Error al optimizar temperatura")

    def optimizar_red(self):
        try:
            self.log("Optimizando red...")
            
            network_commands = [
                'netsh int tcp set global autotuninglevel=normal',
                'netsh int tcp set global chimney=enabled',
                'netsh int tcp set global dca=enabled',
                'netsh int tcp set global ecncapability=enabled',
                'netsh int tcp set global timestamps=disabled',
                'netsh int tcp set global rss=enabled',
                'netsh int tcp set global nonsackrttresiliency=disabled',
                'netsh interface tcp set heuristics disabled',
                'netsh int tcp set supplemental internet congestionprovider=ctcp',
                'netsh int tcp set global initialRto=2000',
                'ipconfig /flushdns',
                'ipconfig /registerdns',
                'netsh winsock reset'
            ]
            
            for cmd in network_commands:
                subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                self.log(f"Ejecutado: {cmd}")
            
            dns_key = winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, 
                                       r"SYSTEM\CurrentControlSet\Services\Dnscache\Parameters",
                                       0, winreg.KEY_ALL_ACCESS)
            winreg.SetValueEx(dns_key, "MaxCacheTtl", 0, winreg.REG_DWORD, 86400)
            winreg.SetValueEx(dns_key, "MaxNegativeCacheTtl", 0, winreg.REG_DWORD, 0)
            
            self.log("Optimización de red completada")
            self.mostrar_mensaje("Éxito", "Red optimizada correctamente")
            
        except Exception as e:
            self.log(f"Error: {str(e)}")
            self.mostrar_error("Error", "Error al optimizar red")

    def optimizar_seguridad(self):
        try:
            self.log("Optimizando seguridad...")
            
            security_commands = [
                'sc start SecurityHealthService',
                'sc config SecurityHealthService start=auto',
                'powershell Set-MpPreference -DisableRealtimeMonitoring $false',
                'powershell Set-MpPreference -SubmitSamplesConsent 1',
                'netsh advfirewall set allprofiles state on',
                'netsh advfirewall firewall set rule group="Red doméstica/trabajo (TCP-Entrada)" new enable=yes',
                'netsh advfirewall firewall set rule group="Red doméstica/trabajo (UDP-Entrada)" new enable=yes'
            ]
            
            for cmd in security_commands:
                subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            self.log("Configuración de seguridad optimizada")
            self.mostrar_mensaje("Éxito", "Seguridad optimizada")
            
        except Exception as e:
            self.log(f"Error: {str(e)}")
            self.mostrar_error("Error", "Error al optimizar seguridad")

    def optimizar_sistema(self):
        try:
            self.log("Optimizando sistema...")
            
            system_commands = [
                'powercfg -h off',  
                'fsutil behavior set disablelastaccess 1',  
                'fsutil behavior set memoryusage 2',  
                'schtasks /Change /TN "\\Microsoft\\Windows\\Registry\\RegIdleBackup" /Disable',
                'schtasks /Change /TN "\\Microsoft\\Power Efficiency Diagnostics\\AnalyzeSystem" /Disable',
                'bcdedit /set useplatformclock no',
                'bcdedit /set disabledynamictick yes',
                'bcdedit /set bootmenupolicy legacy',
                'powershell Disable-MMAgent -mc',  
                'powershell Set-ProcessMitigation -System -Disable DEP,SEHOP'  
            ]
            
            for cmd in system_commands:
                subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                self.log(f"Ejecutado: {cmd}")
            
            registry_optimizations = [
                {
                    'path': r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management",
                    'values': {
                        "LargeSystemCache": (winreg.REG_DWORD, 1),
                        "IoPageLockLimit": (winreg.REG_DWORD, 983040)
                    }
                },
                {
                    'path': r"SYSTEM\CurrentControlSet\Control\Power",
                    'values': {
                        "HibernateEnabled": (winreg.REG_DWORD, 0)
                    }
                }
            ]
            
            for reg_key in registry_optimizations:
                try:
                    key = winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, reg_key['path'], 0, winreg.KEY_ALL_ACCESS)
                    for name, (type_, value) in reg_key['values'].items():
                        winreg.SetValueEx(key, name, 0, type_, value)
                    winreg.CloseKey(key)
                except Exception as e:
                    self.log(f"Error en registro {reg_key['path']}: {str(e)}")
            
            self.log("Sistema optimizado correctamente")
            self.mostrar_mensaje("Éxito", "Sistema optimizado al máximo")
            
        except Exception as e:
            self.log(f"Error: {str(e)}")
            self.mostrar_error("Error", "Error al optimizar sistema")

    def optimizar_apps(self):
        try:
            self.log("Optimizando aplicaciones...")
            
            subprocess.run('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\BackgroundAccessApplications" /v "GlobalUserDisabled" /t REG_DWORD /d "1" /f', shell=True)
            
            apps_to_remove = [
                "Microsoft.BingWeather",
                "Microsoft.GetHelp",
                "Microsoft.Getstarted",
                "Microsoft.Microsoft3DViewer",
                "Microsoft.MicrosoftOfficeHub",
                "Microsoft.MicrosoftSolitaireCollection",
                "Microsoft.MixedReality.Portal",
                "Microsoft.People",
                "Microsoft.SkypeApp",
                "Microsoft.WindowsFeedbackHub",
                "Microsoft.Xbox.TCUI",
                "Microsoft.XboxApp",
                "Microsoft.XboxGameOverlay",
                "Microsoft.XboxGamingOverlay",
                "Microsoft.XboxIdentityProvider",
                "Microsoft.XboxSpeechToTextOverlay",
                "Microsoft.YourPhone",
                "Microsoft.ZuneMusic",
                "Microsoft.ZuneVideo"
            ]
            
            for app in apps_to_remove:
                subprocess.run(f'powershell -command "Get-AppxPackage *{app}* | Remove-AppxPackage"', 
                             shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            services_to_disable = [
                "AppXSvc",
                "ClipSVC",
                "TabletInputService",
                "RetailDemo",
                "MessagingService"
            ]
            
            for service in services_to_disable:
                subprocess.run(f'sc config "{service}" start=disabled', shell=True)
                subprocess.run(f'sc stop "{service}"', shell=True)
            
            self.log("Aplicaciones optimizadas correctamente")
            self.mostrar_mensaje("Éxito", "Aplicaciones optimizadas")
            
        except Exception as e:
            self.log(f"Error: {str(e)}")
            self.mostrar_error("Error", "Error al optimizar aplicaciones")

    def optimizar_fps(self):
        try:
            self.log("Optimizando FPS del sistema...")
            
            performance_settings = [
                {
                    'path': r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games",
                    'values': {
                        "GPU Priority": (winreg.REG_DWORD, 8),
                        "Priority": (winreg.REG_DWORD, 6),
                        "Scheduling Category": (winreg.REG_SZ, "High"),
                        "SFIO Priority": (winreg.REG_SZ, "High")
                    }
                },
                {
                    'path': r"SOFTWARE\Microsoft\Games",
                    'values': {
                        "FpsAll": (winreg.REG_DWORD, 1),
                        "GameFluidity": (winreg.REG_DWORD, 1)
                    }
                }
            ]
            
            for setting in performance_settings:
                try:
                    key = winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, setting['path'], 0, winreg.KEY_ALL_ACCESS)
                    for name, (type_, value) in setting['values'].items():
                        winreg.SetValueEx(key, name, 0, type_, value)
                    winreg.CloseKey(key)
                except Exception as e:
                    self.log(f"Error en registro {setting['path']}: {str(e)}")

            fps_commands = [
                'powercfg -setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c',
                'bcdedit /set useplatformclock false',
                'bcdedit /set disabledynamictick yes',
                'bcdedit /set tscsyncpolicy enhanced'
            ]

            for cmd in fps_commands:
                subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                self.log(f"Ejecutado: {cmd}")

            self.log("Optimización de FPS completada")
            self.mostrar_mensaje("Éxito", "FPS optimizados correctamente")
            
        except Exception as e:
            self.log(f"Error: {str(e)}")
            self.mostrar_error("Error", "Error al optimizar FPS")

    def optimizar_defender(self):
        try:
            self.log("Optimizando Windows Defender...")
            
            defender_commands = [
                'powershell Set-MpPreference -DisableRealtimeMonitoring $false',
                'powershell Add-MpPreference -ExclusionPath "C:\\Games"',
                'powershell Set-MpPreference -ScanAvgCPULoadFactor 50',
                'powershell Set-MpPreference -ScanOnlyIfIdleEnabled $true',
                'powershell Set-MpPreference -DisableArchiveScanning $true'
            ]
            
            for cmd in defender_commands:
                subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                self.log(f"Ejecutado: {cmd}")

            self.log("Windows Defender optimizado")
            self.mostrar_mensaje("Éxito", "Defender optimizado para gaming")
            
        except Exception as e:
            self.log(f"Error: {str(e)}")
            self.mostrar_error("Error", "Error al optimizar Defender")

    def optimizar_audio(self):
        try:
            self.log("Optimizando configuración de audio...")
            
            audio_commands = [
                'net stop Audiosrv',
                'net stop AudioEndpointBuilder',
                'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Audio" /v DisableProtectedAudioDG /t REG_DWORD /d 1 /f',
                'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Audio" /v DisableProtectedAudioDG /t REG_DWORD /d 1 /f',
                'net start Audiosrv',
                'net start AudioEndpointBuilder'
            ]
            
            for cmd in audio_commands:
                subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                self.log(f"Ejecutado: {cmd}")

            self.log("Audio optimizado correctamente")
            self.mostrar_mensaje("Éxito", "Audio optimizado para mejor rendimiento")
            
        except Exception as e:
            self.log(f"Error: {str(e)}")
            self.mostrar_error("Error", "Error al optimizar audio")

    def optimizar_visual(self):
        try:
            self.log("Optimizando rendimiento visual...")
            
            visual_settings = {
                r"Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects": {
                    "VisualFXSetting": (winreg.REG_DWORD, 2)
                },
                r"Control Panel\Desktop": {
                    "UserPreferencesMask": (winreg.REG_BINARY, b"\x90\x12\x03\x80\x10\x00\x00\x00")
                }
            }

            for path, values in visual_settings.items():
                try:
                    key = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_ALL_ACCESS)
                    for name, (type_, value) in values.items():
                        winreg.SetValueEx(key, name, 0, type_, value)
                    winreg.CloseKey(key)
                except Exception as e:
                    self.log(f"Error en registro {path}: {str(e)}")

            self.log("Efectos visuales optimizados")
            self.mostrar_mensaje("Éxito", "Rendimiento visual optimizado")
            
        except Exception as e:
            self.log(f"Error: {str(e)}")
            self.mostrar_error("Error", "Error al optimizar efectos visuales")

def main():
    app = QApplication(sys.argv)

    if not ctypes.windll.shell32.IsUserAnAdmin():
        if sys.platform == 'win32':
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, " ".join(sys.argv), None, 1
            )
            return
        else:
            QMessageBox.critical(None, "Error", "Este programa requiere privilegios de administrador")
            return
            
    app.setStyle('Fusion')
    ventana = OptimizadorTHO()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
