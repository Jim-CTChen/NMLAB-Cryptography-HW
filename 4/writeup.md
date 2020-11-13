###### tags: `網路與多媒體實驗`
# Cryptography homework problem4 writeup
## 思路
1. 針對每行text, 透過iterate 2^8個key去找字母出現比例最高的字串作為該字串的candidate
2. 若該candidate中英文字母出現比率超過90%, 則視為是合法字串
3. 對所有字串做步驟1., 2. 找出合法字串
4. 若合法字串出現大於一個，則可能需要調高篩選字母出現比例

## Code
#### functions
``` python
def bxor(a, b) # bitwise XOR of bytestrings
def letter_ratio(input) # get alphabet ratio
def single_byte_xor(cyphertext) # get best candidate among using every key
```

## How to work
``` bash
>> cd code
>> python3 problem4.py
```