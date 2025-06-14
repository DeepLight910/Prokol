import os
import requests
import pygame
import time
import mimetypes
from urllib.parse import urlparse


def play_audio_from_url(url):
    # Замена для Dropbox
    if "www.dropbox.com" in url:
        url = url.replace("www.dropbox.com", "dl.dropboxusercontent.com", 1)

    # Определяем расширение файла
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    exp = os.path.splitext(filename)[1][1:]  # Извлекаем расширение (без точки)

    # Если расширение не найдено в URL, определяем по Content-Type
    if not exp:
        try:
            response = requests.head(url, allow_redirects=True)
            content_type = response.headers.get('Content-Type', '')
            exp = mimetypes.guess_extension(content_type.split(';')[0].strip())
            if exp and exp.startswith('.'):
                exp = exp[1:]
        except:
            exp = "tmp"  # Резервное расширение

    # Путь к кэш-директории
    cache_dir = os.path.expanduser("~/Documents/Audio")
    os.makedirs(cache_dir, exist_ok=True)
    temp_path = os.path.join(cache_dir, f"temp.{exp}")

    try:
        # Скачивание файла
        response = requests.get(url)
        response.raise_for_status()

        with open(temp_path, 'wb') as f:
            f.write(response.content)

        # Инициализация Pygame и воспроизведение
        pygame.mixer.init()
        pygame.mixer.music.load(temp_path)
        pygame.mixer.music.play()
    finally:
        # Очистка ресурсов
        pygame.mixer.quit()
        if os.path.exists(temp_path):
            os.remove(temp_path)