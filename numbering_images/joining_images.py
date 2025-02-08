from PIL import Image, ImageDraw


img_path_1 = "./images/1"
img_path_2 = "./images/2"
save_path = "./concatenate"
number_of_images = 10

for img_number in range(1, number_of_images + 1):
    # opening up of images
    img1 = Image.open(f"{img_path_1}/{img_number}.png")
    img2 = Image.open(f"{img_path_2}/{img_number}.png")

    # changed images size
    img1_size = img1.resize((800, 800))
    img2_size = img2.resize((800, 800))

    # creating a new image and pasting the images
    img = Image.new("RGB", (1600, 800), "white")

    # pasting images (image_name, (position))
    img.paste(img1_size, (0, 0))
    img.paste(img2_size, (800, 0))

    # get a drawing context
    text = ImageDraw.Draw(img)
    # draw text, full opacity
    text.text((30, img.size[1] - 120), '1', font_size=100, fill=(33, 68, 245, 255))
    text.text((img.size[0] - 120, img.size[1] - 120), '2', font_size=100, fill=(33, 68, 245, 255))

    img.save(f"{save_path}/{img_number}.png")

