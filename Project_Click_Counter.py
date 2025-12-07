from tkinter import *
# عمر احمد احمد احمد الغمراوي

counter = 0

def increment_counter():
    global counter
    counter += 1
    mylabel.config(text=f"عدد النقرات الآن: {counter}")

myframe = Tk()
myframe.title("عداد النقرات (Click Counter)")
myframe.geometry("350x200")

mylabel = Label(
    myframe, 
    text=f"عدد النقرات الآن: {counter}", 
    font="Helvatica 18 bold", 
    fg="blue"
)
mylabel.pack(pady=30) 

mybutton = Button(
    myframe,
    text="اضغط لزيادة العداد",
    fg="white", 
    bg="#008CBA",
    font="Helvatica 12 bold",
    padx=15, 
    pady=8,
    command=increment_counter,
)
mybutton.pack(pady=10)

myframe.mainloop()

