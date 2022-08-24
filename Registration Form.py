from tkinter import*
root = Tk()
root.geometry('500x500')
root.title("Registration Form")

bg = PhotoImage(file=r"C:\Users\abhir\Desktop\bgphoto2.png")
label_5 = Label(root, image=bg)
label_5.place(x=0, y=0)

label_0 = Label(root, text="Registration form", width=20, font=("bold", 20), bg='black', fg='white')
label_0.place(x=90, y=53)

label_1 = Label(root, text="FullName", width=20, font=("bold", 10),  bg='black', fg='white')
label_1.place(x=80, y=130)

entry_1 = Entry(root)
entry_1.place(x=240, y=130)

label_2 = Label(root, text="Email", width=20, font=("bold", 10),  bg='black', fg='white')
label_2.place(x=68, y=180)

entry_2 = Entry(root)
entry_2.place(x=240, y=180)

label_3 = Label(root, text="Gender", width=20, font=("bold", 10),  bg='black', fg='white')
label_3.place(x=70, y=230)
var = IntVar()
Radiobutton(root, text="Male", padx=5, variable=var, value=1,  bg='white', fg='blue').place(x=235, y=230)
Radiobutton(root, text="Female", padx=20, variable=var, value=2,  bg='white', fg='blue').place(x=290, y=230)

label_4 = Label(root, text="Age:", width=20, font=("bold", 10),  bg='black', fg='white')
label_4.place(x=70, y=280)


entry_2 = Entry(root)
entry_2.place(x=240, y=280)

Button(root, text='Submit', width=20, bg='black', fg='white').place(x=180, y=380)

root.mainloop()
print("registration form  seccussfully created...")