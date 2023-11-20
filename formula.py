from math import ceil
import tkinter as tk
import customtkinter as ct

ct.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ct.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = ct.CTk()
root.title('Раскладка деталей')
root.geometry('900x550')
root.resizable(False, False)

canvas = tk.Canvas(root, bg="grey")
canvas.place(x=10, y=135, width=800, height=300)


def draw():
    
    width = int(entry_width.get()) / 5
    height = int(entry_height.get()) / 5
    num = int(entry_numbers.get())
    
    canvas.delete('all')
    
    flag = 0
    
    x = 800
    y = 300

    a, b, c, d = 2, 2 , width , height 

    while d < y and flag < num:
        if c < x and d < y:
            canvas.create_rectangle(a, b, c, d, fill="#A00000", outline='white')
            a += width + 2
            c += width + 2
            flag += 1
        else:
            d += height + 2
            b += height + 2
            a = 2
            c = width
    print(c, d)         
               
    lbl_flag.configure(text=flag)  
    lbl_num_list.configure(text=abs(-num//flag)) 
    remainder.configure(text=round(abs(-num//flag)-num / flag, 2))  

def reverse():
    
    width = int(entry_height.get()) / 5
    height = int(entry_width.get()) / 5
    num = int(entry_numbers.get())
    
    canvas.delete('all')
    
    flag = 0
    
    x = 800
    y = 300

    a, b, c, d = 2, 2 , width , height 

    while c < x and flag < num:
        if c < x and d < y:
            canvas.create_rectangle(a, b, c, d, fill="#A00000", outline='white')
            b += height + 2
            d += height + 2
            flag += 1
        else:
            a += width + 2
            c += width + 2
            b = 2
            d = height
    print(a, b) 

    lbl_flag.configure(text=flag)            
    lbl_num_list.configure(text=abs(-num//flag))  
    remainder.configure(text=round(abs(-num//flag)-num / flag, 2)) 

def package():
    
    height = int(entry_height.get()) / 5
    width = int(entry_width.get()) / 5
    num = int(entry_numbers.get())
    
    canvas.delete('all')
    
    flag = 0
    
    
    x = 800
    y = 300

    a, b, c, d = 2, 2 , width , height 

    while c < x and flag < num:
        if c < x and d < y:
            canvas.create_rectangle(a, b, c, d, fill="#A00000", outline='white')
            b += height + 2
            d += height + 2
            flag += 1
        else:
            a += width + 2
            c += width + 2
            b = 2
            d = height
    print(c, d)        
         
          
    lbl_flag.configure(text=flag)
    lbl_num_list.configure(text=abs(-num//flag))
    remainder.configure(text=str(int((800-c)*5))+'\nX\n1500')  
    
    
def selected(event):
    if choice.get() == 'АКП 4*1,5':
        lbl_flag.configure(text='TT') 

    elif choice.get() == 'ПВХ 3*2':
        lbl_flag.configure(text=f'YY') 


         
entry_width = ct.CTkEntry(root, width=90)
entry_height = ct.CTkEntry(root, width=90)
entry_numbers = ct.CTkEntry(root, width=90)
entry_width.place(x=15, y=40)
entry_height.place(x=15, y=75) 
entry_numbers.place(x=110, y=40)   


btn = ct.CTkButton(root, text='Разложить', command=draw, width=90)
btn.place(x=320, y=40)

btn_change = ct.CTkButton(root, text='Повернуть', command=reverse, width=90)
btn_change.place(x=415, y=40)

btn_change = ct.CTkButton(root, text='Упаковать', command=package, width=90)
btn_change.place(x=320, y=75)

entry_width.insert(0, 350)
entry_height.insert(0, 150)
entry_numbers.insert(0, 10)

lbl_size = ct.CTkLabel(root, text='Размеры', font=ct.CTkFont(size=12, weight="bold")) 
lbl_size.place(x=25,y=10)

lbl_quantity = ct.CTkLabel(root, text='Количество', font=ct.CTkFont(size=12, weight="bold")) 
lbl_quantity.place(x=115,y=10)

lbl_material = ct.CTkLabel(root, text='Материал', font=ct.CTkFont(size=12, weight="bold")) 
lbl_material.place(x=220,y=10)

lbl_flag = ct.CTkLabel(root, text='', text_color='#4671D5', font=ct.CTkFont(size=42, weight="bold", )) 
lbl_flag.place(x=515,y=55)

lbl_list = ct.CTkLabel(root, text='Кол-во листов', font=ct.CTkFont(size=12, weight="bold", )) 
lbl_list.place(x=640,y=10)

lbl_num_list = ct.CTkLabel(root, text='', text_color='#FF0000', font=ct.CTkFont(size=42, weight="bold", )) 
lbl_num_list.place(x=640,y=55)

lbl_num_of = ct.CTkLabel(root, text="Деталей на лист", font=ct.CTkFont(size=12, weight="bold"))
lbl_num_of.place(x=515, y=10)

lbl_remainder = ct.CTkLabel(root, text='Остаток материала', font=ct.CTkFont(size=12, weight="bold", )) 
lbl_remainder.place(x=750,y=10)

remainder = ct.CTkLabel(root, text='', text_color='#3AE73A', font=ct.CTkFont(size=24, weight="bold", ))
remainder.place(x=780, y=35)

choice = ct.CTkComboBox(root, values=['АКП 4*1,5', 'ПВХ 3*2'], width=110)
choice.place(x=205, y=40)
choice.bind("<<ComboboxSelected>>", selected)








root.mainloop()