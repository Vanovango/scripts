from PIL import Image


def for_all_images():
    for i in range(1, 520 + 1):
        if i % 10 == 0:
            print(i)
        tmp = str(i).zfill(3)

        im = Image.open(f'./images/Книга_105_Страница_{tmp}.jpg')

        width, height = im.size
        im_crop_outside = im.crop((65, 65, width - 65, height - 65))
        im_crop_outside.save(f'./книга/Книга_105_Страница_{tmp}.jpg', quality=95)


def test():
    im = Image.open(f'./images/Книга_105_Страница_019.jpg')

    width, height = im.size
    im_crop_outside = im.crop((65, 65, width - 65, height - 65))
    im_crop_outside.save(f'./книга/Книга_105_Страница_019.jpg', quality=95)


if __name__ == "__main__":
    for_all_images()
    # test()
