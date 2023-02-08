
def rearrange(img, fe, N1, N2, n1, n2) :
    N1 = N1 - N1 % n1
    N2 = N2 - N2 % n2
    i3 = 0
    j3 = 0
    fe_pos = 0
    rearranged_image = img.copy()
    start_fe_i = 0
    start_fe_j = 0
    
    for i in range(0, N1, n1) :
        for j in range(0, N2, n2):
            if (fe[fe_pos] == '0') :
                for p in range(0, n1) :
                    for q in range(0, n2) :
                        px = p + i
                        py = q + j
                        g = img.getpixel((px, py))
                        rearranged_image.putpixel((i3 + p, j3 + q), g)
                j3 = j3 + n2
                if (j3 == N2) :
                    j3 = 0
                    i3 = i3 + n1
            fe_pos = fe_pos + 1

    start_fe_i = i3
    start_fe_j = j3

    fe_pos = 0

    for i in range(0, N1, n1) :
        for j in range(0, N2, n2):
            if (fe[fe_pos] == '1') :
                for p in range(0, n1) :
                    for q in range(0, n2) :
                        px = p + i
                        py = q + j
                        g = img.getpixel((px, py))
                        rearranged_image.putpixel((i3 + p, j3 + q), g)
                j3 = j3 + n2
                if (j3 == N2) :
                    j3 = 0
                    i3 = i3 + n1
            fe_pos = fe_pos + 1
    
    return (start_fe_i, start_fe_j, rearranged_image)