#!/usr/bin/python3
'''
Process:
    The server creates 12 random bytes as "prefix"
    The server then creates a random 16 byte key (used for encyption)
    it asks for input.
    it sends the block 0 + user input + FLAG + padding(to get it to 16 byte blocks) to be encrypted, with the random key
    the encryption returns in blocks. and is sent to the user.
    
This script will:
    Grab the return value.
    split it into blocks. Ignore the first block (random number)
    put the second block (block[1]) into "blocks_should_be"
    Then it sends the same string through the ecryption that we did at the begining.
        The idea is we get a return on the block[1] from the server and 
        guess with random keys until we get a match. then we print that key.
    once we get a match we will use that exact key with the server response to decode the server response to get the flag

'''

import threading
import sys
import os
import random
import socket
from time import sleep
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def get_block(string_enc, block_size):
    '''
    We call this when we get the string from the server.
    It puts the string into blocks that we can handle.
    '''
    new = []
    for i in range(0, len(string_enc), block_size):
        # using a blank array we append it with grouping that are the size of our blocks.
        new.append(string_enc[i:i+block_size])
    return new


def push_out(blocks, string_known):
    #print('-=PUSHOUT=-')
    # we know block[1] should be all 0's but this is the encrypted version with a random key that we need to find.
    blocks_should_be = blocks[1]
    count = 2000000  # limiting a loop is good idea!
    for i in range(count):
        # lets generate a new random key each time this loops.
        key = random.randbytes(16)
        # send the new random key with the known string (that we sent to the server) to be encrypted.
        test_string = encrypt(key, string_known)
        # we need to "encode" the result to make sure we have the b'' on it.
        test_string = test_string.encode()
        # split out new random string into blocks so we can grab block[1]
        test_blocks = get_block(test_string, block_size)
        # does the block[1] from the sever match the one we just made with a random key?
        if blocks_should_be == test_blocks[1]:
            for i in range(5): # Screams to the console
                print('-=-=-=GOTHIT=-=-=-')
                print(key)
                print(blocks_should_be)
                print(test_blocks[1])
            # if we have a match print the key ... then we use this to decrypt the full message and this challenge is over.
            with open('log.txt', 'w') as f: # Writes log file once hit is found
                f.write("\n")
                f.write(key)
                f.write(" || ")
                f.write(blocks_should_be)
                f.write(" || ")
                f.write(test_blocks[1])
            os._exit(1) # Kills all threads on hit instead of break
            #break  # make sure it stops!
        #else:
            # if no match, we print the result and keep going.
            #print('-=*=- {} || {} | {}'.format(i,
            #      blocks_should_be, test_blocks[1]))


def encrypt(key, msg):
    ''' this is copy/paste from the server.'''
    sleep(0.01)
    # We know there is a flag so we just throw this in so the encytption
    # is "close" to what the server is doing. but really we care more
    # about the block between the prefix and the flag.
    FLAG = b'HTB{--PLACE_HOLDER--}'
    prefix = random.randbytes(12)
    # print(msg)
    msg = bytes.fromhex(msg)
    crypto = AES.new(key, AES.MODE_ECB)
    padded = pad(prefix + msg + FLAG, 16)
    return crypto.encrypt(padded).hex()


if __name__ == "__main__":
    '''
    Script starts here! We connect to the server, get the result that we need
    which essentially generates a block using 16 0's
    we then send that info off to the push function.
    '''
    print('-=ENTERMAIN=-')
    string_known = '0'*20
    auth_length = 32
    # the encryption takes 16 byte blocks and returns 32 byte blocks (I think)
    block_size = 32
    """
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # why 20 0's? because 16 byte block + 4 to fill up the missing bytes from the 12 random byte prefix.

    print('-=CONNECT=-')
    clientSocket.connect(("0.0.0.0", 32754))  # 157.245.47.33:32242
    sleep(1)
    dataFromServer = clientSocket.recv(1024)
    print(dataFromServer.decode())
    sleep(1)
    # send the string we built. aka 20 0's
    clientSocket.send(string_known.encode())
    sleep(1)
    # this is the string that the server encoded.
    dataFromServer = clientSocket.recv(1024)
    print(dataFromServer.decode())
    string_enc = dataFromServer
    """
    # Now lets split the string recieved into blocks and grab the block of 0's that we sent.
    string_enc = b'dfea1081eb89aa6fef0c62a7143067cbbc5b36d11122aae146cc64b7f0b3631ce64c1ab735f4882fb42db3ec860a93aa'
    
    ## Puts threads into a list
    threads = []
    for i in range(2000): # Creates 1000 threads with the push_out function as a target
        threads.append(threading.Thread(target=push_out, args=((get_block(string_enc, block_size), string_known))))
        threads[i].start() # Starts each thread as it goes
        print(f"Started thread {i}")

    print("Started all threads")
    for thread in threads: # Waits for all threads to finish, just means that this program will wait nicely until a thread gets a hit
        thread.join()
