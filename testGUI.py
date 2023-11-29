# подключаем библиотеки
import asyncio
from bleak import BleakClient
import PySimpleGUI as sg
import random
# обрабатываем нажатие на кнопку

address = "E4:E1:12:53:E7:93"
CHARACTERISTIC_UUID = "f0001111-4202-cd8d-eb11-3386a69ec3e6"

maxButton = 36
maxButtonActive = 10

def get_action(temp):
    return {
               temp == 0: 'o',
         1 <= temp < 20:   'a',
         20 <= temp < 40:  'b',
         40 <= temp < 60:  'c',
         60 <= temp < 80:  'd',
         80 <= temp < 100: 'e'
    }[True]

async def start_read():
    async with BleakClient(address) as client:
        print(client.is_connected)
        while (True):
            value = bytes(await client.read_gatt_char(CHARACTERISTIC_UUID))
            print(value)


def update():
    #asyncio.run(start_read())
    # получаем новое случайное числа
    listNum = []
    #numbers = ''
    for i in range(maxButton):
        listNum.append(random.randint(0,100-1))
        #numbers += str(listNum[i]) + " "
    listElem = [window['-1-'], window['-2-'], window['-3-'], window['-4-'],
                
                window['-5-'], window['-6-'], window['-7-'], window['-8-'],
                window['-9-'], window['-10-'], window['-11-'], window['-12-'],
                window['-13-'], window['-14-'], window['-15-'], window['-16-'],
                window['-17-'], window['-18-'], window['-19-'], window['-20-'],
                window['-21-'], window['-22-'], window['-23-'], window['-24-'],
                window['-25-'], window['-26-'], window['-27-'], window['-28-'],
                window['-29-'], window['-30-'], window['-31-'], window['-32-'],
                window['-33-'], window['-34-'], window['-35-'], window['-36-']]
                
    for i in range(maxButton):
        code_action = get_action(listNum[i])
        if(code_action == 'a'):
            listElem[i].update(filename=f'im/{i+1}a.png')
        elif(code_action == 'b'):
            listElem[i].update(filename=f'im/{i+1}b.png')
        elif(code_action == 'c'):
            listElem[i].update(filename=f'im/{i+1}c.png')
        elif(code_action == 'd'):
            listElem[i].update(filename=f'im/{i+1}d.png')
        elif(code_action == 'e'):
            listElem[i].update(filename=f'im/{i+1}e.png')
        elif(code_action == 'o'):
            listElem[i].update(filename=f'im/{i+1}.png')

    

# что будет внутри окна
# первым описываем кнопку и сразу указываем размер шрифта
layout = [[sg.Button('Новое числа',enable_events=True, key='-GET_RANDOM_NUMBERS-', font='Helvetica 8')],
        [sg.Image(filename="im/1.png", key='-1-'), sg.Image(filename="im/2.png", key='-2-'),
         sg.Image(filename="im/3.png", key='-3-'), sg.Image(filename="im/4.png", key='-4-'),
         sg.Image(filename="im/1sl.png", key='-1sl-'),
         sg.Image(filename="im/19.png", key='-19-'), sg.Image(filename="im/20.png", key='-20-'),
         sg.Image(filename="im/21.png", key='-21-'), sg.Image(filename="im/22.png", key='-22-')],

         [sg.Image(filename="im/5.png", key='-5-'), sg.Image(filename="im/6.png", key='-6-'),
         sg.Image(filename="im/7.png", key='-7-'), sg.Image(filename="im/8.png", key='-8-'),
         sg.Image(filename="im/2sl.png", key='-2sl-'),
         sg.Image(filename="im/23.png", key='-23-'), sg.Image(filename="im/24.png", key='-24-'),
         sg.Image(filename="im/25.png", key='-25-'), sg.Image(filename="im/26.png", key='-26-'),],

         [sg.Image(filename="im/9.png", key='-9-'), sg.Image(filename="im/10.png", key='-10-'),
         sg.Image(filename="im/11.png", key='-11-'),
         sg.Image(filename="im/3sl.png", key='-3sl-'),
         sg.Image(filename="im/27.png", key='-27-'), sg.Image(filename="im/28.png", key='-28-'),
         sg.Image(filename="im/29.png", key='-29-'),],

         [sg.Image(filename="im/12.png", key='-12-'), sg.Image(filename="im/13.png", key='-13-'),
         sg.Image(filename="im/14.png", key='-14-'),
         sg.Image(filename="im/4sl.png", key='-4sl-'),
         sg.Image(filename="im/30.png", key='-30-'), sg.Image(filename="im/31.png", key='-31-'),
         sg.Image(filename="im/32.png", key='-32-'),],

         [sg.Image(filename="im/15.png", key='-15-'), sg.Image(filename="im/16.png", key='-16-'),
          sg.Image(filename="im/5sl.png", key='-5sl-'),
          sg.Image(filename="im/33.png", key='-33-'), sg.Image(filename="im/34.png", key='-34-'),],

         [sg.Image(filename="im/17.png", key='-17-'), sg.Image(filename="im/18.png", key='-18-'),
          sg.Image(filename="im/6sl.png", key='-6sl-'),
          sg.Image(filename="im/35.png", key='-35-'), sg.Image(filename="im/36.png", key='-36-'),]
        ]

# рисуем окно
window = sg.Window('test', layout, background_color='#FFFFFF',resizable=True)
# запускаем основной бесконечный цикл
while True:
    # получаем события, произошедшие в окне
    event, values = window.read()
    # если нажали на крестик
    if event in (sg.WIN_CLOSED, 'Exit'):
        # выходим из цикла
        break
    # если нажали на кнопку
    if event == '-GET_RANDOM_NUMBERS-':
        # запускаем связанную функцию
        update()

# закрываем окно и освобождаем используемые ресурсы
window.close()