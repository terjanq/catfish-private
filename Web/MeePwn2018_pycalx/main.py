#!/usr/bin/env python
import code 
import cgi;
import sys
from html import escape

FLAG =  'MeePwnCTF{welcome_to_meepwnctf_2018}' # open('/var/www/flag','r').read()


def crackme(value1, op, value2):



    def get_value(val):
        val = str(val)[:64]
        if str(val).isdigit(): return int(val)
        blacklist = ['(',')','[',']','\'','"'] # I don't like tuple, list and dict.
        if val == '' or [c for c in blacklist if c in val] != []:
            print('Invalid value:' + val)
            sys.exit(0)
        return val

    def get_op(val):
        val = str(val)[:2]
        list_ops = ['+','-','/','*','=','!']
        if val == '' or val[0] not in list_ops:
            print('<center>Invalid op</center>')
            sys.exit(0)
        return val

    # op = get_op(arguments['op'].value)
    # value1 = get_value(arguments['value1'].value)
    # value2 = get_value(arguments['value2'].value)

    value1 = get_value(value1)
    op = get_op(op)
    value2 = get_value(value2)

    print(value1)
    print(op)
    print(value2)

    if str(value1).isdigit() ^ str(value2).isdigit():
        print('Types of the values don\'t match:')
        print("val1: " + str(value1))
        print("val2: " + str(value2))
        sys.exit(0)

    calc_eval = str(repr(value1)) + str(op) + str(repr(value2))

    print("DEBUG:")
    print(calc_eval)
    # print('<div class=container><div class=row><div class=col-md-2></div><div class="col-md-8"><pre>')
    print('>>>> print('+(calc_eval)+')')

    try:
        result = str(eval(calc_eval))
        if result.isdigit() or result == 'True' or result == 'False':
            print(result)
        else:
            print("Invalid but printing") # Sorry we don't support output as a string due to security issue.
            print(result)
    except:
        print("Invalid <exception>")

# code.interact(local=locals())
input1 = input();
op = input();
input2 = input();

crackme(input1, op, input2);