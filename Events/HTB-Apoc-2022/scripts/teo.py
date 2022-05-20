from pwn import *
from hashlib import sha256
BLOCK_SIZE = 32

s = remote("0.0.0.0", 1337)
s.sendlineafter(">", "cat secret.txt")
ciphertext = bytes.fromhex(s.recvline().decode())
print('>>>cipher: {}'.format(ciphertext))

def decrypt_block(enc_block, secret):
    block = b''
    for i in range(BLOCK_SIZE):
        val = (enc_block[i]-secret[i]) % 256
        block += bytes([val])
    return block

blocks = [ciphertext[i:i+BLOCK_SIZE] for i in range(0, len(ciphertext), BLOCK_SIZE)]
print('>>>blocks: {}'.format(blocks))
plaintextblock = b'Command executed: cat secret.txt'
ciphertextblock = blocks[0]
output = b''
for block in blocks[1:]:
    key = sha256(ciphertextblock + plaintextblock).digest() # derive key for next block
    plaintextblock = decrypt_block(block, key) # set blocks so we can derive key after that
    output += plaintextblock
    ciphertextblock = block

print(output.decode())
