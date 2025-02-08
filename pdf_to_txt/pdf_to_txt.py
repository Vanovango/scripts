from PIL import Image
import pytesseract

# Чтение и предварительная обработка изображения
image = Image.open('./test_1.jpg')
gray = image.convert('L')  # Преобразование в grayscale
threshold = 127
binary_image = gray.point(lambda x: 0 if x < threshold else 255, '1')

# Извлечение текста с использованием pytesseract
# Установка пути к tesseract (если необходимо)
# Укажите путь к вашему tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # !!!!!!!!!!!!!!!!
lang = 'rus'  # Русский язык
text = pytesseract.image_to_string(binary_image, lang=lang)

# Вывод извлеченного текста
print(text)

# Сохранение извлеченного текста в файл
with open("recognized_text.txt", "w") as file:
    file.write(text)
