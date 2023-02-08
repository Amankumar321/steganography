from PIL import Image
import math

from modules.partition import partition
from modules.rearrange import rearrange
from modules.adaptive_git import adaptive_git
from modules.get_lsb_a import get_lsb_a
from modules.embed_data import embed_data
from modules.encrypt_decrypt import encrypt_image
from modules.embed_data32 import embed_data32
from modules.reverse_rearrange import reverse_rearrange

# take the input image
img = Image.open(r"./owner/img_input.png")

# block size. Must be same in owner.py server.py user.py
n1 = 4
n2 = 4
print("Blocks size: " + str(n1) + "x" + str(n2))

# image size
N1 = img.size[0]
N2 = img.size[1]
print("Image size: " + str(N1) + "x" + str(N2))

# number of pixels in block
n = n1 * n2
print("Number of pixels in block: " + str(n))

# number of blocks in image
N = math.floor(N1/n1) * math.floor(N2/n2)
print("Number of blocks in image: " + str(N) + "\n")

# start coordinates of class B blocks
start_FE_i = 0
start_FE_j = 0

# threshold
# change to increase or decrease number of blocks in class A and B
T = 1000

# owner's message
message = "im owner"
bin_message = ''.join(format(ord(i), '08b') for i in message)
print("Owner's message: " + message)
print("Owner's message in binary: " + bin_message)

# partition image in class A and class B
# set FE -> first level embedding map
print("\nPartitioning image ...")
FE = partition(img, N1, N2, n1, n2, T)

# rearrage image according to class A and B
print("\nRearranging image ...")
(start_FE_i, start_FE_j, img_rearranged) = rearrange(img, FE, N1, N2, n1, n2)
img_rearranged.save(r"./owner/img_rearranged.png")
if (start_FE_i >= N1 or start_FE_j >= N2) :
    print("\nError: Not enough class B blocks. Decrease block size.")
    exit(0)

# adaptive GIT to select number of LSB bits to be embedded in each block of class B
# set FE1, FE2, FE3 maps
print("\nGenerating multilevel mapping ( FE1, FE2, FE3 ) ...")
(FE1, FE2, FE3, max_data) = adaptive_git(img_rearranged, start_FE_i, start_FE_j, N1, N2, n1, n2, T)

# LSB string of class A blocks
# data32 -> number of bits to be embedded in class A blocks as binary string
LSBa = ""
data32 = ""

# free space in class B blocks represented as number of bits
free_length = max_data - (len(FE) + len(FE1) + len(FE2) + len(FE3) + len(bin_message))
data32 = '{:032b}'.format(free_length)
print("\nMaximum free length in bits for server data: " + str(free_length))

if (free_length < 32) :
    print("\nError: Not enough embedding capacity. Change block size")
    exit(0)

# get LSB plane of class A blocks upto free length
print("\nGetting LSB plane of class A block ...")
LSBa = get_lsb_a(img_rearranged, free_length, N1, N2, n1, n2)

# total data to be stored in class B blocks
owner_data = FE + FE1 + FE2 + FE3 + LSBa + bin_message
print("\nOwner's data length: " + str(len(owner_data)))

if (len(FE1) * (n - 1) < (len(FE) + len(FE1) + len(FE2) + len(FE3))) :
    print("Number of LSB bits: " + str(len(FE1) * (n - 1)))
    print(("Miniumum LSB bits required: " + str(len(FE) + len(FE1) + len(FE2) + len(FE3))))
    print("\nError: Not enough class B blocks. Change block size.")
    exit(0)

# img_marked -> image after embedding owner's data
print("Embedding owner's data ...")
img_marked = embed_data(img_rearranged, owner_data, FE, FE1, FE2, FE3, N1, N2, n1, n2)

# img_no_rearrangement -> image without rearrangement for sample
img_no_rearrangement = reverse_rearrange(img_marked, FE, N1, N2, n1, n2)
img_no_rearrangement.save(r"./owner/img_no_rearrangement.png")

# encrypting the image using 8 bit key (0 - 255) 
encryption_key = 123
print("\nEncryption key: " + str(encryption_key))
print("Encrypting image ...")
img_encrypted = encrypt_image(img_marked, encryption_key, N1, N2)

# embedding 32 bit data in encrypted image that represents number of bit server can embed
print("\n32 bit data for server: " + data32)
print("Embedding 32 bit data ...")
img_encrypted = embed_data32(data32, img_encrypted, N1, N2, n1, n2)

img_encrypted.save(r"./owner/img_encrypted.png")
print("\nImage to be sent to server saved at ./owner/img_encrypted.png")