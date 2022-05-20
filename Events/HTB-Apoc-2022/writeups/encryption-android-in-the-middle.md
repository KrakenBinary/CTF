# Android in the middle

This challenge comes with python source code. My cup-o-tea! 
The first thing I did was setup a test script. I combed through the 
origin script to find that it sets up a local socket server and then
waits for a user to connect. 

When a user connects it sends them to main(). Once in main it seems to
show the user various things. like some numbers it has pre-saved. Telling
the user that "these numbers are being generated". nice try.

I see that it asks for only two inputs. the first is used in a pow().
Pow(a, b, c) will do a**b%c. so the modulos of the product of a and b. 
It looks like our input goes in a. This pow is used as a "shared_secret".

Next input request, takes our input and determins if it's length
is a multiple of 16. If it is the script continues.

Now the meat! we send the second input with the secret_key to a function
to encrypt it. once it returns we determin if the byte type object returned
equals b"Initialization Sequence - Code 0" ... so essentally do the bytes match
exactly. If true we get a flag!

ok so first issue is that pesky secret key. It uses things I dont want to
have to reverse like random numbers. So lets use some basic math here. 
0 raised to the power of anything = 0 and 0 % random number = 0. Ok so
lets make our first input 0. our "secret key" will always = 0. Easy?

On to the compare. I did fiddle with sending random strings of text to this
function using a test script. The results were predictable and random. 
meaning, because the key was identical each time the result was the same. 
however, the result was garbage. I needed a way to match the len comparrison AND
match the string byte for byte. So I started sending hexidecimal strings.

With hexidecimal I was able to match the length requirment with some easy padding.
I was even able to match the byte for the final compare. but I was getting flase.
So, ok I suppose I need to match the exact sting. Well, I know the key. why
not run the exact string through the encryption and then print the hex for it.

To do this I ran the string in, and before I hit the message.decrypt() I
simply printed to terminal message.encrypt().hex()
```python
#!/usr/bin/python
# -*- coding:utf-8 -*-
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes
import hashlib
import random
import socketserver
import signal
import sys

def decrypt(encrypted, shared_secret):
    print('{} || {}'.format(encrypted, shared_secret))
    key = hashlib.md5(long_to_bytes(shared_secret)).digest()
    # print('key: {}'.format(key))
    cipher = AES.new(key, AES.MODE_ECB)
    # print('cipher {}'.format(cipher))
    print(cipher.decrypt(encrypted))
    print(cipher.encrypt(b"Initialization Sequence - Code 0").hex())
    try:
        message = cipher.decrypt(encrypted)
        print('----------pass----------')
    except Exception as e:
        print(str(e))
    return message

def main():
    count = 0
    encrypted_sequence = bytes.fromhex('0000000000000000000000000000000000000000000000000000000000000000')
    # encrypted_sequence =  b"Initialization Sequence - Code 0"
    while count < 10:
        decrypt(encrypted_sequence, 0)
        count = count +1

main()
```

feed this into the second input and you get the flag!
```
1af761314a07bf79f31aeb53bc9e1335e1749e1142b326d82a3c29ac37a042bf
```
### Flag
> HTB{7h15_p2070c0l_15_pr0tec73d_8y_D@nb3er_c0pyr1gh7_1aws}
