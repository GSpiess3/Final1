from tkinter import *
import Calculations


class GUI:
    def __init__(self, window):
        '''

        :param window: connects to the gui page
        radio buttons: Allows the user to pick the operation they wish to choose
        example label: when an operation is selected this label gives you a hint on the order
        first number: first entry
        second number: second entry
        results label: Will give the results
        compute button: click to calculate
        '''
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
        self.radio_geometry = Radiobutton(self.frame_Select, text='geometry', variable=self.radio_1, value=5, command=self.Option)
        self.label_Options.pack(padx=5)
        self.radio_add.pack()
        self.radio_sub.pack()
        self.radio_mult.pack()
        self.radio_div.pack()
        self.radio_geometry.pack()
        self.frame_Select.pack(pady=10)
        
        # Example Label
        self.frame_example = Frame(self.window)
        self.label_example = Label(self.frame_example)
        self.entry_example = Entry(self.frame_example, width=40)
        self.label_example.pack(padx=20, side='left')
        self.entry_example.pack(padx=20, side='left')
        self.frame_example.pack(pady=10)
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
            self.label_example.config(text='You selected addition!!\n Ex: first number + second number')
            self.label_first.config(text='First Number')
            self.label_second.config(text='Second Number')
            self.entry_second.pack()

        elif selection == 2:
            self.label_example.config(text='You selected subtraction!!\n Ex: first number - second number')
            self.label_first.config(text='First Number')
            self.label_second.config(text='Second Number')
            self.entry_second.pack()
        elif selection == 3:
            self.label_example.config(text='You selected multiplication!!\n Ex: first number * second number')
            self.label_first.config(text='First Number')
            self.label_second.config(text='Second Number')
            self.entry_second.pack()
        elif selection == 4:
            self.label_example.config(text='You selected division!!\n Ex: first number / second number\n Hint: you cant divide by zero')
            self.label_first.config(text='First Number')
            self.label_second.config(text='Second Number')
            self.entry_second.pack()

    def Compute(self):
        '''
        param num1: The first number used in the calculations
        param num2: The second number used in the calculations
        param option: The operation that will be performed
        :return: returns the output using the numbers given and the operation chosen to the 4th decimal pint
        '''
        try:
            num1 = self.entry_first.get()
            num2 = self.entry_second.get()
            option = self.radio_1.get()

            if option == 1:
                self.label_result.config(text=f'{num1} + {num2} = {Calculations.add(num1, num2):.4f}')
            elif option == 2:
                self.label_result.config(text=f'{num1} - {num2} = {Calculations.sub(num1, num2):.4f}')
            elif option == 3:
                self.label_result.config(text=f'{num1} * {num2} = {Calculations.mult(num1, num2):.4f}')
            elif option == 4:
                self.label_result.config(text=f'{num1} / {num2} = {Calculations.div(num1, num2):.4f}')
            else:
                self.label_result.config(text='No operation selected')
        except ValueError:
            self.label_result.config(text='Enter numeric values')
        except ZeroDivisionError:
            self.label_result.config(text='Cant divide by zero')