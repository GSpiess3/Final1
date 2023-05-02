from tkinter import *

class GUI:
    def __init__(self, window):
        self.window = window

        # Radio buttons
        self.frame_Select = Frame(self.window)
        self.label_Options = Label(self.frame_Select, text='Select One of the options below')
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.radio_add = Radiobutton(self.frame_Select, text='Add', variable=self.radio_1, value=1, command=self.Option)
        self.radio_sub = Radiobutton(self.frame_Select, text='Sub', variable=self.radio_1, value=2, command=self.Option)
        self.radio_mult = Radiobutton(self.frame_Select, text='Multiplication', variable=self.radio_1, value=3, command=self.Option)
        self.radio_div = Radiobutton(self.frame_Select, text='Divide', variable=self.radio_1, value=4, command=self.Option)
        self.label_Options.pack(padx=5)
        self.radio_add.pack()
        self.radio_sub.pack()
        self.radio_mult.pack()
        self.radio_div.pack()
        self.frame_Select.pack(anchor='w', pady=10)
        
        # Example Label
        self.frame_example = Frame(self.window)
        self.label_example = Label(self.frame_example)
        self.entry_example = Entry(self.frame_example, width=40)
        self.label_example.pack(padx=20, side='left')
        self.entry_example.pack(padx=20, side='left')
        self.frame_example.pack(anchor='w', pady=10)
        self.entry_example.pack_forget()
        

        # First number
        self.frame_first = Frame(self.window)
        self.label_first = Label(self.frame_first)
        self.entry_first = Entry(self.frame_first, width=40)
        self.label_first.pack(padx=20, side='left')
        self.entry_first.pack(padx=20, side='left')
        self.frame_first.pack(anchor='w', pady=10)
        self.entry_first.pack_forget()

        # Second number
        self.frame_second = Frame(self.window)
        self.label_second = Label(self.frame_second)
        self.entry_second = Entry(self.frame_second, width=40)
        self.label_second.pack(padx=20, side='left')
        self.entry_second.pack(padx=20, side='left')
        self.frame_second.pack(anchor='w', pady=10)
        self.entry_second.pack_forget()

        # Results label
        self.frame_result = Frame(self.window)
        self.label_result = Label(self.frame_result)
        self.label_result.pack(pady=10)
        self.frame_result.pack()

        # Compute button
        self.frame_button = Frame(self.window)
        self.button_compute = Button(self.frame_button, text='COMPUTE', command=self.Compute)
        self.button_compute.pack(pady=10)
        self.frame_button.pack()

    def Option(self):
        self.entry_first.delete(0, END)
        self.entry_second.delete(0, END)
        self.label_result.config(text='')
        self.entry_first.pack()
        selection: int = self.radio_1.get()

        if selection == 1:
            self.label_first.config(text='First Number')
            self.label_second.config(text='Second Number')
            self.entry_second.pack()
        elif selection == 2:
            self.label_first.config(text='First Number')
            self.label_second.config(text='Second Number')
            self.entry_second.pack()
        elif selection == 3:
            self.label_first.config(text='First Number')
            self.label_second.config(text='Second Number')
            self.entry_second.pack()
        elif selection == 4:
            self.label_first.config(text='First Number')
            self.label_second.config(text='Second Number')
            self.entry_second.pack()

    def Compute(self):
        try:
            first_num = self.entry_first.get()
            second_num = self.entry_second.get()
            option = self.radio_1.get()

            if option == 1:
                self.label_result.config(text=f'Circle area = {area.circle(first_num)}')
            elif option == 2:
                self.label_result.config(text=f'Square area = {area.square(first_num)}')
            elif option == 3:
                self.label_result.config(text=f'Rectangle area = {area.rectangle(first_num, second_num)}')
            elif option == 4:
                self.label_result.config(text=f'Triangle area = {area.triangle(first_num, second_num)}')
            else:
                self.label_result.config(text='No operation selected')
        except ValueError:
            self.label_result.config(text='Enter numeric values')
        except TypeError:
            self.label_result.config(text='Values must be positive')