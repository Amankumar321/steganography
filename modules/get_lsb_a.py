

def get_lsb_a(img, length, N1, N2, n1, n2):
    N1 = N1 - N1 % n1
    N2 = N2 - N2 % n2
    i = 0
    j = 0
    count = 0
    LSBa = ""
    
    while True :
        for p in range(0, n1) :
            for q in range(0, n2) :
                px = p + i
                py = q + j
                x = img.getpixel((px, py))
                LSBa = LSBa + str(x & 1)
                count = count + 1
                if (count == length) :
                    break
            if (count == length) :
                break
        
        j = j + n2
        if (j == N2) :
            j = 0
            i = i + n1
        if (count == length) :
            break
    
    return LSBa