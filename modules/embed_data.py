from modules.functions import *
import math

def embed_data(img, dataS, fe, fe1, fe2, fe3, N1, N2, n1, n2) :
    N1 = N1 - N1 % n1
    N2 = N2 - N2 % n2
    i = N1 - n1
    j = N2 - n2
    n = n1 * n2
    img_out = img.copy()
    w = 0
    v = 0
    c1 = 0
    c2 = 0
    c3 = 0

    for z in range(0, len(fe1)) :
        pixels = []

        for p in range(0, n1) :
            for q in range(0, n2) :
                px = p + i
                py = q + j
                x = img.getpixel((px, py))
                pixels.append(x)

        avg = a(pixels)
        px = n1 + i - 1
        py = n2 + j - 1
        xn = img.getpixel((px, py))
        if (fe1[len(fe1) - z - 1] == '0') :
            k = 1
            yn = pow(2, 1) * xn - (pow(2, 1) - 1) * avg
        elif (fe1[len(fe1) - z - 1] == '1' and fe2[len(fe2) - w - 1] == '0') :
            k = 2
            w = w + 1
            yn = pow(2, 2) * xn - (pow(2, 2) - 1) * avg
        elif (fe1[len(fe1) - z - 1] == '1' and fe2[len(fe2) - w - 1] == '1' and fe3[len(fe3) - v - 1] == '0') :
            k = 3
            v = v + 1
            w = w + 1
            yn = pow(2, 3) * xn - (pow(2, 3) - 1) * avg

        for p in range(n1 - 1, -1, -1) :
            for q in range(n2 - 1, -1, -1) :
                if (p == n1 - 1 and q == n2 - 1) :
                    continue
                px = p + i
                py = q + j
                x = img.getpixel((px, py))
                
                if (k == 1) :
                    bits = dataS[c1] if (c1 < len(dataS)) else '0'
                    c1 = c1 + 1

                elif (k == 2) :
                    bits = dataS[c1] if (c1 < len(dataS)) else '0'
                    pos = len(fe1) * (n - 1) + c2
                    bits = (dataS[pos] if (pos < len(dataS)) else '0') + bits
                    c1 = c1 + 1
                    c2 = c2 + 1

                elif (k == 3) :
                    bits = dataS[c1] if (c1 < len(dataS)) else '0'
                    pos1 = len(fe1) * (n - 1) + c2
                    bits = (dataS[pos1] if (pos1 < len(dataS)) else '0') + bits
                    pos2 = len(fe1) * (n - 1) + len(fe2) * (n - 1) + c3
                    bits = (dataS[pos2] if (pos2 < len(dataS)) else '0') + bits
                    c1 = c1 + 1
                    c2 = c2 + 1
                    c3 = c3 + 1

                y = pow(2, k) * x - pow(2, k) * f(avg, pow(2, k)) + int(bits, 2)
                img_out.putpixel((px, py), y)

        px = n1 + i - 1
        py = n2 + j - 1
        img_out.putpixel((px, py), yn)
        

        j = j - n2
        if (j < 0) :
            j = N2 - n2
            i = i - n1

    return img_out