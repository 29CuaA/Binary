from sense_hat import SenseHat
from random import randint
from time import sleep

def adtb(value):
    biny = ""
    x = 1
    bits = 0
    while x <= value:
        x = x * 2
        bits += 1
    x = x/2
    for bit in range(bits):
        if x > value:
            biny += "0"
            x = x / 2
        else:
            biny += "1"
            value -= x
            x = x / 2
    while len(biny) < 8:
        biny = "0" + biny
    return biny

def abtd(value):
    value = str(value)
    bits = len(value)
    x = 2 ** (bits-1)
    deci = 0
    for bit in range(bits):
        if value[bit] == "1":
            deci += x
            x = x / 2
        else:
            x = x / 2
    return int(deci)

def asdttc(num, bits):
    pv = [1]
    a = 1
    for i in range(bits - 1):
        a *= 2
        pv.append(a)
    place_values = pv
    bi = ''
    if num > 0:
        for i in range(len(place_values) - 1, -1, -1):
            if num >= place_values[i]:
                bi = bi + '1'
                num -= place_values[i]
            else:
                bi = bi + '0'
    else:
        bi = '1'
        num = num + place_values[len(place_values) - 1]
        for i in range(len(place_values) - 2, -1, -1):
            if num >= place_values[i]:
                bi = bi + '1'
                num -= place_values[i]
            else:
                bi = bi + '0'
    return bi
   
def adth(dec):
    ct = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    h = ''
    while(dec > 0):
        r = dec % 16
        h = ct[r] + h
        dec //= 16
    return h





def easy1():
    print("Enter a decimal number between 0 and 255 to display:")
    decimal_number = int(input())
    if decimal_number == 0:
        return [0, 0, 0, 0, 0, 0, 0, 0]
    binary_list = []
    num = decimal_number 
    while num > 0:
        remainder = num % 2
        binary_list.insert(0, remainder)
        num = num // 2
    while len(binary_list) < 8:
        binary_list.insert(0, 0)
    
    # display
    for x in range(8):
        if binary_list[x] == 1:
            s.set_pixel(x, 0, col["ON"])
        else:
            s.set_pixel(x, 0, col["OFF"])
    print(f"Displaying: {num}")

def easy2():
    num = randint(0, 255)
    ans = adtc(num)
    print(f"Enter the 8 bit binary of the number {num}")
    user_answer = input()
    
    #display
    for x in range(8):
        if ans[x] == 1:
            s.set_pixel(x, 0, col["ON"])
        else:
            s.set_pixel(x, 0, col["OFF"])
        if user_answer[x] == 1:
            s.set_pixel(x, 1, col["B"])
        else:
            s.set_pixel(x, 1, col["OFF"])
    sleep(2)
    if ans == user_answer:
        for x in range(8):
            if user_answer[x] == ans[x]:
                s.set_pixel(x, 1, col["G"])
            else:
                s.set_pixel(x, 1, col["R"])
        print("Completely correct")

def medium3():
    

def main():
    s = SenseHat()
    col = {
    "ON": [255, 255, 255],
    "OFF": [0, 0, 0],
    "R": [255, 0, 0],
    "G": [0, 255, 0],
    "B": [0, 0, 255]
    }
