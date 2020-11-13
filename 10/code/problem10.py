from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from math import ceil
import random
from random import randint
import os
backend = default_backend()

def pkcs_padding(message, block_size):
  padding_length = block_size - (len(message) % block_size)
  if padding_length == 0:
    padding_length = len(message)
  padding = bytes([padding_length])*padding_length
  return message + padding

def pkcs_strip(message): # remove padding
  padding_length = message[-1]
  return message[:-padding_length]

def split_message_into_block(message, block_size):
  return [ message[ i*block_size : (i+1)*block_size ]for i in range(ceil(len(message)/block_size)) ]

def bxor(a, b): # do XOR
  "bitwise XOR of bytestrings"
  return bytes([x^y for (x, y) in zip(a, b)])

def encrypt_aes_128_block(msg, key):
  cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
  encryptor = cipher.encryptor()
  return encryptor.update(msg) + encryptor.finalize()

def decrypt_aes_128_block(ctxt, key):
  cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
  decryptor = cipher.decryptor()
  return decryptor.update(ctxt) + decryptor.finalize()

def encrypt_aes_128_cbc(message, iv, key):
  result = b''
  previous_block_txt = iv
  padded_msg = pkcs_padding(message, block_size=16)
  blocks = split_message_into_block(padded_msg, block_size=16)

  for block in blocks:
    xor_ed_block = bxor(block, previous_block_txt)
    encrypted_txt = encrypt_aes_128_block(xor_ed_block, key)
    result += encrypted_txt
    previous_block_txt = encrypted_txt

  return result

def decrypt_aes_128_cbc(cyphertxt, iv, key):
  result = b''
  previous_block_txt = iv
  blocks = split_message_into_block(cyphertxt, block_size=16)

  for block in blocks:
    un_xor_message = decrypt_aes_128_block(block, key)
    result += bxor(un_xor_message, previous_block_txt)
    previous_block_txt = block
  
  return pkcs_strip(result)


for _ in range(10):
  length = randint(5,50)
  msg = os.urandom(length)
  key = os.urandom(16)
  iv = os.urandom(16)
  excrypted_txt = encrypt_aes_128_cbc(msg, iv, key)
  decrypted_txt = decrypt_aes_128_cbc(excrypted_txt, iv, key)
  print(f'random case {_}     :')
  print(f'message           : {msg}\nencrypted message : {excrypted_txt}\ndecrypted message : {decrypted_txt}')