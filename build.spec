# -*- mode: python -*-
# build.spec
from PyInstaller.utils.hooks import collect_data_files

block_cipher = None

# Ресурсы проекта
added_files = [
    ('screams/*.png', 'screams'),
    ('screams/*.wav', 'screams'),
    ('screams/bsod.exe', 'screams')
]

a = Analysis(
    ['BotKxrvPersonal.py'],  # Основной скрипт
    pathex=[],
    binaries=[],
    datas=added_files,
    hiddenimports=[],   # Добавьте сюда проблемные импорты при необходимости
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    manifest= 'app.manifest',
    name='Armyane Horror X',       # Имя выходного файла
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,           # Сжатие исполняемого файла
    console=False,      # Без консольного окна (фоновое приложение)
    icon='Churka.ico',          # Путь к иконке приложения (если нужно)
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)