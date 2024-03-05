from tkinter import *
import random
import time


game_account = 5  # счёт игрока
victory_cnt = 0   # счетчик побед
loss_cnt = 0      # счетчик проигрышей

orel = 'orel.png'
reska = 'reska.png'

  
def povorot(event):#  ф-ция изуализации крутящейся монеты
    global b1
    for i in range(30):
        b1 = PhotoImage(file=(random.choice(['orel.png','reska.png','imag.png',
                                             'orel2.png','reska2.png'])))
        label_coin["image"] = b1
        root.update()
        time.sleep(0.05)

def brosok(event):     # ф-ция броска монеты
    global game_account
    global victory_cnt
    global loss_cnt
    global rand
    x = random.choice(['orel.png','reska.png'])
    rand = PhotoImage(file=(x))
    label_coin["image"] = rand
    root.update()
    if event == x:
        game_account = game_account+2
        victory_cnt = victory_cnt + 1
        label_victory["text"] = f"ПОБЕД: {victory_cnt}"      
        label_chek["text"] = f"СЧЁТ ИГРОКА: {game_account} руб."        
    elif event != x:
        loss_cnt = loss_cnt + 1
        label_loss["text"] = text=f"ПОРАЖЕНИЙ: {loss_cnt}"
   
        
    
def choice_reska():   # ф-ция вывода "решка"
    global game_account    
    """<1>"""
    povorot('')
    game_account = game_account-1
    label_chek["text"] = f"СЧЁТ ИГРОКА: {game_account} руб."
    return brosok(reska), game_account

def choice_orel():    # ф-ция вывода "орёл"
    global game_account
    """<1>"""
    povorot('')
    game_account = game_account-1
    label_chek["text"] = f"СЧЁТ ИГРОКА: {game_account} руб. "
    return brosok(orel), game_account


    
root = Tk()
root.geometry("500x400")
root.title("ИГРА В ОРЛЯНКУ")
root.resizable(height=False, width=False) 
root.iconphoto(True, PhotoImage(file=('ikon.png')))


## МЕТКА СЧЁТ ИГРОКА:
label_chek = Label(text=f"СЧЁТ ИГРОКА: {game_account} руб. ",
                foreground="#FF0000",  # Устанавливает цвет текста
                background="yellow",   # Устанавливает цвет фона
                width=40,height=2,     # ширина и высота
                relief=FLAT,           # тип рельефа
                borderwidth=7)         # ширина рамки
label_chek.grid(row=0,column=1,  padx=1, pady=1, sticky="nw")


## МЕТКА МОНЕТЫ:
image_coin = PhotoImage(file=('imag.png'))
label_coin = Label(image=image_coin,
                background="white",    # Устанавливает цвет фона
                width=330,height=300)    # ширина и высота
label_coin.place(x=140, y=60)

## РАМКИ ПОБЕД И ПОРАЖЕНИЙ:
frame_victory = Frame(master=root, relief=GROOVE, borderwidth=4)
frame_loss = Frame(master=root, relief=GROOVE, borderwidth=4)

frame_victory.grid(row=0, column=0, padx=0, pady=3) # координаты рамки побед
frame_loss.grid(row=1, column=0, padx=1, pady=3) # координаты рамки поражений

## МЕТКА ПОД РАМКУ ПОБЕД:
label_victory = Label(master=frame_victory, text=f"ПОБЕД: {victory_cnt}",
                      foreground="black",   # Устанавливает цвет текста
                      background="#00FF27", # Устанавливает цвет фона
                      width=15,height=2)    # ширина и высота
label_victory.grid(row=0, column=0, padx=0, pady=1) # координаты метки побед

## МЕТКА ПОД РАМКУ ПОРАЖЕНИЙ:
label_loss = Label(master=frame_loss, text=f"ПОРАЖЕНИЙ: {loss_cnt}",
                      foreground="black",   # Устанавливает цвет текста
                      background="#00FF27", # Устанавливает цвет фона
                      width=15,height=2)    # ширина и высота
label_loss.grid(row=2, column=0, padx=1, pady=1) # координаты метки поражений

## КНОПКА ОРЁЛ:
button1 = Button(text="ОРЁЛ!", height=2, width= 10, # текст кнопки, высота, ширина
                 bg="#00FFF8",fg="#0015FA",   # цвет текста и фона кнопки
                 relief=RAISED, borderwidth=9,  # рельеф и ширина рамки
                 command=choice_orel)  # команда при нажатии - запуск функции
button1.place(x=15, y=130)  # координаты размещения кнопки

## КНОПКА РЕШКА:
button2 = Button(text="РЕШКА!", height=2,width = 10, # текст кнопки, высота, ширина
                 bg="#00FFF8",fg="#0015FA",   # цвет текста и фона кнопки
                 relief=RAISED, borderwidth=9,  # рельеф и ширина рамки
                 command=choice_reska)  # команда при нажатии - запуск функции
button2.place(x=15, y=220) # координаты размещения кнопки
## альтернативный варинт запуска функций кнопками (вместо command):
##button1.bind("<1>", povorot)  # связывает событие нажатия ЛКМ с choice_orel()    
##button2.bind("<1>", povorot) # связывает событие нажатия ЛКМ с choice_reska()

root.mainloop()
