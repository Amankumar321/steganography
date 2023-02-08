import math


def reverse_rearrange(img, fe, N1, N2, n1, n2) :
    N1 = N1 - N1 % n1
    N2 = N2 - N2 % n2
    x = 0
    y = 0
    i3 = 0
    j3 = 0
    fe_pos = 0
    x4 = 0
    y4 = 0
    count = 0
    img_out = img.copy()

    for i in range(0, N1, n1) :
        for j in range(0, N2, n2):
            if (fe[fe_pos] == '0') :
                j3 = j3 + n2
                if (j3 == N2) :
                    j3 = 0
                    i3 = i3 + n1
            fe_pos = fe_pos + 1

    start_fe_i = i3
    start_fe_j = j3
    fe_i = start_fe_i
    fe_j = start_fe_j

    for i in range(0, math.floor(N1/n1)) :
        for j in range(0, math.floor(N2/n2)) :
            if (fe[count] == '1') :
                for z in range(0, n1) :
                    for k in range(0, n2) :   
                        px = z + x4
                        py = k + y4
                        img_out.putpixel((px, py), img.getpixel((fe_i + z, fe_j + k)))
                fe_j = fe_j + n2
                if (fe_j >= N2) :
                    fe_j = 0
                    fe_i = fe_i + n1
            else :
                for z in range(0, n1) :
                    for k in range(0, n2) :
                        px = z + x4
                        py = k + y4
                        img_out.putpixel((px, py), img.getpixel((x + z, y + k)))
                        
                y = y + n2
                if (y >= N2) :
                    y = 0
                    x = x + n1
            
            y4 = y4 + n2
            if (y4 >= N2) :
                y4 = 0
                x4 = x4 + n1
            count = count + 1
    return img_out