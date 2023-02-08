def embed_server_data(img, bin_msg, N1, N2, n1, n2) :
    N1 = N1 - N1 % n1
    N2 = N2 - N2 % n2
    length = ""
    msg_pos = 0

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
                    bit = bin_msg[msg_pos] if (msg_pos < len(bin_msg)) else '0'
                    x = img.getpixel((px, py))
                    temp = x if x % 2 == 0 else x - 1
                    img.putpixel((px, py), temp + int(bit, 2))
                    len_count = len_count + 1
                    msg_pos = msg_pos + 1

            if (length == len_count) :
                break 
        if (length == len_count) :
            break
        j = j + n2
        if (j == N2) :
            j = 0
            i = i + n1
    return img