from PIL import Image
import os


# путь до папки с анкетами
form_path = "C:/Users/voyte/Desktop/JPG_ancets"

# основная папка
main_dir = "Анкеты_разделенные_по_категориям"
if not os.path.isdir(main_dir):
    os.mkdir(f'./{main_dir}')


for directory in os.listdir(form_path):
    # перебор факультетов
    fac_num = os.fsdecode(directory)

    # путь для дальнейшего перебора
    fac_path = f"{form_path}/{fac_num}"

    # создаем папку факультета
    fac_dir = f"./{main_dir}/{fac_num}"
    if not os.path.isdir(fac_dir):
        os.mkdir(f'{fac_dir}')

    for curse in os.listdir(fac_path):
        # перебор курсов
        curs_num = os.fsdecode(curse)

        # путь для дальнейшего перебора
        curse_path = f"{fac_path}/{curs_num}"

        # создаем папку курса
        curse_dir = f"./{main_dir}/{fac_num}/{curs_num}"
        if not os.path.isdir(curse_dir):
            os.mkdir(f'{curse_dir}')

        # создаем папки для сегментов изображения
        if not (os.path.isdir(curse_dir + "/текст") or
                os.path.isdir(curse_dir + "/галочка") or
                os.path.isdir(curse_dir + "/цифра")):
            os.mkdir(f'{curse_dir}/текст')
            os.mkdir(f'{curse_dir}/галочка')
            os.mkdir(f'{curse_dir}/цифра')

        # счетчики
        image = 1

        for form in os.listdir(curse_path):
            # счетчики
            text_counter = 1
            check_counter = 1
            number_counter = 1

            # перебор изображений
            form_img = os.fsdecode(form)
            img_path = f"{form_path}/{fac_num}/{curs_num}/{form_img}"

            # сохранение в зависимости от страницы анкеты
            if image % 2 == 1:
                form_page_1 = Image.open(img_path)

                outside = form_page_1.crop((0, 0, 840, 1170))
                outside.save(f'{curse_dir}/текст/{fac_num}_{curs_num}_{image}_{text_counter}.jpg', quality=95)
                text_counter += 1

                outside = form_page_1.crop((1445, 1195, 1545, 1730))
                outside.save(f'{curse_dir}/текст/{fac_num}_{curs_num}_{image}_{text_counter}.jpg', quality=95)
                text_counter += 1

                outside = form_page_1.crop((840, 45, 1590, 1170))
                outside.save(f'{curse_dir}/галочка/{fac_num}_{curs_num}_{image}_{check_counter}.jpg', quality=95)
                check_counter += 1

                outside = form_page_1.crop((145, 1230, 755, 2280))
                outside.save(f'{curse_dir}/цифра/{fac_num}_{curs_num}_{image}_{number_counter}.jpg', quality=95)
                check_counter += 1

            elif image % 2 == 0:

                form_page_2 = Image.open(img_path)

                outside = form_page_2.crop((80, 10, 310, 1120))
                outside.save(f'{curse_dir}/текст/{fac_num}_{curs_num}_{image}_{text_counter}.jpg', quality=95)
                text_counter += 1

                outside = form_page_2.crop((615, 10, 960, 1120))
                outside.save(f'{curse_dir}/текст/{fac_num}_{curs_num}_{image}_{text_counter}.jpg', quality=95)
                text_counter += 1

                outside = form_page_2.crop((1065, 10, 1220, 1120))
                outside.save(f'{curse_dir}/текст/{fac_num}_{curs_num}_{image}_{text_counter}.jpg', quality=95)
                text_counter += 1

                outside = form_page_2.crop((1105, 1215, 1355, 2280))
                outside.save(f'{curse_dir}/текст/{fac_num}_{curs_num}_{image}_{text_counter}.jpg', quality=95)
                text_counter += 1

                outside = form_page_2.crop((1360, 1215, 1650, 2280))
                outside.save(f'{curse_dir}/текст/{fac_num}_{curs_num}_{image}_{text_counter}.jpg', quality=95)
                text_counter += 1

                outside = form_page_2.crop((310, 10, 615, 1120))
                outside.save(f'{curse_dir}/галочка/{fac_num}_{curs_num}_{image}_{check_counter}.jpg', quality=95)
                check_counter += 1

                outside = form_page_2.crop((960, 10, 1065, 1120))
                outside.save(f'{curse_dir}/галочка/{fac_num}_{curs_num}_{image}_{check_counter}.jpg', quality=95)
                check_counter += 1

                outside = form_page_2.crop((1220, 365, 1550, 1120))
                outside.save(f'{curse_dir}/галочка/{fac_num}_{curs_num}_{image}_{check_counter}.jpg', quality=95)
                check_counter += 1

                outside = form_page_2.crop((90, 1215, 1105, 2280))
                outside.save(f'{curse_dir}/цифра/{fac_num}_{curs_num}_{image}_{number_counter}.jpg', quality=95)
                check_counter += 1

            image += 1
        print(f"{fac_num}; {curs_num}\nготов\n\n----------------------")
