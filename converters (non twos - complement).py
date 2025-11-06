def dec_to_bin(value):
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
    return biny

def bin_to_dec(value):
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
