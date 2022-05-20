from Crypto.Cipher import AES
from hashlib import sha256
from Crypto.Util.Padding import pad, unpad
import signal
import subprocess
import socketserver
import os
import base64
import hashlib
from Crypto import Random
import itertools

def create_keys():
    random.seed(os.urandom(10000))
    public_key = [random.getrandbits(32) for _ in range(624)]
    private_key = [random.getrandbits(32) for _ in range(624)]
    return public_key, private_key


def crack(public_key):
    rc = RandCrack()
    for x in public_key:
        rc.submit(x)
    cracked_private_key = [rc.predict_getrandbits(32) for _ in range(624)]
    return cracked_private_key


def demo():
    cracked = 0
    for attempt in range(1, 101):
        public_key, private_key = create_keys()
        cracked += crack(public_key) == private_key
        print(cracked, 'out of', attempt, 'private keys cracked')

def encrypt_block(block, secret):
    enc_block = b''
    print('block: ', block)
    print('secret: ', secret)
    for i in range(BLOCK_SIZE):
        val = (block[i]+secret[i]) % 256
        print('{} = {} + {} % 256'.format(val,block[i],secret[i]))
        enc_block += bytes([val])
    print('enc_block: ', enc_block)
    return enc_block


def encrypt(msg, password):
    h = sha256(password).digest()
    print('h: ', h)
    print('BLOCK_SIZE: {} | %32= {} | !=0 {}'.format(len(msg), len(msg) % BLOCK_SIZE, len(msg) % BLOCK_SIZE != 0))
    if len(msg) % BLOCK_SIZE != 0:
        msg = pad(msg, BLOCK_SIZE)
        print('msg+padding: ',msg)
    blocks = [msg[i:i+BLOCK_SIZE] for i in range(0, len(msg), BLOCK_SIZE)]
    print('blocks: ',blocks)
    ct = b''
    # each block (the command and the result) is sent to its own encryption.
    for block in blocks:
        # print('block: ',block)
        enc_block = encrypt_block(block, h)
        h = sha256(enc_block + block).digest()
        print('final hash: ', h)
        ct += enc_block
    ct_hex = ct.hex()
    print('===============')
    print('final: ', ct.hex())
    print('from hex: ', bytearray.fromhex(ct_hex))
    enc = base64.b64decode(ct)
    # print('decrypt: ', cipher.decrypt(enc[AES.block_size:]))

def check_in(string_in):
    compare_string = b'cat secret.txt'
    allowed_commands = [b'whoami', b'ls', b'cat secret.txt', b'pwd']
    if string_in in allowed_commands:
        print('-=IN=-')
    else:
        print('string_in: ', list(string_in))
        print('check_text: ', list(b'cat secret.txt'))
        print(compare_string.hex())

def break_byte():
    fully = '4dab0c8e7d2b11ad8338e262d6d7e253932c0b46d4dbe961ba20cad72435365d47bea67b91a6923055f06077f04a4081'
    print(fully)

BLOCK_SIZE = 32
msg = b'Command executed: cat secret.txt\nHTB{-FIND_ME-}\n'
password = os.urandom(32)
encrypt(msg, password)
check_in(b'')
break_byte()




'''
99, 97, 116, 32, 115, 101, 99, 114, 101, 116, 46, 116, 120, 116
636174207365637265742e747874
0000000000000000000000000000

03a47f4fb66e8d980bd7c777afb50aa3  << random number
70f658d79c4b0b0f8f8f8aa1f57202d4  << FLAG
acafe4837a8ba09be8207bebcf532d64  << \x0f (null bytes)

'''
