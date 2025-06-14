from ctypes import *

def Disable():
    windll.user32.BlockInput(True)

def Enable():
    windll.user32.BlockInput(False)