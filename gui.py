from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

import matplotlib.pyplot as plt


# This is a program that allows a user to input pay stub data and returns visualized data via matplot library
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def append(self, new_val):
        if self.head is not None:
            if self.tail is not None:
                new_node = Node(new_val)
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            else:
                self.tail = Node(new_val)
                self.tail.prev = self.head
                self.head.next = self.tail

        else:
            self.head = Node(new_val)


# pay_stub_data = {}
gross = {}
pre = {}
withheld = {}
post = {}
take_home = {}

total_gross = None
total_pre = None
total_withheld = None
total_post = None
total_take_home = None

months_dictionary = {1: 'Jan.',
                     2: 'Feb.',
                     3: 'Mar.',
                     4: 'Apr.',
                     5: 'May',
                     6: 'Jun.',
                     7: 'Jul.',
                     8: 'Aug.',
                     9: 'Sep.',
                     10: 'Oct.',
                     11: 'Nov.',
                     12: 'Dec.', }

sizes = []


# def append_paystub_data(month, some_dict):
#     pay_stub_data[month] = some_dict


def get_total(some_dict):
    count = 0
    for value in some_dict.values():
        count += value

    return count


class MainWindow:
    def __init__(self, root):
        self.root = root

    def clear(self):
        for widget in self.root.grid_slaves():
            widget.grid_forget()


class InputWindow(MainWindow):
    def __init__(self, root):

        self.months = DoublyLinkedList()
        self.months.push(1)
        for i in range(2, 13):
            self.months.append(i)

        self.month_node = self.months.head

        MainWindow.__init__(self, root)
        self.input_frame = LabelFrame(root, text='Input')
        self.button_frame = Frame(root)

        self.month_label = Label(self.input_frame, text=months_dictionary[self.month_node.data])
        self.gross_label = Label(self.input_frame, text='Gross Pay: ')
        self.pre_tax_label = Label(self.input_frame, text='Pre-Tax Deductions: ')
        self.withholding_label = Label(self.input_frame, text='Tax Withholding: ')
        self.post_tax_label = Label(self.input_frame, text='Post-Tax Deductions: ')

        self.gross_input = Entry(self.input_frame)
        self.pre_tax_input = Entry(self.input_frame)
        self.withholding_input = Entry(self.input_frame)
        self.post_tax_input = Entry(self.input_frame)

        self.prev_button = Button(self.button_frame, text='<--', width=7, command=self.prev_command)
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

        self.total_gross = None
        self.total_pre_tax = None
        self.total_withholding = None
        self.total_post_tax = None
        self.total_take_home = None

    def next_command(self):
        global total_gross
        global total_pre
        global total_withheld
        global total_post
        global total_take_home
        self.get_entrys()
        self.get_take_home_pay()
        self.format_dictionary()
        # self.append_sizes()
        # OutputWindow(self.root)
        # pprint.pprint(pay_stub_data)
        if self.month_node.next is not None:
            self.month_node = self.month_node.next
            self.month_label.configure(text=months_dictionary[self.month_node.data])
            self.root.update()
        else:
            self.total_gross = get_total(gross)
            self.total_pre_tax = get_total(pre)
            self.total_withholding = get_total(withheld)
            self.total_post_tax = get_total(post)
            self.total_take_home = get_total(take_home)

            total_gross = self.total_gross
            total_pre = self.total_pre_tax
            total_withheld = self.total_withholding
            total_post = self.total_post_tax
            total_take_home = self.total_take_home

            self.append_sizes()
            OutputWindow(self.root)

    def prev_command(self):
        if self.month_node.prev is not None:
            self.month_node = self.month_node.prev
            self.month_label.configure(text=months_dictionary[self.month_node.data])
            self.root.update()

    def format_dictionary(self):
        gross[self.month_node.data] = self.gross
        pre[self.month_node.data] = self.pre_tax
        withheld[self.month_node.data] = self.withholding
        post[self.month_node.data] = self.post_tax
        take_home[self.month_node.data] = self.take_home

    # def next_command(self):
    #     self.get_entrys()
    #     self.get_take_home_pay()
    #     self.append_sizes()
    #     print(sizes)
    #     OutputWindow(self.root)

    def get_take_home_pay(self):
        deductions = self.pre_tax + self.withholding + self.post_tax
        take_home = self.gross - deductions
        self.take_home = take_home

    def convert_to_percent(self, some_slice_value):
        float_value = some_slice_value / self.gross
        percent = round((float_value * 100), 1)
        return percent

    def append_sizes(self):
        take_home_percent = self.convert_to_percent(self.total_take_home)
        pre_tax_percent = self.convert_to_percent(self.total_pre_tax)
        withholding_percent = self.convert_to_percent(self.total_withholding)
        post_tax_percent = self.convert_to_percent(self.total_post_tax)

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

        string_output = f'Totals:\nGross: ${total_gross}\nPre-Tax: ${total_pre}\nTax-Withholding: ${total_withheld}\nPost-Tax: ${total_post}\nTake-Home: ${total_take_home}'

        # First two params position, third is the content, bbox= is an option keyword arg that gives text a border.
        plt.text(2, 1, string_output, bbox=dict(facecolor='red', alpha=0.5))
        # Opens the plot I've been drawing in the background up until this point
        # plt.show()

        canvas = FigureCanvasTkAgg(fig1, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, sticky=W+E+S+N)
        button = Button(text='Quit', command=self.close)
        button.grid(row=1)

    # TODO: Threads do not close properly without this. Bind to close event.
    def close(self):
        self.root.quit()  # stops mainloop
        self.root.destroy()  # this is necessary on Windows to prevent
        # Fatal Python Error: PyEval_RestoreThread: NULL tstate


if __name__ == '__main__':
    main = Tk()
    InputWindow(main)
    main.mainloop()
