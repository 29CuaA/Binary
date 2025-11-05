def gen_pv(bits):
    pv = [1]
    a = 1
    for i in range(bits - 1):
        a *= 2
        pv.append(a)
    return pv

def twos_complement(num, bits):
    place_values = gen_pv(bits)
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




num = int(input("Number: "))
print(twos_complement(num, 8))
