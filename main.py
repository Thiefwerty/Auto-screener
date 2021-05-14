import win32gui
import time
from PIL import ImageGrab
print("Данная программа разработана на основе Open Source и предназначена для некоммерческого использования")
print("Depeloped by Mikhail Andronov")
print("GitHub: https://github.com/Thiefwerty")
print()
print()
print()
print("Введите путь сохранения файлов в формате: C:\\name\\ и нажмите Enter")
s = input()
print("Введите коэффицент масштабирования (если 100% введите 1, если 125% введите 1.25 и т.д)")
k = float(input())
print("Переместите курсор в левый верхний угол области скрининга и нажмите Enter")
flag = input()
x1, y1 = win32gui.GetCursorPos()
print("Переместите курсор в правый нижний угол области скрининга и нажмите Enter")
flag = input()
x2, y2 = win32gui.GetCursorPos()
print("Программа работает, для завершения раобты программы закройте данное окно")
print("Перед следующим запуском не забудьте перенести сохраненные файлы, иначе они будут перезаписаны")
screensize = ImageGrab.grab(bbox = (x1 * k, y1 * k, x2 * k, y2 * k)).size
original = ImageGrab.grab(bbox = (x1 * k, y1 * k, x2 * k, y2 * k))
a = 1
while True:
    cnt = 0
    matched = ImageGrab.grab(bbox = (x1 * k, y1 * k, x2 * k, y2 * k))
    for i in range (0, screensize[0]):
        for j in range (0, screensize[1]):
            if matched.getpixel((i, j)) != original.getpixel((i, j)):
                cnt += 1
    if cnt >= ((screensize[0] * screensize[1]) / 5):    
        original.save(s + str(a) + '.png')
        a += 1
        original = ImageGrab.grab(bbox = (x1 * k, y1 * k, x2 * k, y2 * k))
    time.sleep(5)
