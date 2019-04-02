from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

import matplotlib.pyplot as plt
sizes = []


class MainWindow:
    def __init__(self, root):
        self.root = root

    def clear(self):
        for widget in self.root.grid_slaves():
            widget.grid_forget()


class InputWindow(MainWindow):
    def __init__(self, root):

        MainWindow.__init__(self, root)
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

        self.prev_button = Button(self.button_frame, text='<--', width=7)
        self.next_button = Button(self.button_frame, text='-->', width=7, command=self.next_command)

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

        self.gross = None
        self.pre_tax = None
        self.withholding = None
        self.post_tax = None
        self.take_home = None

    def next_command(self):
        self.get_entrys()
        self.get_take_home_pay()
        self.append_sizes()
        print(sizes)
        OutputWindow(self.root, )

    def get_take_home_pay(self):

        deductions = self.pre_tax + self.withholding + self.post_tax
        take_home = self.gross - deductions
        self.take_home = take_home

    def convert_to_percent(self, some_slice_value):
        float_value = some_slice_value / self.gross
        percent = round((float_value * 100), 1)
        return percent

    def append_sizes(self):
        take_home_percent = self.convert_to_percent(self.take_home)
        pre_tax_percent = self.convert_to_percent(self.pre_tax)
        withholding_percent = self.convert_to_percent(self.withholding)
        post_tax_percent = self.convert_to_percent(self.post_tax)

        sizes.append(take_home_percent)
        sizes.append(pre_tax_percent)
        sizes.append(withholding_percent)
        sizes.append(post_tax_percent)

    def get_entrys(self):
        self.gross = int(self.gross_input.get())
        self.pre_tax = int(self.pre_tax_input.get())
        self.withholding = int(self.withholding_input.get())
        self.post_tax = int(self.post_tax_input.get())


class OutputWindow(MainWindow):
    def __init__(self, root):
        MainWindow.__init__(self, root)
        print(sizes)
        self.clear()
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:

        # Outer labels for each slice
        labels = ['Take Home', 'Pre', 'Withheld', 'Post']
        # Percentages as integers. Dictate size of each slice
        # sizes = [15, 33.5, 45, 6.5]

        # 0 Means no 'explode' of emphasis on a given slice. Higher the number, greater the offset
        explode = [0.1, 0, 0, 0]

        fig1 = plt.figure(figsize=(12, 5))
        # TODO: I need to cement my understanding of subplots.
        # fig1, ax1 = plt.subplots(figsize=(12, 5))

        # Declaring my pie plot
        # pie_chart = plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
        pie_chart = plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)

        # Ensures pie is drawn as circle
        plt.axis('equal')

        # First two params position, third is the content, bbox= is an option keyword arg that gives text a border.
        plt.text(2, 1, 'Ima String: Ima number', bbox=dict(facecolor='red', alpha=0.5))
        # Opens the plot I've been drawing in the background up until this point
        # plt.show()

        canvas = FigureCanvasTkAgg(fig1, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().grid(sticky=W+E+S+N)


if __name__ == '__main__':
    main = Tk()
    InputWindow(main)
    main.mainloop()
