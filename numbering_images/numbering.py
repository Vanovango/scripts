from PIL import Image, ImageDraw


def image_1_dir():
    img_path = "./images/1"
    save_path = "./numbering/1"
    number_of_images = 10

    for img_number in range(1, number_of_images + 1):
        image = Image.open(f'{img_path}/{img_number}.png')

        # get a drawing context
        text = ImageDraw.Draw(image)
        # draw text, full opacity
        text.text((300, image.size[1] - 120), '1', font_size=100, fill=(33, 68, 245, 255))

        # save changed image
        image.save(f'{save_path}/{img_number}.png', quality=95)


def image_2_dir():
    img_path = "./images/2"
    save_path = "./numbering/2"
    number_of_images = 10

    for img_number in range(1, number_of_images + 1):
        image = Image.open(f'{img_path}/{img_number}.png')

        # get a drawing context
        text = ImageDraw.Draw(image)
        # draw text, full opacity
        text.text((image.size[0] - 120, image.size[1] - 120), '2', font_size=100, fill=(33, 68, 245, 255))

        # save changed image
        image.save(f'{save_path}/{img_number}.png', quality=95)


if __name__ == "__main__":
    image_1_dir()
    image_2_dir()
