def encrypt_image(img, key, N1, N2) :
    img_out = img.copy()

    for i in range(0, N1) :
        for j in range(0, N2) :
            plain = img.getpixel((i, j))
            cipher = plain ^ key
            img_out.putpixel((i, j), cipher)
    
    return img_out




def decrypt_image(img, key, N1, N2) :
    img_out = img.copy()

    for i in range(0, N1) :
        for j in range(0, N2) :
            cipher = img.getpixel((i, j))
            plain = cipher ^ key
            img_out.putpixel((i, j), plain)
    
    return img_out
