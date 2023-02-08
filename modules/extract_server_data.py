
def extract_server_data(img, N1, N2, n1, n2) :
    N1 = N1 - N1 % n1
    N2 = N2 - N2 % n2
    msg = ""
    length = ""

    count = 0
    i = 0
    j = 0
    len_count = 0

    while True :
        for p in range(0, n1) :
            for q in range(0, n2) :
                px = p + i
                py = q + j
                if (count < 32) :
                    length = length + str(img.getpixel((px, py)) & 1)
                count = count + 1
                if (count == 32) :
                    length = int(length, 2) - 32
                if (count > 32) :
                    if (length == len_count) :
                        break
                    x = img.getpixel((px, py))
                    msg = msg + str(x & 1)
                    len_count = len_count + 1

            if (length == len_count) :
                break 
        if (length == len_count) :
            break
        j = j + n2
        if (j == N2) :
            j = 0
            i = i + n1

    server_data = ""
    for i in range(0, len(msg), 8) :
        byte = int(msg[i : i + 8], 2)
        if (byte != 0) :
            server_data = server_data + chr(byte)

    return (server_data, length + 32)