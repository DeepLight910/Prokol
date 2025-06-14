import sys
import os


def resource_path(relative_path):
    """
    Получает абсолютный путь к ресурсу. Работает для:
    - режима разработки (когда скрипт запущен напрямую)
    - однофайлового режима PyInstaller
    """
    try:
        # PyInstaller создает временную папку в _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Функция для проверки работы в собранном приложении
def is_frozen():
    """Проверяет, запущено ли приложение в собранном виде (exe)"""
    return hasattr(sys, 'frozen') or hasattr(sys, '_MEIPASS')

def get_exe_dir():
    """
    Возвращает путь к директории, где находится исполняемый файл (.exe)
    - В собранном режиме: путь к папке с .exe
    - В режиме разработки: путь к папке проекта
    """
    if is_frozen():
        # Если приложение "заморожено" (скомпилировано)
        return os.path.dirname(sys.executable)
    else:
        # В режиме разработки - возвращаем папку проекта
        return os.path.dirname(os.path.abspath(__file__))

def get_exe_path():
    """
    Возвращает полный путь к исполняемому файлу (.exe)
    - В собранном режиме: полный путь к .exe
    - В режиме разработки: путь к main.py
    """
    if is_frozen():
        return sys.executable
    else:
        return os.path.abspath(__file__)