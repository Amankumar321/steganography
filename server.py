from PIL import Image
import math

from modules.embed_server_data import embed_server_data

# taking encrypted image from owner
img = Image.open(r"./owner/img_encrypted.png")

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

# server's data
data = "im server"
bin_data = ''.join(format(ord(i), '08b') for i in data)
print("Server's data: " + data)
print("Server's data in binary: " + bin_data)
print("Server's data length: " + str(len(bin_data)))
print("\nEmbedding server's data ...")
img = embed_server_data(img, bin_data, N1, N2, n1, n2)

img.save(r"./server/img_output.png")
print("\nImage to be sent to user saved at ./server/img_output.png")
