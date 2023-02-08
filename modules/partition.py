from modules.functions import a, Cm, sse

def partition(img, N1, N2, n1, n2, T) :
    N1 = N1 - N1 % n1
    N2 = N2 - N2 % n2
    k = 1
    FE = ""

    for i in range(0, N1, n1) :
        for j in range(0, N2, n2):
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
            yn = pow(2, k) * xn - (pow(2, k) - 1) * avg

            if (sse(pixels) <= T) :
                if (Cm(pixels, 1, avg, yn) == True) :
                    FE = FE + "1"
                else :
                    FE = FE + "0"
            else :
                FE = FE + "0"
    
    return FE
