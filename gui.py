from tkinter import *


class MainWindow:
    def __init__(self, root):
        self.root = root

        self.input_frame = LabelFrame(root, text='Input')
        self.button_frame = Frame(root)

        self.month_label = Label(self.input_frame, text='Month Label')
        self.gross_label = Label(self.input_frame, text='Gross Pay: ')
        self.pre_tax_label = Label(self.input_frame, text='Pre-Tax Deductions: ')
        self.withholding_label = Label(self.input_frame, text='Tax Withholding: ')
        self.post_tax_label = Label(self.input_frame, text='Post-Tax Deductions: ')

        self.gross_input = Entry(self.input_frame)
        self.pre_tax_input = Entry(self.input_frame)
        self.withholding_input = Entry(self.input_frame)
        self.post_tax_input = Entry(self.input_frame)

        self.prev_button = Button(self.button_frame, text='Previous')
        self.next_button = Button(self.button_frame, text='Next', width=7)

        self.month_label.grid(row=0, columnspan=2)

        self.gross_label.grid(row=1, column=0)
        self.gross_input.grid(row=1, column=1)

        self.pre_tax_label.grid(row=2, column=0)
        self.pre_tax_input.grid(row=2, column=1)

        self.withholding_label.grid(row=3, column=0)
        self.withholding_input.grid(row=3, column=1)

        self.post_tax_label.grid(row=4, column=0)
        self.post_tax_input.grid(row=4, column=1)

        self.prev_button.grid(row=0, column=0)
        self.next_button.grid(row=0, column=1)

        self.input_frame.grid(row=0)
        self.button_frame.grid(row=1)



if __name__ == '__main__':
    main = Tk()
    MainWindow(main)
    main.mainloop()
