###### tags: `網路與多媒體實驗`
# Cryptography homework problem8 writeup
## 思路
由於使用ECB的話，同樣的明文會被encode成同樣的密文，並且AES使用16個bytes為cipher block，因此只要簡單來說只要將密文分成每16bytes為一個block，若有複數block的密文相同的話就是使用ECB
## Code
#### functions
``` python
def has_repeated_block(txt, block_size = 16) # 將密文分成每16bytes一個block
                                             # 並用set去檢測重複性
```

## How to work
``` bash
>> cd code
>> python3 problem8.py
```