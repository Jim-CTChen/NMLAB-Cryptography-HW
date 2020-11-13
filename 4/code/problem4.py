with open('./04data.txt') as file:
  ciphertext_list = [ bytes.fromhex(line.strip()) for line in file ]

# 'a'~'z', ' '
ascii_text_chars = list(range(65, 91)) + list(range(97, 123)) + [32]

def bxor(a, b): # do XOR
  "bitwise XOR of bytestrings"
  return bytes([x^y for (x, y) in zip(a, b)])

def letter_ratio(input_bytes):
  letter_amount = sum([x in ascii_text_chars for x in input_bytes])
  return letter_amount/len(input_bytes)

def is_prob_text(input_bytes): # take 70% of text char in input text as possible sentence
  ratio = letter_ratio(input_bytes)
  return True if ratio > 0.7 else False

def single_byte_xor(cyphertext):
  best = None
  for i in range(2**8):
    candidate_key = i.to_bytes(1, byteorder='big')
    keystream = candidate_key*len(cyphertext)
    candidate_message = bxor(keystream, cyphertext)
    letter_amount = sum([x in ascii_text_chars for x in candidate_message])
    if best == None or letter_amount > best['letter_amount']:
      best = {
        "message": candidate_message,
        "letter_amount": letter_amount,
        "key": candidate_key,
        "letter_ratio": letter_amount/len(cyphertext)
      }
  return best

candidates = list()

for (line_num, ciphertext) in enumerate(ciphertext_list):
  result = single_byte_xor(ciphertext)
  if result['letter_ratio'] > 0.9:
    result['line_number'] = line_num
    candidates.append(result)

for (id, candidate) in enumerate(candidates):
  for (key, value) in candidate.items():
    print(f'{key}: {value}')
