


def put_lsb_a(img, LSBa, N1, N2, n1, n2):
    N1 = N1 - N1 % n1
    N2 = N2 - N2 % n2
    i = 0
    j = 0
    img_out = img.copy()
    position = 0
    length = len(LSBa)
    
    while True :
        for p in range(0, n1) :
            for q in range(0, n2) :
                px = p + i
                py = q + j
                x = img.getpixel((px, py))
                if (position == length) :
                    break
                img_out.putpixel((px, py), ((x >> 1) << 1) + int(LSBa[position]))
                position = position + 1
        
        j = j + n2
        if (j == N2) :
            j = 0
            i = i + n1
            if (position == length) :
                break
    
    return img_out