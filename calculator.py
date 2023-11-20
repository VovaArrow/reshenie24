from tkinter import *
from tkinter import ttk
 
 
root = Tk()
root.title("ООО Решение")
root.geometry("470x340+300+250")
root.resizable(False, False)
try:
    root.iconbitmap(default="Z:\soft\logo.ico")
except:
    pass

# Словари и списки цен и материалов
mat_price = {'АКП 3мм': 2700, 'ПВХ 3мм': 1000, 'ПВХ 5мм': 1700, 'ПВХ 8мм':2850, 'Акрил(мол)3мм': 2700, 'Акрил(мол)5мм': 4600, 'Акрил(пр)3мм': 2350, 'Акрил(пр)5мм': 4000}
mat_choise = ['АКП 3мм', 'ПВХ 3мм', 'ПВХ 5мм', 'ПВХ 8мм','Акрил(мол)3мм','Акрил(мол)5мм', 'Акрил(пр)3мм', 'Акрил(пр)5мм']

UV_price =  {'Печать(ШИР)': 0, 'УФ-печать': 1700, 'Шрифт Брайля': 13500}
UV_choise = ['Печать(ШИР)', 'Печать(ИНТ)', 'УФ-печать', 'Шрифт Брайля', 'Пенопласт']

ban_price = {'340 г/м2': 350, '440 г/м2': 400, '510 г/м2': 450}
ban_choise = ['340 г/м2', '440 г/м2', '510 г/м2']

int_prise = {'Oracal 641': 550, 'OraJet': 550, 'Холст': 1000, 'Баннер': 450}
int_choise = ['Oracal 641', 'OraJet', 'Холст', 'Баннер']

# Переменные
answer = 0
k = 1

# Функция расчета УФ-печати и Брайля
def calculate():
    a = mat_price[material.get()]
    b = UV_price[UV.get()]
    c = it_number.get()
    S = (int(it_width.get()) * int(it_height.get())) / 1000000
        
    if S < 1:
        k = 1 + (1 - S)

    else:
        k = 1     
            

    answer = (a + b) * S * k + (freza.get() * 350 * S) + (tape.get() * 200 * S) 
        
    it_answer['text'] = round(answer * int(it_number.get()) + mak.get() * 1500)
    it_per_num['text'] = round(answer)

# Функция расчета Широкоформатной печати
def calculate_ban():

    a = int(it_width.get()) / 1000
    b = int(it_height.get()) / 1000
    c = 0
    S = (int(it_width.get()) * int(it_height.get())) / 1000000
        
    # Считаем перерасход

    if a%3 == 0 or b%3 ==0:
        c = 0
    elif a < 3 and b < 3:
        c = round(3 * min(a, b) - (a*b), 1) 
    else:
        x = ((3-(b%3)) * a)
        y = ((3-(a%3)) * b)
        c = round(min(x, y), 1)

    it_per_num['text'] = round((S * ban_price[material.get()]) + (((a+b) * 2) // 0.3 + 1) * freza.get() * 35 + (tape.get() * 200 * c ))
    it_answer['text'] = it_per_num['text'] * int(it_number.get()) + (mak.get() * 1500)   

# Обработка события выбора функций    
def selected(event):
    it_num['text'] = 'Количество'
    
    it_width.delete(0, END)
    it_height.delete(0, END)
    it_number.delete(0, END)

    it_width.insert(0, 0)
    it_height.insert(0, 0)
    it_number.insert(0, 1)

    it_answer['text'] = 0
    it_per_num['text'] = 0

    if UV.get() == 'Печать(ШИР)':
        
        material['values'] = ban_choise
        material.set('510 г/м2')
        it_tape['text'] = 'Перерасход'
        it_freza['text'] = 'Люверсы'
        it_calc['command'] = calculate_ban
    
    elif UV.get() == 'УФ-печать' or UV.get() == 'Шрифт Брайля':
        
        material['values'] = mat_choise
        material.set('АКП 3мм')
        it_tape['text'] = 'Скотч'
        it_freza['text'] = 'Фрезеровка'
        it_calc['command'] = calculate

    elif  UV.get() == 'Пенопласт':

        material['values'] = ['Пенопласт']
        material.set('Пенопласт')
        it_tape['text'] = 'Упаковка'
        it_freza['text'] = 'Покраска'
        it_calc['command'] = calculate_penoplast
        it_num['text'] = 'Глубина мм'

    elif UV.get() == 'Печать(ИНТ)':
        material['values'] = ['Oracal 641', 'OraJet', 'Холст', 'Баннер']
        material.set('Oracal 641')
        it_tape['text'] = 'Резка'
        it_freza['text'] = 'Ламинация'
        it_calc['command'] = calculate_int

# Функция расчета пенопласта
def calculate_penoplast():

    a = int(it_width.get()) / 1000
    b = a
    c = int(it_number.get()) / 1000
    V = a * b * c 
    it_answer['text'] = round(V * 9000 + (freza.get() * 7500 * V) + (tape.get() * 1000 * V)) + mak.get()*2500
    it_per_num['text'] = round(it_answer['text']) - mak.get()*2500 

# Функция расчета интерьерной печати
def calculate_int():
    a = int(it_width.get()) / 1000
    b = int(it_height.get()) / 1000
    S = a * b
    
    
    it_per_num['text'] = round(int_prise[material.get()] * S + (tape.get() * 300 * S) + (freza.get() * 500 * S))
    it_answer['text'] = it_per_num['text'] * int(it_number.get()) + mak.get() * 1500

notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)


# Лейблы с текстом
it_wh = ttk.Label(frame1, text='Размеры мм', font=('Comic Sans MS', 15))
it_wh.place(relwidth=0.3, x=30, y=30)

it_material = ttk.Label(frame1, text='Технология', font=('Comic Sans MS', 15))
it_material.place(relwidth=0.3, x=170, y=30)

it_UV = ttk.Label(frame1, text='Материал', font=('Comic Sans MS', 15))
it_UV.place(relwidth=0.25, x=320, y=30)

it_num = ttk.Label(frame1, text='Количество', font=('Comic Sans MS', 15))
it_num.place(relwidth=0.3, x=30, y=130)

per_num = ttk.Label(frame1, text='Цена за Шт', font=('Comic Sans MS', 13))
per_num.place(relwidth=0.3, x=30, y=190)



# Поля ввода Размеры
it_width = ttk.Entry(frame1, font=('Comic Sans MS', 12))
it_width.place(relwidth=0.23, x=30, y=70)

it_height = ttk.Entry(frame1, font=('Comic Sans MS', 12))
it_height.place(relwidth=0.23, x=30, y=100)

# Поле ввода Количество
it_number = ttk.Entry(frame1, font=('Comic Sans MS', 12))
it_number.place(relwidth=0.2, x=30, y=160)

# Выбор материала и печати
material = ttk.Combobox(frame1, font=('Comic Sans MS', 12), values=mat_choise)
material.place(relwidth=0.3, x=320, y=70)
material.insert(0, 'АКП 3мм')

UV = ttk.Combobox(frame1, font=('Comic Sans MS', 12), values=UV_choise)
UV.place(relwidth=0.3, x=165, y=70)
UV.insert(0, 'УФ-печать')
UV.bind("<<ComboboxSelected>>", selected)

# Кнопка рассчитать
it_calc = ttk.Button(frame1, text='Рассчитать', padding=15, command=calculate)
it_calc.place(x=180, y=220)


#Галочка скотч
tape = IntVar()
it_tape = ttk.Checkbutton(frame1, text='Скотч', variable=tape, onvalue=1)
it_tape.place(x=320, y=160)


#Галочка Фрезеровка
freza = IntVar()
it_freza = ttk.Checkbutton(frame1, text='Фрезеровка', variable=freza, onvalue=1)
it_freza.place(x=320, y=130)

#Галочка макет
mak = IntVar()
it_maket = ttk.Checkbutton(frame1, text='Макет', variable=mak, onvalue=1)
it_maket.place(x=320, y=190)

# Стоимость
it_answer = ttk.Label(frame1, text='0', font=('Comic Sans MS', 22), foreground='#F0FFF0', background='#2F4F4F', padding=10)
it_answer.pack(expand=1)

it_per_num = ttk.Label(frame1, text='0', font=('Comic Sans MS', 15), background='#5F9EA0')
it_per_num.place(x=30, y=230)

# Вставка по умолчанию
it_width.insert(0, 0)
it_height.insert(0, 0)
it_number.insert(0, 1)

frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)


notebook.add(frame1, text='Калькулятор')
notebook.add(frame2, text='Листы материала')


root.mainloop()
    
