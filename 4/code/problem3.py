cyphertext = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
ascii_text_chars = list(range(97, 123)) + [32]  # ' ' = 32

def bxor(a, b):
  "bitwise XOR of bytestrings"
  return bytes([x^y for (x, y) in zip(a, b)])

def letter_ratio(input_bytes):
  letter_amount = sum([x in ascii_text_chars for x in input_bytes])
  return letter_amount/len(input_bytes)

def is_prob_text(input_bytes):
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
      best = { "message": candidate_message, "letter_amount": letter_amount, "key": candidate_key}
  return best

result = single_byte_xor(cyphertext)