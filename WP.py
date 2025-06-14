import os
import ctypes
from utils import resource_path
import shutil
import winreg


def get_wallpaper_path():
    """Получает путь к текущим обоям из реестра Windows"""
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Control Panel\Desktop") as key:
            path, _ = winreg.QueryValueEx(key, "Wallpaper")
            return path
    except Exception as e:
        print(f"Ошибка при чтении реестра: {e}")
        return None


def save_current_wallpaper(dest_path):
    """Сохраняет текущие обои в указанное место"""
    src_path = get_wallpaper_path()
    if not src_path or not os.path.exists(src_path):
        print("Не удалось найти текущие обои")
        return False

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    try:
        shutil.copy2(src_path, dest_path)
        print(f"Сохранены текущие обои: {dest_path}")
        return True
    except Exception as e:
        print(f"Ошибка при сохранении обоев: {e}")
        return False


def set_wallpaper(image_path):
    """Устанавливает новые обои из абсолютного пути"""
    try:
        SPI_SETDESKWALLPAPER = 0x0014
        SPIF_UPDATEINIFILE = 0x01
        SPIF_SENDCHANGE = 0x02

        if not os.path.exists(image_path):
            return False

        ctypes.windll.user32.SystemParametersInfoW(
            SPI_SETDESKWALLPAPER,
            0,
            image_path,
            SPIF_UPDATEINIFILE | SPIF_SENDCHANGE
        )
        return True
    except Exception as e:
        return False


def wallpaper_action(action, image_path=None):
    """
    Основная функция для управления обоями

    Параметры:
    action: "set" для установки новых обоев, "restore" для восстановления
    image_path: Относительный или абсолютный путь к файлу обоев (только для action="set")

    Возвращает:
    True - операция успешна, False - произошла ошибка
    """
    # Определяем путь для сохранения оригинальных обоев
    docs_dir = os.path.expanduser("~/Documents")
    original_path = os.path.join(docs_dir, "wallpaper", "original.png")

    # Восстановление обоев
    if action == "restore":
        if os.path.exists(original_path):
            return set_wallpaper(original_path)
        return False

    # Установка новых обоев
    elif action == "set":
        if not image_path:
            return False

        # Преобразуем относительный путь в абсолютный
        if not os.path.isabs(image_path):
            # Получаем путь к директории текущего скрипта
            script_dir = os.path.dirname(os.path.abspath(__file__))
            abs_path = os.path.join(script_dir, image_path)
        else:
            abs_path = image_path

        # Сохраняем текущие обои перед первой установкой
        if not os.path.exists(original_path):
            save_current_wallpaper(original_path)

        return set_wallpaper(abs_path)

    else:
        return False