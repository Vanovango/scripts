from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os


def generate_qr(user_id: int, fio: str, passport: str) -> str:
    """
    Функция создает гостевой qr-код и сохраняет его в определенную папку
    :param user_id: название qr-кода
    :param fio: ФИО
    :param passport: серия и номер
    P.S. добавить время генерации qr-кода + лого ТП
    :return: возвращает путь до созданного qr-кода
    """
    save_dir = './generated_qr'
    qr_name = f"{user_id}.png"
    font_base = ImageFont.truetype("arial.ttf", 60)
    font_fio = ImageFont.truetype("arial.ttf", 75)

    qr = Image.open(qr_name)
    qr_resize = qr.resize((900, 900))

    if not os.path.isdir(save_dir):
        os.mkdir(save_dir)

    # создаем новое изображение
    generate_qr = Image.new("RGB", (1000, 1700), (255, 255, 255, 255))

    # загружаем логотип
    logo = Image.open("./logo.png")
    logo_resize = logo.resize((1000, 200))

    # загружаем qr-код
    generate_qr.paste(logo_resize, (15, 0))
    generate_qr.paste(qr_resize, (50, 250))

    # РИСУЕМ ЛИНИЮ
    line = ImageDraw.Draw(generate_qr)
    line.line([(0, 210), (1000, 210)], fill=(0, 0, 0, 0), width=15)

    # рисуем фио
    # разделяем на фамилию имя и отчество
    fio_slit = [i for i in fio.split()]
    # рисуем фамилию
    text_f = ImageDraw.Draw(generate_qr)
    text_f.text((50, 1150), f"{fio_slit[0]}", font=font_fio, fill=(0, 0, 0, 0), stroke_width=1)
    # рисуем имя и отчество
    text_io = ImageDraw.Draw(generate_qr)
    text_io.text((50, 1225), f"{' '.join(i for i in fio_slit[1:3])}", font=font_fio, fill=(0, 0, 0, 0))

    # рисуем серию и номер паспорта
    text_passport = ImageDraw.Draw(generate_qr)
    text_passport.text((50, 1350), f"Паспорт: {passport}", font=font_base, fill=(0, 0, 0, 0))

    # рисуем дату и время
    time_ = datetime.now()
    text_time = ImageDraw.Draw(generate_qr)
    text_time.text((50, 1450), time_.strftime("%H:%M  |  %Y-%m-%d"), font=font_base, fill=(0, 0, 0, 0), stroke_width=1)

    # сохраняем результат
    save_path = save_dir + "/" + qr_name
    generate_qr.save(save_path)

    return save_dir + "/" + qr_name


if __name__ == "__main__":
    user_id = 1234567
    fio = "Краснослободцев Алексей Николаевич"
    passport = "4023 416912"

    print(generate_qr(user_id, fio, passport))
