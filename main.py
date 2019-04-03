# This is a program that allows a user to input pay stub data and returns visualized data via matplot library
import pprint

pay_stub_data = {}

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


def get_paystub_data():
    temp = {}
    print('Type Gross')
    gross = int(input())
    print('Type pre')
    pre_tax = int(input())
    print('Type withholding')
    tax_witholding = int(input())
    print('Type after')
    after_tax_deductions = int(input())
    print('Type home')
    take_home = int(input())

    temp['gross'] = gross
    temp['pre'] = pre_tax
    temp['withholding'] = tax_witholding
    temp['after'] = after_tax_deductions
    temp['home'] = take_home

    return temp


def append_paystub_data(month, some_dict):
    pay_stub_data[month] = some_dict


if __name__ == '__main__':
    months = DoublyLinkedList()
    months.push(1)
    for i in range(2, 13):
        months.append(i)

    month_node = months.head
    while month_node is not None:
        print(f'The month is {months_dictionary[month_node.data]}')
        append_paystub_data(month_node.data, get_paystub_data())
        month_node = month_node.next

    pprint.pprint(pay_stub_data)
