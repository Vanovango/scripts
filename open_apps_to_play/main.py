# python -m auto_py_to_exe
# go this command to create exe file

from subprocess import Popen

path_to_apps = {'Telegram': "C:/Users/voyte/AppData/Roaming/Telegram Desktop/Telegram.exe",
                'Music': "C:/Users/voyte/AppData/Local/Programs/YandexMusic/Яндекс Музыка.exe",
                'Steam': "D:/Steam/steam.exe"}


try:
    for app_name in path_to_apps.keys():
        Popen(path_to_apps[app_name])

except NameError:
    print("Ошибка запуска приложений, проверьте корректность имени файла")
