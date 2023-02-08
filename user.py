import math

from PIL import Image
from modules.reverse_rearrange import reverse_rearrange
from modules.put_lsb_a import put_lsb_a
from modules.extract_data import extract_data
from modules.encrypt_decrypt import decrypt_image
from modules.extract_server_data import extract_server_data

# take output image from server
img = Image.open(r"./server/img_output.png")

# block size. Must be same in owner.py server.py user.py
n1 = 4
n2 = 4
print("Blocks size: " + str(n1) + "x" + str(n2))

# image size
N1 = img.size[0]
N2 = img.size[1]
print("Image size: " + str(N1) + "x" + str(N2))

# number of pixels in a block
n = n1 * n2
print("Number of pixels in block: " + str(n))

# number of blocks in image
N = math.floor(N1/n1) * math.floor(N2/n2)
print("Number of blocks in image: " + str(N) + "\n")

# extracting server'data
print("\nExtracting server's data ...")
(server_data, len_lsb_a) = extract_server_data(img, N1, N2, n1, n2)
print("Server's data: " + server_data)

# decrypting the image using 8 bit key (0 - 255) 
# must be same as used by owner
decryption_key = 123
print("\nDecryption key: " + str(decryption_key))
print("Decrypting image ...")
img_decrypted = decrypt_image(img, decryption_key, N1, N2)

# extracting owner's data,
# LSB plane of class A blocks
# multilevel maps -> FE, FE1, FE2, FE3
print("\nExtracting owner's data ...")
(img_marked, FE, FE1, FE2, FE3, LSBa, owner_data) = extract_data(img_decrypted, len_lsb_a, N1, N2, n1, n2)
print("Owner's message: " + owner_data)

# recovering LSB plane of class A blocks
print("\nRecovering LSB planes of class A blocks ...")
img_rearranged = put_lsb_a(img_marked, LSBa, N1, N2, n1, n2)

# rearrange image back to get original image
print("\nRearranging image ...")
img_arranged = reverse_rearrange(img_rearranged, FE, N1, N2, n1, n2)

img_arranged.save(r"./user/img_recovered.png")
print("\nImage recovered saved at ./user/img_recovered.png")
