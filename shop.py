import os
import datetime
from tkinter import *
from tkinter import messagebox

class Products:
    def __init__(self, id, name, price) -> None:
        self.id = id
        self.name = name
        self.price = price

class shopping_cart:
    def __init__(self) -> None:
        self.temp_cart = {}
        self.temp_total= 0
        self.products = {
            "1": Products("1", "Twix", 1.2),
            "2": Products("2", "Lollipop", 1.6),
            "3": Products("3", "Taffy", 1.4),
            "4": Products("4", "Gummy bears", 2.5),
            "5": Products("5", "Polly", 3.2),
            "6": Products("6", "Smash", 2.7),
            "7": Products("7", "Snickers", 1.3),
            "8": Products("8", "Toblerone", 1.5),
            "9": Products("9", "Gobstopper", 16),
        }

    def add_product(self, id, amount, id_box, amount_box, amount_number):
        id_box.delete("1.0", END)
        amount_box.delete("1.0", END)
        for symbol in id:
            if not symbol.isdigit():
                messagebox.showerror(title="Error", message="Invalid ID")
                return
        if id not in self.products:
            messagebox.showerror(title="Error", message="Invalid ID")
            return
        if not len(amount):
            messagebox.showerror(title="Error", message="Invalid amount")
            return
        for symbol in amount:
            if not symbol.isdigit():
                messagebox.showerror(title="Error", message="Invalid amount")
                return
        if int(amount) == 0:
            messagebox.showerror(title="Error", message="Invalid amount")
            return
        if id not in self.temp_cart:
            self.temp_cart.setdefault(id, int(amount))
        else: 
            self.temp_cart[id] = self.temp_cart[id] + int(amount)
        self.temp_total = round(self.temp_total + int(amount) * self.products[id].price, 2)
        if self.temp_total > 999:
            amount_number.config(
                text=str(self.temp_total / 1000)[
                    0 : str(self.temp_total / 1000).index(".") + 2
                ]
                + "K$"
            )
        else:
            amount_number.config(text=str(self.temp_total) + "$")

    def debit(self, amount_number):
        if self.temp_total == 0:
            messagebox.showerror(
                title="Error",
                message="Can't process order. There are no items in the cart",
            )
            return
        receipt_text = ""
        for item in self.temp_cart:
            receipt_text = (
                receipt_text
                + self.products[item].name
                + ": "
                + str(self.temp_cart[item])
                + ", "
                + str(self.temp_cart[item] * self.products[item].price)
                + "$\n"
            )
        amount_number.config(text="0$")
        messagebox.showinfo(
            title=datetime.datetime.strftime(datetime.datetime.now(), "%x %X"),
            message="Receipt: \n"
            + receipt_text
            + "Total: "
            + str(self.temp_total)
            + "$",
        )
        self.temp_total = 0
        self.temp_cart = {}
        return

class GUI:
    def __init__(self) -> None:
        self.shopping_cart = shopping_cart()

    def start(self):
        os.system("cls" if os.name == "nt" else "clear")
        root = Tk()
        root.title("Shop")
        root.geometry("900x500")
        root.resizable(0, 0)
        bg = PhotoImage(file="cndy.png")
        background = Label(root, image=bg)
        background.place(x=0, y=0, relwidth=1, relheight=1)
        amount_text = Label(
            root,
            text="Current amount:",
            font=("Times New Roman", 40),
            bd=5,
            relief=SOLID,
            bg = "light blue"
        )
        amount_text.place(x=210, y=20)
        amount_number = Label(
            root,
            text="0$",
            width=5,
            height=1,
            font=("Times New Roman", 40),
            bd=5,
            relief=SOLID,
            bg = "light blue"
        )
        amount_number.place(x=640, y=20)
        menu_header = Label(
            root,
            height=1,
            width=13,
            text="Products",
            font=("Times New Roman", 30),
            bd=5,
            relief=SOLID,
            bg="light blue",
        )
        menu_header.place(x=20, y=120)
        menu_options = Label(
            root,
            height=11,
            width=23,
            text="ID(1): Twix 1.2$\nID(2): Lollipop 1.6$\nID(3): "
            + "Taffy 1.4$\nID(4): Gummy bears 2.5$\nID(5): Polly 3.2$\nID(6): Smash 2.7$"
            + "\nID(7): Snickers 1.3$\nID(8): Toblerone 1.5$\nID(9): Gobstopper 16$",
            font=("Times New Roman", 15),
            bd=4,
            relief=SOLID,
        )
        menu_options.place(x=36, y=183)
        id_label = Label(root, text="ID:", width=3, font=("Times New Roman", 40))
        id_label.place(x=320, y=250)
        id_box = Text(root, height=1, width=3, font=("Times New Roman", 30))
        id_box.place(x=445, y=260)
        amount_label = Label(root, text="X", width=2, font=("Times New Roman", 40))
        amount_label.place(x=540, y=250)
        amount_box = Text(root, height=1, width=3, font=("Times New Roman", 30))
        amount_box.place(x=635, y=260)
        button = Button(
            root,
            height=1,
            width=5,
            text="Pay!",
            font=("Times New Roman", 30),
            bg="light blue",
            bd=3,
            relief=RAISED,
            command=lambda: self.shopping_cart.debit(amount_number),
        )
        button.place(x=740, y=245)
        root.bind(
            "<Return>",
            lambda event: self.shopping_cart.add_product(
                id_box.get("1.0", END)[0:-1].replace("\n", ""),
                amount_box.get("1.0", END)[0:-1].replace("\n", ""),
                id_box,
                amount_box,
                amount_number,
            ),
        )
        root.mainloop()


if __name__ == "__main__":
    gui = GUI()
    gui.start()
