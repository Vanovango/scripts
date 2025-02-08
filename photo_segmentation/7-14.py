import os

from PIL import Image

fac = 'СПО'
curs = "24с_курс"

# путь до папки с анкетами
form_path = f"C:/Users/voyte/Desktop/Рабочка/Технопарк/Статистика анкет по СР/JPG_ancets/{fac}/{curs}"

# save_dir = f"Анкеты_разделенные_7-14/{fac}/{curs}"

if not os.path.isdir(curs):
    os.mkdir(f'./{curs}')

for image in os.listdir(form_path):
    # print(image, image[-5])
    image_number = int([i for i in image.split('_')][0])

    img_path = form_path + "/" + image

    form_1 = Image.open(img_path)

    outside = form_1.crop((840, 38, 1633, 1130))
    outside.save(f'{curs + "/" + image[:-5]}.jpg', quality=95)

    # elif int(image[-5]) == 2:
    #     form_2 = Image.open(img_path)
    #
    #     outside = form_2.crop((20, 1212, 760, 2298))
    #     outside.save(f'{curs + "/" + image[:-5]}.jpg', quality=95)


# if image_number not in [2, 51, 52]:
#     if int(image[-5]) == 1:
#         form_1 = Image.open(img_path)
#
#         if image_number in [12, 23, 47, 48, 49]:
#             outside = form_1.crop((20, 1212, 790, 2298))
#             outside.save(f'{curs + "/" + image[:-5]}.jpg', quality=95)
#         else:
#             outside = form_1.crop((840, 38, 1633, 1130))
#             outside.save(f'{curs + "/" + image[:-5]}.jpg', quality=95)
#
# elif int(image[-5]) == 2:
#     form_2 = Image.open(img_path)
#
#     outside = form_2.crop((20, 1212, 790, 2298))
#     outside.save(f'{curs + "/" + image[:-5]}.jpg', quality=95)

# 11 курс
# ((1 <= image_number <= 50) or (80 <= image_number <= 109))
# form_1.crop((840, 38, 1633, 1130))
# ((51 <= image_number <= 79) or (110 <= image_number <= 127))
# form_2.crop((20, 1212, 760, 2298))

# 12, 13, 14, 21, 22, 23, 24, 33 курс
# все норм
# crop((840, 20, 1633, 1150))

# 31 курс
# [2, 12, 23, 47, 48, 49, 51, 52]
# 12, 23, 47, 48, 49 - 1 страница, но снизу

# 32 курс
# 26 анкета - 2

# 34 курс
# 113 анкета - 2


