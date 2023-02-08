from modules.functions import *
import math

def extract_data(img, len_lsb_a, N1, N2, n1, n2) :
    N1 = N1 - N1 % n1
    N2 = N2 - N2 % n2
    i = N1 - n1
    j = N2 - n2
    msg = ""
    fe = ""
    fe1 = ""
    fe2 = ""
    fe3 = ""
    LSBa = ""
    N = math.floor(N1/n1) * math.floor(N2/n2)
    count_fe = 0
    count_fe1 = 0
    count_fe2 = 0
    count_fe3 = 0
    max_fe = N
    max_fe1 = 0
    max_fe2 = 0
    max_fe3 = 0
    img_out = img.copy()

    while True :
        to_break = False
        for p in range(n1 - 1, -1, -1) :
            for q in range(n2 - 1, -1, -1) :
                px = p + i
                py = q + j
                if (p == n1 - 1 and q == n2 - 1) :
                    continue
                y = img.getpixel((px, py))
                
                if (count_fe < max_fe) :
                    fe = fe + str(y & 1)
                    count_fe = count_fe + 1
                    if (y & 1 == 1) :
                        max_fe1 = max_fe1 + 1
        
                elif (count_fe1 < max_fe1) :
                    fe1 = fe1 + str(y & 1)
                    
                    count_fe1 = count_fe1 + 1
                    if (y & 1 == 1) :
                        max_fe2 = max_fe2 + 1

                elif (count_fe2 < max_fe2) :
                    fe2 = fe2 + str(y & 1)
                    count_fe2 = count_fe2 + 1
                    if (y & 1 == 1) :
                        max_fe3 = max_fe3 + 1

                elif (count_fe3 < max_fe3) :
                    fe3 = fe3 + str(y & 1)
                    count_fe3 = count_fe3 + 1
                
                else :
                    to_break = True

        if (to_break) :
            break

        j = j - n2
        if (j < 0) :
            j = N2 - n2
            i = i - n1


    i = N1 - n1
    j = N2 - n2
    w = 0
    v = 0

    data1 = ""
    data2 = ""
    data3 = ""

    for z in range(0, len(fe1)) :
        h_array = []

        if (fe1[len(fe1) - z - 1] == '0') :
            k = 1
        elif (fe1[len(fe1) - z - 1] == '1' and fe2[len(fe2) - w - 1] == '0') :
            k = 2
            w = w + 1
        elif (fe1[len(fe1) - z - 1] == '1' and fe2[len(fe2) - w - 1] == '1' and fe3[len(fe3) - v - 1] == '0') :
            k = 3
            w = w + 1
            v = v + 1

        for p in range(0, n1) :
            for q in range(0, n2) :
                px = p + i
                py = q + j
                y = img.getpixel((px, py))
                h_array.append(h(y, pow(2, k)))

        avg = a(h_array)
        px = n1 + i - 1
        py = n2 + j - 1
        yn = img.getpixel((px, py))

        for p in range(n1 - 1, -1, -1) :
            for q in range(n2 - 1, -1, -1) :
                px = p + i
                py = q + j
                y = img.getpixel((px, py))
                if (p == n1 - 1 and q == n2 - 1) :
                    continue
                if (k == 1) :
                    data1 = data1 + str(y & 1)
                if (k == 2) :
                    data1 = data1 + str(y & 1)
                    data2 = data2 + str((y >> 1) & 1)
                if (k == 3) :
                    data1 = data1 + str(y & 1)
                    data2 = data2 + str((y >> 1) & 1)
                    data3 = data3 + str((y >> 2) & 1)

                x = h(y, pow(2, k)) + (pow(2, k) - 1) * avg + g(yn, pow(2, k))
                img_out.putpixel((px, py), x)
                
        j = j - n2
        if (j < 0) :
            j = N2 - n2
            i = i - n1
    
    msg = data1 + data2 + data3
    owner_data = ""
    fe = msg[0 : len(fe)]
    LSBa = msg[len(fe) + len(fe1) + len(fe2) + len(fe3) : len(fe) + len(fe1) + len(fe2) + len(fe3) + len_lsb_a]
    msg = msg[len(fe) + len(fe1) + len(fe2) + len(fe3) + len_lsb_a : ]
    for i in range(0, len(msg), 8) :
        byte = int(msg[i : i + 8], 2)
        if (byte != 0) :
            owner_data = owner_data + chr(byte)
    
    return (img_out, fe, fe1, fe2, fe3, LSBa, owner_data)