from random import randint

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps
from scipy.interpolate import make_interp_spline

# глобальные параметры
W, H = 1920, 1080
N_LINES = 2
GRID_SIZE = 75
GRID_COLOR = (50, 50, 50, 255)
BACKGROUND_COLOR = (0, 0, 0, 255)
TEXT_COLOR = (255, 255, 255, 255)
LINE_COLORS = {0: (119, 0, 255, 175),
               1: (0, 255, 255, 175),
               2: (255, 0, 196, 175),
               3: (56, 30, 102, 175),
               4: (68, 255, 47, 175),
               5: (140, 255, 127, 175),
               6: (255, 168, 255, 175),
               7: (168, 203, 255, 175),
               8: (168, 244, 255, 175),
               9: (255, 209, 168, 175),
               10: (185, 4, 34, 175),
               11: (185, 4, 94, 175),
               12: (149, 4, 185, 175),
               13: (34, 4, 185, 175),
               14: (4, 179, 185, 175),
               15: (255, 204, 204, 175)
               }
N_LINE_COLORS = 15
PHOTO_PATH = './horse.png'


def generate_sequence(n, axis):
    sequence = []
    i = 1
    if axis == 'x':
        while i < n:
            number = randint(0, 1920)
            if number in sequence:
                continue
            else:
                sequence.append(number)
                i += 1

        return sorted(sequence)

    elif axis == 'y':
        while i < n:
            number = randint(0, 1080)
            if number in sequence:
                continue
            else:
                sequence.append(number)
                i += 1

        return sequence


def create_line(draw):
    x_ = np.array(generate_sequence(10, 'x'))
    y_ = np.array(generate_sequence(10, 'y'))

    x_y_spline = make_interp_spline(x_, y_)

    x = np.linspace(min(x_), max(x_), 5000)
    y = x_y_spline(x)

    plt.plot(x, y)
    plt.xlabel("X ось")
    plt.ylabel("Y ось")

    # Сохраняем график в буфер
    fig = plt.gcf()
    fig.canvas.draw()

    # Получаем объект Line2D из текущего графика
    line = plt.gca().lines[0]

    # Извлекаем координаты x и y линии
    x_data = line.get_xdata()
    y_data = line.get_ydata()

    # Масштабируем координаты линии под размеры изображения
    scale_x = W / (x.max() - x.min())
    scale_y = H / (y.max() - y.min())

    offset_x = -x.min() * scale_x
    offset_y = -y.min() * scale_y

    # Преобразуем координаты в целочисленные значения для рисования
    line_points = [(int((xi - x.min()) * scale_x + offset_x), int(H - (yi - y.min()) * scale_y - offset_y)) for
                   xi, yi in zip(x_data, y_data)]

    # Рисуем линию на изображении
    draw.line(line_points, width=randint(5, 15), fill=LINE_COLORS[randint(0, N_LINE_COLORS)])


def draw_grid(draw):
    # Рисование сетки
    for x in range(0, W, GRID_SIZE):
        draw.line([(x, 0), (x, H)], fill=GRID_COLOR, width=2)
    for y in range(0, W, GRID_SIZE):
        draw.line([(0, y), (W, y)], fill=GRID_COLOR, width=2)


def draw_text(draw):
    # Добавление текста
    font_path = "arial.ttf"  # Путь к шрифту (может потребоваться загрузить)
    font = ImageFont.truetype(font_path, size=72)
    text = "Ваши жопы под охраной\nСпите спокойно мои хорошие\n\nВсех целую )"
    text_x = 75
    text_y = 100
    draw.text((text_x, text_y), text, font=font, fill=TEXT_COLOR)


def add_person_image(draw, image):
    photo = Image.open(PHOTO_PATH)
    center_x = photo.width // 2
    center_y = photo.height // 2
    n = 200
    photo = photo.crop((center_x - n, center_y - n, center_x + n, center_y + n))
    photo = photo.resize((600, 600))

    # Создаем круглую маску
    mask = Image.new('L', photo.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + photo.size, fill=255)

    # Применяем маску к изображению
    circular_image = ImageOps.fit(photo, mask.size, centering=(0.2, 0.2))
    circular_image.putalpha(mask)

    # Определяем позицию для размещения круглого изображения
    position = (1300, 450)

    # Накладываем круглое изображение на фон
    image.paste(circular_image, position, circular_image)


def main():
    # Создаем новый объект Image, на котором будет фон и линия
    image = Image.new("RGBA", (W, H), BACKGROUND_COLOR)

    # Создаем объект ImageDraw для рисования на изображении
    draw = ImageDraw.Draw(image)
    # Рисуем сетку
    draw_grid(draw)
    # Рисуем линии
    for _ in range(N_LINES):
        create_line(draw)

    # Draw a rounded rectangle
    draw.rounded_rectangle((50, 50, 1250, 1020), outline=TEXT_COLOR, width=5, radius=30)

    # Рисуем текст
    draw_text(draw)
    # Рисуем фото человека
    add_person_image(draw, image)

    # Сохраняем итоговое изображение
    image.save("дуги(2).png")
    print("Изображение успешно создано.")


if __name__ == '__main__':
    main()
