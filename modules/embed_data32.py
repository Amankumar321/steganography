
def embed_data32(data32, img, N1, N2, n1, n2) :
    N1 = N1 - N1 % n1
    N2 = N2 - N2 % n2
    i = 0
    j = 0
    count = 0

    while True :
        for p in range(0, n1) :
            for q in range(0, n2) :
                px = p + i
                py = q + j
                x = img.getpixel((px, py))
                temp = x if x % 2 == 0 else x - 1
                img.putpixel((px, py), temp + int(data32[count], 2))
                count = count + 1
                if (count == 32) :
                    break
            if (count == 32) :
                break
        
        j = j + n2
        if (j == N2) :
            j = 0
            i = i + n1
        if (count == 32) :
            break

    return img