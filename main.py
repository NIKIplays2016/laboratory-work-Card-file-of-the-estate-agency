from tkinter import *
from modules.db_manager import DBManager


class App:
    def __init__(self):
        self.manager = DBManager()
        self.manager.create_table()
        self.manager.create_call_table()
        self.root = Tk()
        self.root.title("Real Estate")
        self.root.geometry("800x600")
        self.font = ("Arial", 12)



        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):

        Label().grid(row=0, column=0)
        Label().grid(row=2, column=0)
        Label().grid(row=4, column=0)
        Label().grid(row=6, column=0)
        Label().grid(row=8, column=0)
        Label(text="        ").grid(row=0, column=2)
        Label().grid(row=9, column=0)
        Label().grid(row=12, column=0)

        Label(self.root, text="Тип недвижимости: ", font=self.font).grid(row=1, column=0)
        self.type_entry = Entry(self.root, font=self.font)
        self.type_entry.grid(row=1, column=1)

        Label(self.root, text="Город: ", font=self.font).grid(row=3, column=0)
        self.city_entry = Entry(self.root, font=self.font)
        self.city_entry.grid(row=3, column=1)

        Label(self.root, text="Улица: ", font=self.font).grid(row=5, column=0)
        self.street_entry = Entry(self.root, font=self.font)
        self.street_entry.grid(row=5, column=1)

        Label(self.root, text="Номер дома: ", font=self.font).grid(row=7, column=0)
        self.number_entry = Entry(self.root)
        self.number_entry.grid(row=7, column=1)



        Label(self.root, text="Площадь: ", font=self.font).grid(row=1, column=3)
        Label(self.root, text= "от    до", font=self.font).grid(row=1, column=4)
        self.square_entry = Entry(self.root, font=self.font)
        self.square_entry.grid(row=2, column=4)

        Label(self.root, text="Цена: ", font=self.font).grid(row=4, column=3)
        Label(self.root, text= "от    до", font=self.font).grid(row=4, column=4)
        self.price_entry = Entry(self.root, font=self.font)
        self.price_entry.grid(row=5, column=4)

        Label(self.root, text="Количество комнат: ", font=self.font).grid(row=7, column=3)
        Label(self.root, text= "от    до", font=self.font).grid(row=7, column=4)
        self.rooms_entry = Entry(self.root, font=self.font)
        self.rooms_entry.grid(row=8, column=4)

        Label(self.root, text="Этаж: ", font=self.font).grid(row=10, column=0)
        self.floor_entry = Entry(self.root, font=self.font)
        self.floor_entry.grid(row=10, column=1)

        Button(
            self.root,
            text="Поиск",
            font=self.font,
            command=self.search,
            width=10,
            height=1,
            bg="lightblue",
        ).place(x=630, y=240)

        Label(text="Ваш номер телефона: ", font=self.font).place(x=360, y=230)
        self.phone_entry = Entry(self.root, font=self.font)
        self.phone_entry.place(x=360, y=260)

        self.result_text = Text(self.root, height=15, width=86, font=self.font)
        self.result_text.place(x=10, y=300)

        Button(
            self.root,
            text="Уведомить",
            font=self.font,
            command= self.compl_call,
            width=10,
            height=1,
            bg="lightgreen",
        ).place(x=687, y=540)

    def compl_call(self):
        phone = self.phone_entry.get()
        estate_type = self.type_entry.get()
        city = self.city_entry.get()
        street = self.street_entry.get()
        number = self.number_entry.get()
        square = self.square_entry.get()
        price = self.price_entry.get()
        rooms = self.rooms_entry.get()
        floor = self.floor_entry.get()
        self.manager.add_call(estate_type, city, street, number, square, price, rooms, floor, phone)
    def search(self):
        estate_type = self.type_entry.get()
        city = self.city_entry.get()
        street = self.street_entry.get()
        number = self.number_entry.get()
        square = self.square_entry.get()
        price = self.price_entry.get()
        rooms = self.rooms_entry.get()
        floor = self.floor_entry.get()

        result = self.manager.find_estate(estate_type, city, street, number, square, price, rooms, floor)

        self.result_text.delete(1.0, END)

        if len(result) == 0:
            self.result_text.insert(1.0, "Ничего не найдено \nНажмите на кнопку 'Уведомить' чтобы уведомить вас о появлении подходящего варианта")
        else:
            print(result)
            self.result_text.insert(END, f"Найдено {len(result)} вариантов\n\n\n")

            for i, row in enumerate(result):

                text = "-" * 50 + "\n"
                text += f"Недвижимость №{i+1}"
                text += f"\n Тип недвижимости: {row[1]} \n Город: {row[2]} \n Улица: {row[3]} \n Номер дома: {row[4]} \n Площадь: {row[5]} \n Цена: {row[6]} \n Количество комнат: {row[7]} \n Этаж: {row[8]} \n Комментарий: {row[9]} \n"
                text += "\n\n\n"


                self.result_text.insert(END, text)


App()