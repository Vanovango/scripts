import random

from PIL import Image, ImageDraw, ImageFont

# Настройки изображения
WIDTH, HEIGHT = 1920, 1080
BACKGROUND_COLOR = (0, 0, 0)
GRID_COLOR = (50, 50, 50)
LINE_COLOR_RANGE = [(128, 0, 128), (192, 0, 192)]  # Диапазон цветов для линий
TEXT_COLOR = (255, 255, 255)

# Создание нового изображения
image = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND_COLOR)
draw = ImageDraw.Draw(image)

# Рисование сетки
grid_size = 50
for x in range(0, WIDTH, grid_size):
    draw.line([(x, 0), (x, HEIGHT)], fill=GRID_COLOR, width=2)
for y in range(0, HEIGHT, grid_size):
    draw.line([(0, y), (WIDTH, y)], fill=GRID_COLOR, width=2)


# Функция для рисования случайной кривой
def draw_random_curve(draw, color):
    points = []
    for i in range(7):  # Количество контрольных точек
        x = i * (WIDTH // 9) + random.randint(-50, 50)
        y = random.randint(0, HEIGHT)
        points.append((x, y))

    # Добавление начальной и конечной точки
    points.insert(0, (0, random.randint(0, HEIGHT)))
    points.append((WIDTH, random.randint(0, HEIGHT)))

    # Рисование кривой
    draw.line(points, fill=color, width=10)


# Генерация случайных линий
num_lines = 2
for _ in range(num_lines):
    line_color = (
        random.randint(LINE_COLOR_RANGE[0][0], LINE_COLOR_RANGE[1][0]),
        random.randint(LINE_COLOR_RANGE[0][1], LINE_COLOR_RANGE[1][1]),
        random.randint(LINE_COLOR_RANGE[0][2], LINE_COLOR_RANGE[1][2])
    )
    draw_random_curve(draw, line_color)

# Добавление текста
font_path = "arial.ttf"  # Путь к шрифту (может потребоваться загрузить)
font = ImageFont.truetype(font_path, size=72)
text = "Руководство по использованию\nфирменного стиля"
text_x = 50
text_y = 500
draw.text((text_x, text_y), text, font=font, fill=TEXT_COLOR)

# Сохранение изображения
image.save("ломанные(1).png")
print("Изображение успешно создано.")



