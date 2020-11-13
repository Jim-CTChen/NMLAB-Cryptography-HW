with open('./08data.txt') as f:
  cipher_txts = [bytes.fromhex(line.strip()) for line in f]

def has_repeated_block(txt, block_size = 16):
  if len(txt) % 16 != 0:
    return
  else:
    num_blocks = len(txt)//block_size

  blocks = [txt[i*block_size:(i+1)*block_size] for i in range(num_blocks)]
  if (len(set(blocks)) != num_blocks):
    return True
  else:
    return False

ECB_encrypted = list()
for (line_num, cipher_txt) in enumerate(cipher_txts):
  if has_repeated_block(cipher_txt):
    line = line_num
    txt = cipher_txt
    candidate = {"line":line, "txt":txt}
    ECB_encrypted.append(candidate)

print('ECB encoded ciphertext:')
for candidate in ECB_encrypted:
  line = candidate['line']
  txt = candidate['txt']
  print(f'line: {line}\nciphertext: {txt}')

