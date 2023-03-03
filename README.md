# Requirement #

1. Python version 3.x
2. PIL package. To install use - ```pip3 install Pillow```


# Input #
    ./owner/img_input.png

# Output #
    printed on console and ./user/img_recovered.png

# Basic steps (Run all in order) #

1. ```python3 owner.py```
2. ```python3 server.py```
3. ```python3 user.py```


# Detailed steps #

1. python3 owner.py
    - takes input image at ./owner/img_input.png
    - creates intermediate ./owner/img_no_rearrangement.png and ./owner/img_rearranged.png
    - creates output ./owner/img_encrypted.png

Owner takes an input image and embeds data and encrypts it before sending it to server

2. python3 server.py
    - takes input image at ./owner/encrypted.png
    - creates output ./server/img_output.png

Server takes encrypted image from owner and embeds its own data and sends it to user

2. python3 user.py
    - takes input image at ./server/img_output.png
    - creates output ./user/img_recovered.png

Users extracts data and decrypts image and recovers the original image back


# Instructions #

1. owner.py, server.py and user.py must have same block size variables
2. Steps must be executed in order because output of one file is input to other
3. Our input image is ./owner directory/img_input.png inside which we want to embed data
4. All other images are created during execution of program
5. Owner's message can be changed in owner.py with variable "message"
5. Server's message can be changed in server.py with variable "data"

# About paper #

Reversible Data Hiding in Encrypted Images With Dual Data Embedding
https://ieeexplore.ieee.org/document/8968332
