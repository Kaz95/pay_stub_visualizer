# This is a program that allows a user to input pay stub data and returns visualized data via matplot library
import pprint

pay_stub_data = {}


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
    for i in range(2):
        append_paystub_data(i, get_paystub_data())

    pprint.pprint(pay_stub_data)
