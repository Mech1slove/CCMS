import math
import tkinter as tk  # import Test_Link
from tkinter import ttk
from tkinter import filedialog
from tkinter import simpledialog
import sqlite3
import pandas as pd

import Test_Link as Gp
import pandas

"""""
radio_button_select = {
    "Одноступенчатое":1,
    "Двухступенчатое":2
     }
"""""
Napravlenie = []
Konductor = []
Promezutochnaya = []
Osnovnaya = []

Number_gradient = 0

class Item:
    def __init__(self, name, depthdes, depthver, insidediam, columndiam, chiseldiam, stakan, coeftrikery):
        self.Name = name
        self.Depthdes = depthdes
        self.Depthver = depthver
        self.Insidediam = insidediam
        self.Columndiam = columndiam
        self.Chiseldiam = chiseldiam
        self.Stakan = stakan
        self.Coeftrikery = coeftrikery

    def __str__(self):
        return f"{self.Name}: {self.Depthdes}: {self.Depthver}: {self.Insidediam} {self.Columndiam}: {self.Chiseldiam}:{self.Stakan}: {self.Coeftrikery}"


class Fluid:
    def __init__(self, nameF, before, after, density, DNS, comprescoef):
        self.nameF = nameF
        self.before = before
        self.after = after
        self.density = density
        self.DNS = DNS
        self.comprescoef = comprescoef

    def __str__(self):
        return f"{self.nameF}: {self.before}:{self.after}:{self.density}:{self.comprescoef}"

class Gradient:
    def __init__(self, Number, Roof, Sole, Gradient):
        self.Number = Number
        self.Roof = Roof
        self.Sole = Sole
        self.Gradient = Gradient
    def __str__(self):
        return f"{self.Number}: {self.Roof}:{self.Sole}:{self.Gradient}"


def trynotnull(ress):
    try:
        variable = float(ress)
    except ValueError:
        variable = 0
    return variable

def open_popup():
    switch_type_colonn = {
        "Направление": 1,
        "Кондуктор": 2,
        "Промежуточная кол.": 3,
        "Эксплуатационная кол.": 4,
        "Хвостовик": 5
    }

    selected_value = tk.StringVar()

    popup = tk.Toplevel(root, width=100)
    popup.title("Всплывающее окно ")
    popup.geometry("340x330")

    type_combo = ttk.Combobox(popup, textvariable=selected_value, width=20)
    type_combo['value'] = list(switch_type_colonn.keys())
    type_combo.place(x=190, y=0)

    deep_entry = tk.Entry(popup, width=10)
    deep_entry.place(x=190, y=30)
    deep_entry1 = tk.Entry(popup, width=10)
    deep_entry1.place(x=190, y=60)
    diameter_entry = tk.Entry(popup, width=10)
    diameter_entry.place(x=190, y=90)
    diameterinside_entry = tk.Entry(popup, width=10)
    diameterinside_entry.place(x=190, y=120)
    diameter_entry1 = tk.Entry(popup, width=10)
    diameter_entry1.place(x=190, y=150)
    deep_entry2 = tk.Entry(popup, width=10)
    deep_entry2.place(x=184, y=210)
    Coeftrikery_entry = tk.Entry(popup, width=10)
    Coeftrikery_entry.place(x=190, y=250)

    popup_label = tk.Label(popup, text="Тип обсадной колонны")
    popup_label.place(x=30, y=0)
    popup_label1 = tk.Label(popup, text="Глубина спуска(ствол), м")
    popup_label1.place(x=30, y=30)
    popup_label2 = tk.Label(popup, text="Глубина спуска(верт), м")
    popup_label2.place(x=30, y=60)
    popup_label22 = tk.Label(popup, text="Внутренний диаметр, м")
    popup_label22.place(x=30, y=90)
    popup_label3 = tk.Label(popup, text="Наружный диаметр, мм")
    popup_label3.place(x=30, y=120)
    popup_label4 = tk.Label(popup, text="Диаметр долота, мм")
    popup_label4.place(x=30, y=150)
    popup_label5 = tk.Label(popup, text="Тип цементирования")
   # popup_label5.place(x=30, y=180)
    popup_label6 = tk.Label(popup, text="Глубина цем. стакана")
    popup_label6.place(x=130, y=180)
    popup_label7 = tk.Label(popup, text="Коэффициент кавернозности")
    popup_label7.place(x=20, y=250)

    radio_button_level_var = tk.IntVar()

  # tk.Radiobutton(popup, text="Одноступенчатое", variable=radio_button_level_var, value=1, ).place(x=30, y=210)
  # tk.Radiobutton(popup, text="Двухступенчатое", variable=radio_button_level_var, value=2, ).place(x=30, y=230)

    def save_item():
        Name       = type_combo.get()
        Depthdes   = trynotnull(deep_entry.get())
        Depthver   = trynotnull(deep_entry1.get())
        Insidediam = trynotnull(diameterinside_entry.get())
        Dolumndiam = trynotnull(diameter_entry.get())
        Chiseldiam = trynotnull(diameter_entry1.get())
        Stakan     = trynotnull(deep_entry2.get())
        Coeftrikery= trynotnull(Coeftrikery_entry.get())


        item = Item(Name, Depthdes, Depthver, Insidediam, Dolumndiam, Chiseldiam, Stakan, Coeftrikery)
        items.append(item)
        update_table()
        if type_combo.get() == 'Направление':
            global Napravlenie
            Napravlenie = [Name, Depthdes, Depthver, Insidediam, Dolumndiam, Chiseldiam, Stakan, Coeftrikery]
        elif type_combo.get() == 'Кондуктор':
            global Konductor
            Konductor = [Name, Depthdes, Depthver, Insidediam, Dolumndiam, Chiseldiam, Stakan, Coeftrikery]
        elif type_combo.get() == 'Промежуточная кол.':
            global Promezutochnaya
            Promezutochnaya = [Name, Depthdes, Depthver, Insidediam, Dolumndiam, Chiseldiam, Stakan, Coeftrikery]
        elif type_combo.get() == 'Эксплуатационная кол.':
            global Osnovnaya
            Osnovnaya = [Name, Depthdes, Depthver, Insidediam, Dolumndiam, Chiseldiam, Stakan, Coeftrikery]

        popup.destroy()


    save_button = tk.Button(popup,
                            text="Сохранить",
                            command=save_item)
    save_button.place(x=150, y=280)


def find_value(input_value):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    cursor.execute('SELECT Betta FROM Bethans WHERE SenVenanI = ?', (input_value))
    result = cursor.fetchone()

    if result:
        return result[0]
    else:
        print('Что-то не пашет, Лошара')


def get_selected_item_data():
    # получаем выделенную строку
    selected_item = table.selection()
    if selected_item:
        # получаем данные из выбранной строки
        item_name = table.item(selected_item, "values")[0]
        item_quantity = table.item(selected_item, "values")[1]

    else:
        print("ничего не выбранно")


def update_table():
    #   Очищаем таблицу
    for row in table.get_children():
        table.delete(row)
    # Заполняем таблицу данными name,depthdes,depthver,dolumndiam,chiseldiam,stakan,coeftrikery
    for item in items:
        table.insert("", "end", values=(
            item.Name, item.Depthdes, item.Depthver, item.Insidediam, item.Columndiam, item.Chiseldiam, item.Stakan, item.Coeftrikery))


def update_fluid_table():
    # Очищаем таблицу
    for row in table_fluid.get_children():
        table_fluid.delete(row)

    for item_fluid in items_fluid:
        table_fluid.insert("", "end", values=(item_fluid.nameF,
                                              item_fluid.before,
                                              item_fluid.after,
                                              item_fluid.density,
                                              item_fluid.DNS,
                                              item_fluid.comprescoef,))


def update_Gradient_table():
    #   Очищаем таблицу
    for row in GradientTable.get_children():
        GradientTable.delete(row)
    # Заполняем таблицу данными name,depthdes,depthver,dolumndiam,chiseldiam,stakan,coeftrikery
    for item in Gradient_list:
        GradientTable.insert("", "end", values=(
                                                item.Number, item.Roof, item.Sole, item.Gradient))


def fill_combobox():
    valuescm = [table.item(item, "values")[0] for item in table.get_children()]
    column_combobox['values'] = valuescm
    valuescm1 = [table_fluid.item(item, "values")[0] for item in table_fluid.get_children()]
    column_combobox1['values'] = valuescm1
    valuescm2 = [table_fluid.item(item, "values")[0] for item in table_fluid.get_children()]
    push_volume_combo['values'] = valuescm2
    root.after(1000, fill_combobox)

deeptrunk = 0.0

def res():

  # for item in table:
  #     pass

    selected_item = column_combobox.get()
    for item in table.get_children():
        values = table.item(item, "values")
        if values and values[0] == selected_item:

            deeptrunk = trynotnull(values[1])
            deepver   = trynotnull(values[2])
            insidediam= trynotnull(values[4])
            outerdiam = trynotnull(values[3])
            dolotodiam= trynotnull(values[5])
            stakan1   = trynotnull(values[6])
            koefkav   = trynotnull(values[7])
            poteri    = trynotnull(koef_entry.get())
            ring      = trynotnull(ring_space_height_entry.get())
            Kresprod  = trynotnull(koefprod_entry.get())
            NAME = values[0]
            Length    =  trynotnull(length_cem_entry.get())
            Klos      =  trynotnull(cement_coef_losless_entry.get())
            N_water   =  trynotnull(water_cement_entry.get())
            #CM_entry = float(CM_entry.get())  # подача воды
            #CM_quantity_entry = float(CM_quantity_entry()) # количество ЦМ
            # print(Gp.outer_space())
            Capacity = trynotnull(CM_overflow_entry.get())

            #CM_entry = float(CM_entry.get())  # подача воды
            #CM_quantity_entry = float(CM_quantity_entry()) # количество ЦМ
            # print(Gp.outer_space())


            MM_quantity = trynotnull(MM_quantity_entry.get())
            MM_water_flow = trynotnull(MM_entry.get())
            MM_tank_capasity = trynotnull(MM_overflow_entry.get())

            CM_quantity = trynotnull(CM_quantity_entry.get())
            CM_flow = trynotnull(CM_entry.get())
            CM_preassure = trynotnull(CM_overflow_entry.get())
            Q = CM_flow * CM_quantity

    gradient_valuev = []

    for rows in GradientTable.get_children():
        valuess = GradientTable.item(rows)['values']
        gradient_valuev.append(valuess)

    selected_item1 = column_combobox1.get()

    for item in table_fluid.get_children(): # тампонажный раствор
        values_fluid = table_fluid.item(item, "values")
        if values_fluid and values_fluid[0] == selected_item1:
            density_cem = float(values_fluid[3])
            Nasipnaya_density = float(values_fluid[1])
            DNS = float(values_fluid[4])
            dinamyc_va = float(values_fluid[5])

    selected_item2 = push_volume_combo.get()
    for item in table_fluid.get_children(): #продавочная жидкость
        values_push = table_fluid.item(item, "values")
        if values_push and values_push[0] == selected_item2:
            push_density = float(values_push[3])


    for item in table_fluid.get_children(): # буферная жидкость
        values_push = table_fluid.item(item, "values")
        if values_push and values_push[0] == "Буферная":
            buff_density = float(values_push[3])

    if selected_item == 'Направление':
        OS = (Gp.outer_space_simple(deeptrunk, deepver, Length, dolotodiam, koefkav, outerdiam, insidediam, stakan1, poteri, density_cem, N_water, NAME))

    elif selected_item == 'Кондуктор':
        OS = (Gp.outer_space(Napravlenie[2], deepver, Napravlenie[4], dolotodiam, koefkav, outerdiam, insidediam, stakan1, Klos, density_cem, N_water, deeptrunk, deepver, Length))

    elif selected_item == 'Промежуточная кол.':
        OS = (Gp.outer_space(Konductor[2], deepver, Konductor[4], dolotodiam, koefkav, outerdiam, insidediam, stakan1, Klos, density_cem, N_water, deeptrunk, deepver, Length))

    elif selected_item == 'Эксплуатационная кол.':

        OS = (Gp.outer_space(Promezutochnaya[2], deepver, Promezutochnaya[4],  dolotodiam, koefkav, outerdiam, insidediam, stakan1, Klos, density_cem, N_water, deeptrunk, deepver, Length))


    if selected_item == 'Направление':
        d_past = 0
        L_past1 = 0
    elif selected_item == 'Кондуктор':
        d_past =Napravlenie[4]
        L_past1 = Napravlenie[2]
    elif selected_item == 'Промежуточная кол.':
        d_past = Konductor[4]
        L_past1 = Konductor[2]
    elif selected_item == 'Эксплуатационная кол.':
        d_past = Promezutochnaya[4]
        L_past1 = Promezutochnaya[2]


    VB = (Gp.Volume_buff(dolotodiam, outerdiam, poteri, ring, deeptrunk, deepver))
    Wv = Gp.volume_water(N_water, OS[0], density_cem)
    PV = Gp.push_volume(Kresprod, insidediam, deeptrunk, stakan1)
    pzagr = Gp.Qpod(OS[0], OS[2], deeptrunk, 0.8)
    #Pmax = Gp.PMAX(deeptrunk, stakan1, density_cem, push_density, insidediam, dinamyc_va, pzagr, deepver, dolotodiam * koefkav, outerdiam, DNS)
    Bethas = Gp.bethas(DNS, dolotodiam*math.sqrt(koefkav), outerdiam, insidediam, dinamyc_va, CM_quantity*CM_flow)

    if parity_checkbutton == True:
        clean_density = push_density
    else:
        for item in table_fluid.get_children(): # промывочная жидкость
            values_clean = table_fluid.item(item, "values")
        if values_clean and values_clean[0] == "Промывочная":
            clean_density = float(values_clean[3])
    skvajina = dolotodiam*math.sqrt(koefkav)
    #if tank_check == True:
    #    pass
    #else:
    Hydro = Gp.critical_speed(Q, DNS, 999, push_density, buff_density, density_cem, skvajina, outerdiam, insidediam, dinamyc_va, deeptrunk, deepver, OS[5]*ring,
                              Bethas[0], Bethas[1], d_past, PV[1], gradient_valuev, 1200, L_past1, selected_item)
    print(Hydro)



    Podacha = Gp.mixing_cem(OS[3], Nasipnaya_density, Capacity, CM_flow, N_water, density_cem, 1000)
   # Hydro = Gp.critical_speed(Q, DNS, push_density, 1010, density_cem, dolotodiam*math.sqrt(koefkav), outerdiam, insidediam, dinamyc_va, deeptrunk, deepver, 89.0, Bethas[0], Bethas[1]) # заполнить полностью

    result_table.insert("", "end", values=(values[0], VB, OS[3], Wv, PV[0], Hydro[0]))







def Pressure_calculation():
    pass



items = []
items_fluid = []
result_list = []
Gradient_list = []

# Всплывающее окно


# функция_заполения_окна_жидкостей
def Fluid_open_popup():
    switch_type_fluid = ["Тампонаж", "Буферная", "Продавочная", "Промывочная"]

    # nameF,before, after, density, DNS, comprescoef
    selected_value = tk.StringVar()
    global popup
    popup_fluid = tk.Toplevel(root, width=100)
    popup_fluid.title("Растворы")
    popup_fluid.geometry("240x250")

    type_fluid_combo = ttk.Combobox(popup_fluid, values=switch_type_fluid, width=15)
    type_fluid_combo.bind("<Key>", lambda _: 'break')  # нельзя редактирвать комбо бокс
    type_fluid_combo.place(x=90, y=10)

    before_entry = tk.Entry(popup_fluid, width=10)
    after_entry = tk.Entry(popup_fluid, width=10)
    density_entry = tk.Entry(popup_fluid, width=10)
    dns_entry = tk.Entry(popup_fluid, width=10)
    before_entry.place(x=140, y=40)
    after_entry.place(x=140, y=70)
    density_entry.place(x=140, y=100)
    dns_entry.place(x=140, y=130)
    comprescoef_entry = tk.Entry(popup_fluid, width=10)

    name_label = tk.Label(popup_fluid,
                          text='Тип жидкости')
    name_label.place(x=5, y=10)
    befor_label = tk.Label(popup_fluid,
                           text='Насыпная плотность')
    befor_label.place(x=5, y=40)
    after_label = tk.Label(popup_fluid,
                           text='Длинна по стволу до, м')
    after_label.place(x=5, y=70)
    density_label = tk.Label(popup_fluid,
                             text='Плотность, Кг/м3')
    density_label.place(x=5, y=100)
    dns_label = tk.Label(popup_fluid,
                         text='ДНС, Па')
    dns_label.place(x=5, y=130)
    comprescoef_label = tk.Label(popup_fluid, text='Пластическая вязкость')


    comprescoef_entry.place(x=140, y=160)
    comprescoef_label.place(x=5, y=160)

    def save_item_fluid():
        Name_fluid = type_fluid_combo.get()
        Dry_density = trynotnull(before_entry.get())
        Long = trynotnull(after_entry.get())
        Density = trynotnull(density_entry.get())
        DNS = trynotnull(dns_entry.get())
        Viscosity = trynotnull(comprescoef_entry.get())
        item = Fluid(Name_fluid, Dry_density, Long, Density, DNS, Viscosity)
        items_fluid.append(item)
        update_fluid_table()
        popup_fluid.destroy()




    save_button_fluid = tk.Button(popup_fluid,
                            text="Сохранить",
                            command=save_item_fluid)
    save_button_fluid.place(x=130, y=190)


def Gradient_open_popup():



    selected_value = tk.StringVar()
    global popup
    popup_Gradient = tk.Toplevel(root, width=100)
    popup_Gradient.title("Градиент давлений")
    popup_Gradient.geometry("220x160")


    roof_entry = tk.Entry(popup_Gradient, width=10)
    roof_entry.place(x=150, y=13)
    Gradient_density_entry = tk.Entry(popup_Gradient, width=7)
    Sole_entry = tk.Entry(popup_Gradient, width=9)
    Gradient_density_entry.place(x=165, y=73)
    Sole_entry.place(x=155, y=43)


    roof_label = tk.Label(popup_Gradient,
                          text='Крыша пласта, М')
    roof_label.place(x=5, y=10)
    Sole_label = tk.Label(popup_Gradient,
                           text='Подошва пласта, М')
    Sole_label.place(x=5, y=40)
    Gradient_density_label = tk.Label(popup_Gradient,
                           text='Градиент давлений, КПа/М')
    Gradient_density_label.place(x=5, y=70)
    # nameF,before, after, density, DNS, comprescoef
    def save_item_Gradient():  # возможны ошибки с формулировкой
        global Number_gradient
        Number_gradient += 1
        Roof = (roof_entry.get())
        Sole = (Sole_entry.get())
        Gradient_density = (Gradient_density_entry.get())
        item_Gradient = Gradient(Number_gradient, Roof, Sole, Gradient_density)
        Gradient_list.append(item_Gradient)
        update_Gradient_table()
        popup_Gradient.destroy()



    save_button_Graident = tk.Button(popup_Gradient,
                                  text="Сохранить",
                                  command=save_item_Gradient
                                  )
    save_button_Graident.pack(side='bottom')

def delete_row_table():
    selection = table.focus()
    if selection:
        item = table.item(selection)
        item_id = item['values'][0]
        for data in items:
            if data.Name == item_id:
                items.remove(data)
                break
        table.delete(selection)


def delete_row_table_fluid():
    selection = table_fluid.focus()
    if selection:
        item = table_fluid.item(selection)
        item_id = item['values'][0]
        for data in items_fluid:
            if data.nameF == item_id:
                items_fluid.remove(data)
                break
        table_fluid.delete(selection)

def delete_row_Gradient_table():
    selection = GradientTable.focus()
    if selection:
        item = GradientTable.item(selection)
        item_id = item['values'][0]
        for data in Gradient_list:
            if data.Number == item_id:
                Gradient_list.remove(data)
                break
        GradientTable.delete(selection)


def export_to_excel():
    data = []
    for item in result_table.get_children():
        values = result_table.item(item, "values")
        data.append(values)

    df = pd.DataFrame(data, columns=['Наименование     ',
                                     'Объём буферной жидкости, м3',
                                     'Масса цемента, Кг', 'Масса воды для затворения цемента, Кг ',
                                     'Объём продавочной жидкости, м3',
                                     'Максимальное давление в устье, Па'])
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
    if file_path:
        df.to_excel(file_path, index=False)



# Основное окно
root = tk.Tk()
notebook = ttk.Notebook(root)
notebook.pack(fill='both',
              expand=True)

root.title("ЦОК")
root.geometry("900x600")

# Вкладки
tab1 = ttk.Frame(notebook)
notebook.add(tab1,
             text='Обсадные колонны')

tab2 = ttk.Frame(notebook)
notebook.add(tab2,
             text='Цементирование')
tab3 = ttk.Frame(notebook)
#notebook.add(tab3,
#             text='ЦА и ЦМ')
tab4 = ttk.Frame(notebook)
notebook.add(tab4,
             text='Результаты')

# виджеты
default_value = 1.0
entry_Var = tk.DoubleVar()
entry_Var.set(default_value)


name_table = tk.Label(tab1,
                      text='Обсадные колонны',
                      font='bold 13')
name_table.place(x=669, y=27)
name_table1 = tk.Label(tab1,
                      text='Материалы цементирования',
                       font='bold 13')
name_table1.place(x=600, y=197)

# Таблица обсадных колонн
table = ttk.Treeview(tab1, columns=("Name", "Depthdes", "Depthver", "Columndiam", "Insidediam", "Chiseldiam", "Stakan" "Coeftrikery"),
                     height=5,
                     padding=0,
                     show='headings')

open_popup_button = tk.Button(root,
                              text="Расчитать",
                              command= lambda: print(items)
                              )


open_popup_button = tk.Button(tab1,
                              text="Добавить",
                              command=open_popup
                              )
open_popup_button.place(x=11, y=23)

edit_popup_button = tk.Button(tab1,
                              text="Редактировать",
                              command=delete_row_table
                              )
edit_popup_button.place(x=75, y=23)

delete_popup_button = tk.Button(tab1,
                                text="Удалить",
                                command=delete_row_table
                                )
delete_popup_button.place(x=166, y=23)

heads = ["Название", "Глубина спуска", "Длина по оси", "Наружный диаметр", "внутренний диаметр", "диаметр долота", "глубина стакана", "Коэф. кавер."]
table['columns'] = heads
table.column(0, width=100)
table.column(1, width=100)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=100)
table.column(5, width=100)
table.column(6, width=100)
table.column(7, width=100)

for header in heads:
    table.heading(header, text=header, anchor='center')
# table.heading("#0",text="Название", )
# table.heading("#1",text="Глубина спуска(ствол), м")
# table.heading("#2",text="Глубина спуска (верт), м")
# table.heading("#3",text="Наружный диаметр колонны, мм")
# table.heading("#4",text="Диаметр долота, мм")
# table.heading("#5",text="Глубина стакана, м")
# table.heading("#6",text="Коэффициент каверзности, мм")

table.place(x=10, y=50)
# Таблица жидкостей
table_fluid = ttk.Treeview(tab1, columns=('nameF', 'before', 'after', 'density', 'DNS', 'comprescoef'), height=5,
                           padding=0, show="headings")

heads_fluid = ['Название', 'От(ствол), м', 'До(ствол), м', 'Плотность. Кг/м3', 'ДНС, Па', 'Пластическая вязкость, Па*с']
table_fluid['columns'] = heads_fluid
table_fluid.column(0, width=120)
table_fluid.column(1, width=150)
table_fluid.column(2, width=150)
table_fluid.column(3, width=130)
table_fluid.column(4, width=80)
table_fluid.column(5, width=170)

# for header in heads:
#    table_fluid.heading(header, text=header,)
#    table_fluid.column(header, anchor='center')

for header_fluid in heads_fluid:
    table_fluid.heading(header_fluid, text=header_fluid, anchor='center')

table_fluid.place(x=10, y=220)

Fluid_open_popup_button = tk.Button(tab1,
                                    text="Добавить",
                                    command=Fluid_open_popup
                                    )
Fluid_open_popup_button.place(x=11, y=193)

Fluid_edit_popup_button = tk.Button(tab1,
                                    text="Редактировать",
                                    command=Fluid_open_popup
                                    )
Fluid_edit_popup_button.place(x=75, y=193)

Fluid_delete_popup_button = tk.Button(tab1,
                                      text="Удалить",
                                      command=delete_row_table_fluid
                                      )
Fluid_delete_popup_button.place(x=166, y=193)
# таблица градиента давлений
GradientTable = ttk.Treeview(tab1, columns=("Number", "Roof", "Sole", "DevourDensity",),
                     height=5,
                     padding=0,
                     show='headings')

heads_Gradient = ['№#', 'Кровля, М', 'Подошва, М', 'Давление поглощения, Па/м']
GradientTable['columns'] = heads_Gradient
GradientTable.column(0, width=30)
GradientTable.column(1, width=80)
GradientTable.column(2, width=80)
GradientTable.column(3, width=140)
for header_Gradient in heads_Gradient:
    GradientTable.heading(header_Gradient, text=header_Gradient, anchor='center')
GradientTable.place(x=485, y=386)

open_gradient_popup_button = tk.Button(tab1,


                              text="Добавить",
                              command=Gradient_open_popup
                              )
open_gradient_popup_button.place(x=485, y=359)

delete_gradient_popup_button = tk.Button(tab1,
                                text="Удалить",
                                command=delete_row_Gradient_table
                                )
delete_gradient_popup_button.place(x=549, y=359)
Gradientlabel = tk.Label(tab1, text="Градиент давлений", font='bold 13'
                        )
Gradientlabel.place(x=666, y=361)
# Вкладка 2 расчёты
ring_space_height_entry = tk.Entry(tab2,
                                   width='7', )
ring_space_height_entry.place(x=205, y=96)
water_cement_entry = tk.Entry(tab2,
                              width=7
                              )
water_cement_entry.place(x=205, y=132)
water_cement_label = tk.Label(tab2,
                              text='Водно-цементное отношение')
water_cement_label.place(x=1, y=130)

column_combobox = ttk.Combobox(tab2,
                               values=table,
                               )
column_combobox.place(x=190, y=5)

column_label = tk.Label(tab2,
                        text='Выберите колонну для расчётов'
                        )
column_label.place(x=1, y=5)
ring_space_height_label = tk.Label(tab2,
                                   text='Высота столба буферной жидкости\nв кольцевом пространстве, м',
                                   anchor='nw',
                                   justify="left"
                                   )
ring_space_height_label.place(x=1, y=90)

column_combobox1 = ttk.Combobox(tab2,
                                values=table,
                                )

column_combobox1.place(x=190, y=35)
column_label1 = tk.Label(tab2,
                         text='Выберите тампонажный раствор'
                         )
column_label1.place(x=1, y=33)

koef_entry = tk.Entry(tab1,
                      textvariable=default_value,
                      width=5,
                      )

koef_entry.place(x=195, y=440)
koef_label = tk.Label(tab1,
                      text='Коэффициент потери БЖ'
                      )
koef_label.place(x=13, y=440)

koefprod_entry = tk.Entry(tab1,
                         width=5,
                          textvariable=default_value)
koefprod_entry.place(x=195, y=473)
koefprod_label = tk.Label(tab1,
                      text='Коэффициент потери ПЖ')
koefprod_label.place(x=13, y=473)
push_volume_combo = ttk.Combobox(tab2
                                 )
push_volume_combo.place(x=190, y=65)
push_volume_label = tk.Label(tab2,
                             text='Выберите продавочну жидкость')
push_volume_label.place(x=1, y=63)

length_cem_label = tk.Label(tab2,
                      text='Интервал цементирования')
length_cem_label.place(x=1, y=160)
length_cem_entry = tk.Entry(tab2,
                            width=7)
length_cem_entry.place(x=205, y=160)

MM_entry = tk.Entry(tab2, width=7)
MM_entry.place(x=535, y=15)
MM_Label = tk.Label(tab2, text='Подача воды ЦМ, л/с')
MM_Label.place(x=370, y=13)

MM_quantity_entry = tk.Entry(tab2, width=7)
MM_quantity_entry.place(x=535, y=45)
MM_quantity_label = tk.Label(tab2, text='Количество ЦМ')
MM_quantity_label.place(x=370, y=43)

MM_overflow_entry = tk.Entry(tab2, width=7)
MM_overflow_entry.place(x=535, y=75)
MM_overflow_label = tk.Label(tab2, text='Вместимость бункера ЦМ, т')
MM_overflow_label.place(x=370, y=73)
# a= tk.DoubleVar()

CM_entry = tk.Entry(tab2, width=7)
CM_entry.place(x=785, y=15)
CM_Label = tk.Label(tab2, text='Подача ЦА, л/с')
CM_Label.place(x=620, y=13)

CM_quantity_entry = tk.Entry(tab2, width=7)
CM_quantity_entry.place(x=785, y=45)
CM_quantity_label = tk.Label(tab2, text='Количество ЦА')
CM_quantity_label.place(x=620, y=43)

CM_overflow_entry = tk.Entry(tab2, width=7)
CM_overflow_entry.place(x=785, y=75)
CM_overflow_label = tk.Label(tab2, text='Давление ЦА, МПа')
CM_overflow_label.place(x=620, y=73)


#enabled = BooleanVar()
parity_checkbutton = ttk.Checkbutton(tab2, text="Использовать в качестве продавочной жидкости  промывочную", )
parity_checkbutton.place(x=13, y=193)
'''
#lie down baby 
#Arch your back now
#Maybe you can help me 
# get what i want
'''



# venture = float(test_entry.get())
# result22 = Test_Link.Volume_buff(30, 20, 1.05, venture)
# result1_label = tk.Label(tab2, text=result22).pack()



# Вкладка 3 ЦА и ЦМ

CU_insert_button = tk.Button(tab3, text="добавить ЦА",)
CU_insert_button.place(x=570, y=250)
MM_insert_button = tk.Button(tab3, text="добавить ЦМ",)
MM_insert_button.place(x=170, y=250)

CU_Choose_combobox = ttk.Combobox(tab3, textvariable=[1], width=20)
CU_Choose_combobox.place(x=570, y=5)
MM_Choose_combobox = ttk.Combobox(tab3, textvariable=1, width=20)
MM_Choose_combobox.place(x=150, y=5)


entry01 = tk.Entry(tab3, width=10) # Имя
entry02 = tk.Entry(tab3, width=10) # диаметр втулок
entry03 = tk.Entry(tab3, width=10) # Подача л/с
entry04 = tk.Entry(tab3, width=10) # Максимальное давление МПа
entry05 = tk.Entry(tab3, width=10) # коэффициент продуктивности
entry06 = tk.Entry(tab3, width=10) # Число ходов / передача

entry07 = tk.Entry(tab3, width=10) # Наименование ЦМ
entry08 = tk.Entry(tab3, width=10) #  Вместимость бункера
entry09 = tk.Entry(tab3, width=10) #  Подача водяного насоса
entry10 = tk.Entry(tab3, width=10) #  Давление, МПа


entry11 = tk.Entry(tab3, width=9) #

entry01.place(x=590, y=60)
entry02.place(x=590, y=90)
entry03.place(x=590, y=120)
entry04.place(x=590, y=150)
entry05.place(x=590, y=180)
entry06.place(x=590, y=210)

entry07.place(x=150, y=60)
entry08.place(x=150, y=90)
entry09.place(x=150, y=120)
entry10.place(x=150, y=150)

entry11.place(x=10, y=1)

label0 = tk.Label(tab3, text='Цементировочный агрегат ')
label1 = tk.Label(tab3, text='Имя')
label2 = tk.Label(tab3, text='диаметр втулки')
label3 = tk.Label(tab3, text='Подача л/с')
label4 = tk.Label(tab3, text='Максимальное давление МПа')
label5 = tk.Label(tab3, text='коэффициент продуктивности')
label6 = tk.Label(tab3, text='Число ходов / передача')

label00 = tk.Label(tab3, text='Цементировочная машина ')
label7 = tk.Label(tab3, text='Наименование ЦМ')
label8 = tk.Label(tab3, text='Вместимость бункера')
label9 = tk.Label(tab3, text='Подача водяного насоса')
label10= tk.Label(tab3, text='Давление, МПа')

label00.place(x=30, y=30)
label0.place(x=430, y=30)
label1.place(x=410, y=60)
label2.place(x=410, y=90)
label3.place(x=410, y=120)
label4.place(x=410, y=150)
label5.place(x=410, y=180)
label6.place(x=410, y=210)

label7.place(x=10, y=60)
label8.place(x=10, y=90)
label9.place(x=10, y=120)
label10.place(x=10, y=150)


water_pump_check = tk.Checkbutton(tab3, text='Использовать ЦА вместо водоподающего насоса')
water_pump_check.place(x=10, y=350)
movenumbers_check = tk.Checkbutton(tab3, text='Использовать число ходов вместо скоростей ')
movenumbers_check.place(x=10, y=320)
tank_check = tk.Checkbutton(tab3, text='Использование осреднительной ёмкости')   # чекбокс использования осреднительной ёмкости
tank_check.place(x=10, y=290)
if tank_check == True:
    print('не тру')
else:
    pass


# Вкладка 4 результы
result_table = ttk.Treeview(tab2,
                            columns=('name', 'buffervol', 'cement', 'water_zatvor', 'volume_push', 'Pmax'),
                            height=11,
                            padding=0,
                            show="headings")

heads_result = ['Название', 'Объём буф. жид.', 'Масса цементного раствора', 'Объём воды для затворения', 'Объём продавочной жидкости',
                'Макc. давление в устье']
result_table['columns'] = heads_result
result_table.column(0, width=110)
result_table.column(1, width=130)
result_table.column(2, width=165)
result_table.column(3, width=165)
result_table.column(4, width=165)
result_table.column(5, width=150)
result_table.pack(side='bottom')
# for header in heads:
#    table_fluid.heading(header, text=header,)
#    table_fluid.column(header, anchor='center')

for header_result in heads_result:
    result_table.heading(header_result, text=header_result, anchor='center')

result_table.place(x=5, y=250)


final_table_tab4 = ttk.Treeview(tab4,
                            columns=('name', 'buffervol', 'cement', 'water_zatvor', 'volume_push', 'Pmax'),
                            height=11,
                            padding=0,
                            show="headings")

heads_final_tab4 = ['Название', 'Объём буф. жид.', 'Масса цементного раствора', 'Объём воды для затворения', 'Объём продавочной жидкости',
                'Макc. давление в устье']
final_table_tab4['columns'] = heads_final_tab4
final_table_tab4.column(0, width=110)
final_table_tab4.column(1, width=130)
final_table_tab4.column(2, width=165)
final_table_tab4.column(3, width=165)
final_table_tab4.column(4, width=165)
final_table_tab4.column(5, width=150)
final_table_tab4.pack(side='bottom')

final_table_tab4.place(x=5, y=100)
for header_result in heads_final_tab4:
    final_table_tab4.heading(header_result, text=header_result, anchor='center')

# Вкладка??
fill_combobox()
# активные элементы
cement_coef_losless_entry = tk.Entry(tab1,
                                     textvariable=default_value,
                                     width=5)
cement_coef_losless_entry.place(x=196, y=363)
cement_coef_losless_label = tk.Label(tab1,
                                     text='Коэффициент потери цемента')
cement_coef_losless_label.place(x=13, y=360)

water_coef_losless_entry = tk.Entry(tab1,
                                    textvariable=default_value,
                                    width=5)
water_coef_losless_entry.place(x=196, y=393)
water_coef_losless_label = tk.Label(tab1,
                                    text='Коэффициент потери воды')
water_coef_losless_label.place(x=13, y=390)

test_button = tk.Button(tab2,
                        text='Расчёт',
                        command=res, width=6, border='1',
                        )
test_button.place(x=30, y=223)
# прочее
export_button = ttk.Button(tab2, text="Экспорт в Excel", command=export_to_excel)
export_button.place(x=790, y=225)

column_combobox.bind("<<ComboboxSelected>>", res)
# Запуск цикла обработки событий
root.mainloop()
