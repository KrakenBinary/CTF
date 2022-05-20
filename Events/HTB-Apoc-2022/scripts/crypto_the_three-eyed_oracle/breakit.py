#!/usr/bin/env python3
# Reference: zachgrace.com/posts/attacking-ecb
# but it has the spirit of one.
'''three eyed oracle'''
from pwn import remote
from pwn import log
# from pwn import sleep
from pwn import success


remote_connection = remote('0.0.0.0', 1337)


def oracle(plaintext: str):
    '''sending to server for a new thing :)'''
    remote_connection.sendlineafter(">", plaintext.encode('latin-1').hex())
    return remote_connection.recvlineS().strip()


def main():
    '''main method'''
    flag = ""
    process_instance = log.progress('working...')
    while True:
        padding = 'B' * 4 + 'A' * (31 - len(flag))
        ref = oracle(padding)
        for char in range(33, 126):
            # sleep(0.01)
            results = oracle(padding+flag+chr(char))
            process_instance.status(f"\n  ct: {results[64:96]}\n ref: {ref[64:96]}\nflag: {flag}\n pad: {padding+flag+chr(char)}")
            if results[64:96] == ref[64:96]:
                flag += chr(char)
                break
        if '}' in flag:
            break
    success(flag)


if __name__ == "__main__":
    main()
