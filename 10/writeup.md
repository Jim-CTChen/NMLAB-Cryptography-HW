###### tags: `網路與多媒體實驗`
# Cryptography homework problem10 writeup
## 思路
### 加密
1. 利用pkcs padding 補齊明文長度
2. CBC加密是利用每個block加密後的結果來將下一個block的明文XOR後在加密，因此可以產生不規律的密文
3. 利用random的方式產生iv(第一個block的previous_ctxt)
4. 將每個block xor previous txt後再進行aes_128加密

### 解密
1. 步驟與加密相反，先將每個block的密文進行aes_128解密
2. 將解密完的message xor previous_ctxt才是明文，並且將密文傳下去當作previous_ctxt
3. strip padding
## Code
#### functions
``` python
pkcs_padding(message, block_size) # PKCS#7 padding scheme
pkcs_strip(message) # strip PKCS#7 padding
split_message_into_block(message, block_size) # split message into blocks

encrypt_aes_128_block(msg, key)  # use package
decrypt_aes_128_block(ctxt, key) # cryptography.hazmat.primitives.ciphers
                                 # to do AES encryption on a block
                                 
encrypt_aes_128_cbc(message, iv, key)   # encrypt message using CBC mode 
decrypt_aes_128_cbc(cyphertxt, iv, key) # in AES encryption
```

## How to work
I do 10 random cases (with random length of message) in problem10.py.
``` bash
>> cd code
>> python3 problem10.py
```