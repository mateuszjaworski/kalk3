#!/usr/bin/python3
#-*- coding: utf-8-*-
# Nazwa pliku: kalkulator.py

import sys
print("....:::::KALKULATOR::::....")
def add(x, y):             # definiujemy dzialania matematyczne
    return x + y
def sub(x, y):
    return x - y
def mult(x, y):
    return x * y
def div(x, y):
    return x / y
program = True
sign = 0
while program:            # troche jak z zielona flaga w scratchu
    try:
        first = int(eval(input("  Write first number (or letter to exit):"))) # wprowdzamy pierwsza liczbe dzialania
    except:
        break            # w przypadku wpisania litery
    sign = input("  Write sign (+ or - or / or *) between:")
    try:
        second = int(eval(input("  Write second number:"))) #wprowadzamy druga liczbe dzialania
    except:
        print("Wrong number, try again")            # w przypadku wpisania czegos innego niz liczba
        try:
            second = int(eval(input("  Write second number:")))
        except:
            break
    if sign == ("*"):                               # no i dzialania przypisane do kazdego ze znakow, ktore mamy mozliwosc wprowadzic
        print("   Result:", mult(first, second))    # pewnie sporo osob zrobilo to na zasadzie menu
    if sign == ("+"):                               # ja wolalem zrobic wg wytycznych
        print("   Result:", add(first, second))
    if sign == ("-"):
        print("   Result:", sub(first, second))
    if sign == ("/"):
        print("   Result:", div(first, second))
    if sign not in ("+", "-", "/", "*"):
        print("Wrong sign, try again!")
