from PIL import Image


size = (2438, 1895)

for i in range(1, 520 + 1):
    if i % 10 == 0:
        print(i)
    tmp = str(i).zfill(3)

    im = Image.open(f'./images/Книга_105_Страница_{tmp}.jpg')
    im.thumbnail(size, Image.Resampling.LANCZOS)
    im_crop_outside = im.crop((75, 75, 2_388, 1_845))
    im_crop_outside.save(f'./книга/Книга_105_Страница_{tmp}.jpg', quality=95)
