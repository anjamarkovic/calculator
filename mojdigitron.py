from tkinter import *
import tkinter

root= tkinter.Tk()
#root.iconbitmap('C:\Users\Anja - AbakusWeb\work\.vscode\slike\digitron.png')
root.title("Calculator")
root.geometry("250x338")
root.resizable(0, 0)


"""Funkcije koje su potrebne za rad digitrona su: kliknuti dugme, brisanje i jednakost"""

def btn_click(item):
    """Funkcija azurira polje za unos svaki put kada se unese neki broj i omogucava novi unos
    Dakle, omogucava unos,zatim dodaje novi unos, podesava unos
    Koristim globalnu promjenljivu u sve 3 funkcije ce se ponasati kako sama funkcija zahtjeva
    """
    global expression
    expression = expression + str(item) #str(item) omogucava unos kao sto je: 7777 tipa string, da je tip int cifre bi se sabirale
    input_text.set(expression)

def btn_clear():
    """Funkcija brise prethodno unijeta polja i operacije koje su se obavljale"""
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    """Funkcija predstavlja proracun datog izraza. 
    Eval je ugradjena funkcija koja procjenjuje(eng.evaluate) racunsku operaciju, tj.izraz
    Da nismo koristili ovu funkciju, morali bi voditi racuna o znaku npr. if str(expression== '+') pa pozvati metod za sabiranje i tako za sve ostale operacije"""
    global expression
    result = str(eval(expression)) 
    input_text.set(result)
    expression = ""
expression = ""


input_text = StringVar()

#prozor za unos brojeva i njegov dizajn
input_frame = Frame(root, width = 250, height = 50,  bd = 5, highlightbackground = "#a7c7e7", highlightcolor = "#a7c7e7", highlightthickness = 1)
input_frame.pack(side = TOP)
input_field = Entry(input_frame, font = ('open sans', 18), textvariable = input_text, width = 50, bg = "#66cdaa", bd = 0, justify = RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10)

# prozor za dugmad i dizajn
btns_frame = Frame(root, width = 250, height = 300,  bg = "#a7c7e7" )
btns_frame.pack()


clear = Button(btns_frame, text = "C",  fg = "white", width = 7, height = 3,  bd = 0, bg = "#B22222", command = lambda: btn_clear()).grid(row = 0, column = 0,  padx = 1, pady = 1)
divide = Button(btns_frame, text = "/",fg = "#0e2f44", width = 7, height = 3, bd = 0, bg = "#eee",  command = lambda: btn_click("/")).grid(row = 1, column = 3, padx = 1, pady = 1)
seven = Button(btns_frame, text = "7", fg = "#0e2f44", width = 7, height = 3, bd = 0, bg = "#fff",  command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(btns_frame, text = "8", fg = "#0e2f44", width = 7, height = 3, bd = 0, bg = "#fff",  command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(btns_frame, text = "9", fg = "#0e2f44", width = 7, height = 3, bd = 0, bg = "#fff",  command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
multiply = Button(btns_frame, text = "*", fg = "#0e2f44", width = 7, height = 3, bd = 0, bg = "#eee",  command = lambda: btn_click("*")).grid(row = 2, column = 3, padx = 1, pady = 1)
four = Button(btns_frame, text = "4", fg = "#0e2f44", width = 7, height = 3, bd = 0, bg = "#fff",  command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(btns_frame, text = "5", fg = "#0e2f44", width = 7, height = 3, bd = 0, bg = "#fff",  command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(btns_frame, text = "6", fg = "#0e2f44", width = 7, height = 3, bd = 0, bg = "#fff",  command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
minus = Button(btns_frame, text = "-", fg = "black", width = 7, height = 3, bd = 0, bg = "#eee",  command = lambda: btn_click("-")).grid(row = 3, column = 3, padx = 1, pady = 1)
one = Button(btns_frame, text = "1", fg = "#0e2f44", width = 7, height = 3, bd = 0, bg = "#fff",  command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(btns_frame, text = "2", fg = "#0e2f44", width = 7, height = 3, bd = 0, bg = "#fff",  command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(btns_frame, text = "3", fg = "#0e2f44", width = 7, height = 3, bd = 0, bg = "#fff",  command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
plus = Button(btns_frame, text = "+", fg = "#0e2f44", width = 7, height = 3, bd = 0, bg = "#eee",  command = lambda: btn_click("+")).grid(row = 4, column = 3, padx = 1, pady = 1)
zero = Button(btns_frame, text = "0", fg = "#0e2f44", width = 7, height = 3, bd = 0, bg = "#fff",  command = lambda: btn_click(0)).grid(row = 4, column = 0,  padx = 1, pady = 1)
point = Button(btns_frame, text = ".", fg = "#0e2f44", width = 7, height = 3, bd = 0, bg = "#eee",  command = lambda: btn_click(".")).grid(row = 4, column = 1, padx = 1, pady = 1)
equals = Button(btns_frame, text = "=", fg = "#0e2f44", width = 7, height = 3, bd = 0, bg = "#eee",  command = lambda: btn_equal()).grid(row = 4, column = 2, padx = 1, pady = 1)
root.mainloop()
