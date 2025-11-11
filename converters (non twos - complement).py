def dec_to(value, base):
    biny = ""
    x = 1
    bits = 0
    z = 1
    while x <= value:
        x = x * base
        bits += 1
    x = x / base
    for bit in range(bits):
        if x > value:
            biny += "0"
            x = x / base
        else:
            y = x
            while y <= value:
                z += 1
                y = x * z
            z -= 1
            y = x * z
            biny += str(z)
            value -= y
            x = x / base
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
