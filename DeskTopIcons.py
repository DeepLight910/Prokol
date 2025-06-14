import ctypes
from ctypes import wintypes

# Константы для ShowWindow
SW_HIDE = 0
SW_SHOW = 5


def get_listview_hwnd():
    """Находит дескриптор окна со значками рабочего стола."""
    hwnd_progman = ctypes.windll.user32.FindWindowW("Progman", None)
    hwnd_shelldll = ctypes.windll.user32.FindWindowExW(
        hwnd_progman, None, "SHELLDLL_DefView", None
    )

    # Поиск в основном окне рабочего стола
    if hwnd_shelldll:
        return ctypes.windll.user32.FindWindowExW(
            hwnd_shelldll, None, "SysListView32", "FolderView"
        )

    # Поиск в альтернативных окнах (для современных версий Windows)
    def enum_windows(hwnd, _):
        nonlocal hwnd_shelldll
        buffer = ctypes.create_unicode_buffer(256)
        ctypes.windll.user32.GetClassNameW(hwnd, buffer, 256)
        if buffer.value == "WorkerW":
            child = ctypes.windll.user32.FindWindowExW(
                hwnd, None, "SHELLDLL_DefView", None
            )
            if child:
                hwnd_shelldll = child
                return False  # Остановить перебор
        return True  # Продолжить перебор

    callback = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)(enum_windows)
    ctypes.windll.user32.EnumWindows(callback, 0)

    if hwnd_shelldll:
        return ctypes.windll.user32.FindWindowExW(
            hwnd_shelldll, None, "SysListView32", "FolderView"
        )
    return None


def hide_desktop_icons():
    """Скрывает значки рабочего стола."""
    hwnd = get_listview_hwnd()
    if hwnd:
        ctypes.windll.user32.ShowWindow(hwnd, SW_HIDE)


def show_desktop_icons():
    """Показывает значки рабочего стола."""
    hwnd = get_listview_hwnd()
    if hwnd:
        ctypes.windll.user32.ShowWindow(hwnd, SW_SHOW)