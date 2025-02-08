from subprocess import Popen

path_to_apps = {'Telegram': "C:/Users/voyte/AppData/Roaming/Telegram Desktop/Telegram.exe",
                'Music': "C:/Users/voyte/AppData/Local/Programs/YandexMusic/Яндекс Музыка.exe",
                'Browser': "C:/Users/voyte/AppData/Local/Yandex/YandexBrowser/Application/browser.exe",
                'PyCharm': "C:/Code/PyCharm 2023.1.3/PyCharm Community Edition 2023.1.3/bin/pycharm64.exe"}


try:
    for app_name in path_to_apps.keys():
        Popen(path_to_apps[app_name])

except NameError:
    print("Ошибка запуска приложений, проверьте корректность имени файла")
