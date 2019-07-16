# -*- coding: utf-8 -*-
import tkinter as tk
import SDKP
from tkinter import ttk


class SdkpEntryFrame:

    def __init__(self, master):

        self.frame = tk.LabelFrame(master)
        self.sd_entry = ["" for _ in range(9)]
        for i in range(9):
            self.sd_entry[i] = tk.Entry(self.frame, width=2, font=('meiryo', 10), justify="center")

        # self.e00 = tk.Entry(self.frame, width=2, font=('meiryo', 10), justify="center").grid(row=0, column=0)
        # self.e01 = tk.Entry(self.frame, width=2, font=('meiryo', 10), justify="center").grid(row=0, column=1)
        # self.e02 = tk.Entry(self.frame, width=2, font=('meiryo', 10), justify="center").grid(row=0, column=2)
        # self.e10 = tk.Entry(self.frame, width=2, font=('meiryo', 10), justify="center").grid(row=1, column=0)
        # self.e12 = tk.Entry(self.frame, width=2, font=('meiryo', 10), justify="center").grid(row=1, column=1)
        # self.e13 = tk.Entry(self.frame, width=2, font=('meiryo', 10), justify="center").grid(row=1, column=2)
        # self.e20 = tk.Entry(self.frame, width=2, font=('meiryo', 10), justify="center").grid(row=2, column=0)
        # self.e21 = tk.Entry(self.frame, width=2, font=('meiryo', 10), justify="center").grid(row=2, column=1)
        # self.e22 = tk.Entry(self.frame, width=2, font=('meiryo', 10), justify="center").grid(row=2, column=2)

    def grid_entry(self):
        cont = 0
        for i in range(3):
            for j in range(3):
                self.sd_entry[cont].grid(row=i, column=j)
                # print("#", i, j)
                cont += 1


def input_button(array):
    for i in range(9):
        for j in range(9):
            array_value[i][j] = int(0) if sd_frame[i].sd_entry[j].get() == '' else int(sd_frame[i].sd_entry[j].get())
    print(array_value)
    array_complete = SDKP.cal_sdkp(array_value)

    for i in range(9):
        for j in range(9):
            if sd_frame[i].sd_entry[j].get() == '':
                sd_frame[i].sd_entry[j].configure(foreground="red")
                sd_frame[i].sd_entry[j].insert(tk.END, array_complete[i][j])


def save_list(array):
    for i in range(9):
        for j in range(9):
            array_value[i][j] = int(0) if sd_frame[i].sd_entry[j].get() == '' else int(sd_frame[i].sd_entry[j].get())
    print(array_value)
    file_a = open('./list.txt', 'w')
    for i in range(9):
        for j in range(9):
            file_a.write(str(array_value[i][j]) + "\n")


def open_list():
    file_o = open("./list.txt", "r")
    list_row = [[_ for _ in range(9)] for _ in range(9)]

    for count, input_number in enumerate(file_o):
        count_x = count // 9
        count_y = count % 9
        #  print(count_x,count_y,input_number)
        list_row[count_x][count_y] = input_number.rstrip("\n")

    file_o.close()
    print(list_row)
    for i in range(9):
        for j in range(9):
            sd_frame[i].sd_entry[j].delete(0, tk.END)
            str_cell = list_row[i][j]
            if str_cell == '0':
                str_cell = ''
            sd_frame[i].sd_entry[j].insert(tk.END, str_cell)


def clear_cel():
    for i in range(9):
        for j in range(9):
            sd_frame[i].sd_entry[j].delete(0, tk.END)


master = tk.Tk()
master.title("数独瞬解きくん")
master.geometry("250x300")

frame0 = tk.LabelFrame(master)
frame1 = tk.LabelFrame(master)
frame0.pack()
frame1.pack()
sd_frame = [SdkpEntryFrame(frame0) for _ in range(9)]

count = 0
for i in range(3):
    for j in range(3):
        sd_frame[count].frame.grid(row=i, column=j)
        print("#", i, j, count)
        count += 1

for i in range(9):
    sd_frame[i].grid_entry()

array_value = [[0 for _ in range(9)] for _ in range(9)]

print(array_value)
b1 = tk.Button(
    frame1,
    text='実行',
    command=lambda: input_button(array_value)
)

b2 = tk.Button(
    frame1,
    text='保存',
    command=lambda: save_list(array_value)
)
b3 = tk.Button(
    frame1,
    text='開く',
    command=lambda: open_list()
)
b4 = tk.Button(
    frame1,
    text='クリア',
    command=lambda: clear_cel()
)
b1.pack(side="left")
b2.pack(side="left")
b3.pack(side="left")
b4.pack(side="left")
master.mainloop()
