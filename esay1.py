from sense_hat import SenseHat()
s = SenseHat()

def decimal_to_binary_list(decimal_number):
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
    return binary_list
def main():
    col = {
    "ON" : [255, 255, 255],
    "OFF" : [0, 0, 0],
    "R" : [255, 0, 0],
    "G" : [0, 255, 0],
    "B" : [0, 0, 255]
    }
    num = int(input())
    bin_l = decimal_to_binary_list(num)
    for x in range(8):
        if bin_l[x] == 1:
            s.set_pixel(x, 0, col["ON"])
        else:
            s.set_pixel(x, 0, col["OFF"])
    print(f"Displaying: {num}")
