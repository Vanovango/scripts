from PIL import Image, ImageDraw


# Функция для создания градиента между двумя цветами
def gradient_color(start_color, end_color, steps):
    """
    Создает градиент между двумя цветами.

    :param start_color: Начальный цвет (RGB).
    :param end_color: Конечный цвет (RGB).
    :param steps: Количество шагов (цветов) в градиенте.
    :return: Список цветов градиента.
    """
    r1, g1, b1 = start_color
    r2, g2, b2 = end_color
    colors = []
    for i in range(steps):
        r = int(r1 + (r2 - r1) * i / (steps - 1))
        g = int(g1 + (g2 - g1) * i / (steps - 1))
        b = int(b1 + (b2 - b1) * i / (steps - 1))
        colors.append((r, g, b))
    return colors


# Функция для рисования градиентной линии
def draw_gradient_line(draw, start_point, end_point, start_color, end_color, steps=100, width=5):
    """
    Рисует градиентную линию.

    :param draw: Объект ImageDraw.
    :param start_point: Начальная точка линии (x, y).
    :param end_point: Конечная точка линии (x, y).
    :param start_color: Начальный цвет градиента (RGB).
    :param end_color: Конечный цвет градиента (RGB).
    :param steps: Количество шагов (цветов) в градиенте.
    :param width: Толщина линии.
    """
    # Создаем градиентные цвета
    colors = gradient_color(start_color, end_color, steps)

    # Вычисляем координаты для каждой линии
    x1, y1 = start_point
    x2, y2 = end_point
    dx = (x2 - x1) / (steps - 1)
    dy = (y2 - y1) / (steps - 1)

    # Рисуем линии с градиентом
    for i in range(steps):
        current_x = int(x1 + i * dx)
        current_y = int(y1 + i * dy)
        next_x = int(x1 + (i + 1) * dx)
        next_y = int(y1 + (i + 1) * dy)
        draw.line([(current_x, current_y), (next_x, next_y)], fill=colors[i], width=width)


# Пример использования
if __name__ == "__main__":
    # Создаем новое изображение
    image = Image.new("RGB", (800, 600), (0, 0, 0))
    draw = ImageDraw.Draw(image)

    # Определяем точки и цвета для градиентной линии
    start_point = (100, 100)
    end_point = (700, 500)
    start_color = (255, 0, 0)  # Красный
    end_color = (0, 0, 255)  # Синий

    # Рисуем градиентную линию
    draw_gradient_line(draw, start_point, end_point, start_color, end_color, steps=100, width=5)

    # Сохраняем изображение
    image.save("градиент(3).png")
    print("Изображение успешно создано.")
