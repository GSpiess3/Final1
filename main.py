from gui import *


def main():

    window = Tk()
    window.title('Final Part1')
    window.geometry('500x500')
    window.resizable(False, False)

    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()