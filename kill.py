import os
import psutil
import win32gui
import win32process
import win32con

def get_visible_window_pids():
    """Получает PID всех процессов с видимыми окнами."""
    pids = set()

    def callback(hwnd, _):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd):
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            pids.add(pid)
        return True

    win32gui.EnumWindows(callback, None)
    return pids


def Kill(message):
    """
    Закрывает все процессы с видимыми окнами за исключением дискорда, питона, проводника, коммандной строки, и некоторых IDE
    :param message: Сообщение от бота
    :return: None
    """
    EXCLUDED_NAMES = {'discord.exe',  # Основной Discord
                    'discordptb.exe',
                    'discordcanary.exe',
                    'explorer.exe',
                    'cmd.exe',
                    'conhost.exe',
                    'python.exe',
                    'pythonw.exe',
                    'py.exe',
                    'code.exe',
                    'winws',
                    'devenv.exe'}

    current_pid = os.getpid()  # PID текущего скрипта
    parent_pid = psutil.Process(current_pid).ppid()  # PID родительского процесса

    try:
        # Получаем PID всех процессов с окнами
        visible_pids = get_visible_window_pids()

        for pid in visible_pids:
            try:
                proc = psutil.Process(pid)
                name = proc.name().lower()

                # Проверка исключений
                if (name in EXCLUDED_NAMES or
                        pid == current_pid or
                        pid == parent_pid):
                    continue

                # Принудительное завершение процесса
                proc.kill()

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

    except Exception as e:
        pass