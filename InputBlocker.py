from ctypes import *

def Disable(): # Отключаем ввод
    windll.user32.BlockInput(True)

def Enable(): # Включаем ввод
    windll.user32.BlockInput(False)