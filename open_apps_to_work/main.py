from subprocess import Popen

path_to_apps = {'Telegram': "C:/Users/voyte/AppData/Roaming/Telegram Desktop/Telegram.exe",
                'Music': "C:/Users/voyte/AppData/Local/Programs/YandexMusic/Яндекс Музыка.exe",
                'Browser': "C:/Users/voyte/AppData/Local/Yandex/YandexBrowser/Application/browser.exe",
                'PyCharm': "C:/Code/PyCharm 2023.1.3/PyCharm Community Edition 2023.1.3/bin/pycharm64.exe"}


try:
    Popen(path_to_apps['Telegram'])
    Popen(path_to_apps['Music'])
    Popen(path_to_apps['Browser'])
    Popen(path_to_apps['PyCharm'])


except NameError:
    print("Ошибка запуска приложений, проверьте корректность пути")
