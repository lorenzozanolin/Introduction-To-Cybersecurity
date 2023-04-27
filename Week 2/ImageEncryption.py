
import binascii

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter
from Crypto import Random


# read in image and extract header information so the encrypted image
# can be easily displayed
# note that this tux version has just the right size so padding is not necessary

# read in image: separate header from image data

f_in = open("tux_clear.bmp", 'rb')
# BMP is 14 bytes
bmpheader = f_in.read(14)
# DIB is 40 bytes
dibheader = f_in.read(40)

DIBheader = []
width = 0
height = 0
for i in range(0, 80, 2):
    DIBheader.append(int(binascii.hexlify(dibheader)[i:i + 2], 16))

width = sum([DIBheader[i + 4] * 256 ** i for i in range(0, 4)])
height = sum([DIBheader[i + 8] * 256 ** i for i in range(0, 4)])

# prepare ciphertext image(s)
f_ECB_out = open("tux_ECB_enc.bmp", 'wb')

# ECB mode does not incur any ciphertext expansion so the the header information does not need to change
f_ECB_out.write(bmpheader)
f_ECB_out.write(dibheader)

# now read in image data and close the image file
row_padded = (width * height * 3)
image_data = f_in.read(row_padded)
f_in.close()
msg = binascii.unhexlify(binascii.hexlify(image_data))


# set up the encryption box(es) and write to file
sk = get_random_bytes(16)


ECBBox = AES.new(sk, AES.MODE_ECB)
ECB_cipher = ECBBox.encrypt(msg)


f_ECB_out.write(ECB_cipher)
f_ECB_out.close()


