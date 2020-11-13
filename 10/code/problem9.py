def pkcs_padding(message, block_size):
  padding_length = block_size - (len(message) % block_size)
  if padding_length == 0:
    padding_length = len(message)
  padding = bytes([padding_length])*padding_length
  return message + padding

def pkcs_strip(message):
  padding_length = message[-1]
  return message[:-padding_length]

print(pkcs_strip(pkcs_padding(b'YELLOW SUBMARINE', 20)))