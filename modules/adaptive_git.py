from modules.functions import *

def adaptive_git(img, start_fe_i, start_fe_j, N1, N2, n1, n2, T) :
    N1 = N1 - N1 % n1
    N2 = N2 - N2 % n2
    i3 = start_fe_i
    j3 = start_fe_j
    n = n1 * n2
    count = 0
    fe1 = ""
    fe2 = ""
    fe3 = ""

    while True :
        pixels = []
        for p in range(0, n1) :
            for q in range(0, n2) :
                px = p + i3
                py = q + j3
                x = img.getpixel((px, py))
                pixels.append(x)
        
        avg = a(pixels)
        px = n1 + i3 - 1
        py = n2 + j3 - 1
        xn = img.getpixel((px, py))
        yn3 = pow(2, 3) * xn - (pow(2, 3) - 1) * avg
        yn2 = pow(2, 2) * xn - (pow(2, 2) - 1) * avg

        sse_temp = sse(pixels)
        if (sse_temp <= T/49) :
            if (Cm(pixels, 3, avg, yn3) == True) :
                fe1 = fe1 + "1"
                fe2 = fe2 + "1"
                fe3 = fe3 + "0"
                count = count + 3 * (n - 1)
            elif (Cm(pixels, 2, avg, yn2) == True) :
                fe1 = fe1 + "1"
                fe2 = fe2 + "0"
                count = count + 2 * (n - 1)
            else :
                fe1 = fe1 + "0"
                count = count + 1 * (n - 1)
        elif (sse_temp <= T/9) :
            if (Cm(pixels, 2, avg, yn2) == True) :
                fe1 = fe1 + "1"
                fe2 = fe2 + "0"
                count = count + 2 * (n - 1)
            else :
                fe1 = fe1 + "0"
                count = count + 1 * (n - 1)
        else :
            fe1 = fe1 + "0"
            count = count + 1 * (n - 1)

        j3 = j3 + n2
        if (j3 == N2) :
            j3 = 0
            i3 = i3 + n1
        if (i3 >= N1) :
            break
    
    return (fe1, fe2, fe3, count)
    