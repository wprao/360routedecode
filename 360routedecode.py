# coding:utf-8
import requests
from Crypto.Cipher import AES
from pkcs7 import PKCS7Encoder
from binascii import b2a_hex, a2b_hex
import base64

rand_key =  '708501d193ff76cc445b54fe9552716ed3504e098763b3d7189e71eba6c4e24d'
pass_word = '708501d193ff76cc445b54fe9552716e4263e71bc923a6a4a37f3544ac453285'
#real password = '12345678'
#从密码生成pass码
def EnAES(key):
    mode = AES.MODE_CBC
    iv = '\x33\x36\x30\x6c\x75\x79\x6f\x75\x40\x69\x6e\x73\x74\x61\x6c\x6c' #"360luyou@install".decode('hex')
    encryptor = AES.new(key, mode, iv.encode('utf-8'))
    encoder = PKCS7Encoder()
    text = '12345678' # password
    pad_text = encoder.encode(text)
    a = pad_text
    print(a)
    cipher = encryptor.encrypt(a.encode('utf-8'))
    return(b2a_hex(cipher))#b2a_hex 字节串转16进制表示,固定两个字符表示: str(binascii.b2a_hex(b'\x01\x0212'))[2:-1]  ==>  01023132

temp = rand_key[32:]
aes_key = a2b_hex(temp)

data = EnAES(aes_key)
print('加密：'+rand_key[:32]+data.decode())

print('\n真实：'+pass_word)




#从密码和pass码生成密码
def DeCode(key,p):
    mode = AES.MODE_CBC
    iv = '\x33\x36\x30\x6c\x75\x79\x6f\x75\x40\x69\x6e\x73\x74\x61\x6c\x6c' #"360luyou@install".decode('hex')
    decryptor = AES.new(key, mode, iv.encode('utf-8'))
    plain_text =decryptor.decrypt(p)
    temp = str(plain_text, encoding = "utf8")
    return(temp.rstrip(temp[-1]))  #截取补位的字符。


rand_key = '708501d193ff76cc445b54fe9552716ed3504e098763b3d7189e71eba6c4e24d'
pass_word = '708501d193ff76cc445b54fe9552716e4263e71bc923a6a4a37f3544ac453285'

aes_key = a2b_hex(rand_key[32:])
aes_p = a2b_hex(pass_word[32:])
data = DeCode(aes_key,aes_p)
print('密码：'+ data)
