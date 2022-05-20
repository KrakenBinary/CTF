from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes
import hashlib
import random
import socketserver
import signal
import sys


FLAG = "HTB{--REDACTED--}"
DEBUG_MSG = "DEBUG MSG - "
done = 0
p = 0x509efab16c5e2772fa00fc180766b6e62c09bdbd65637793c70b6094f6a7bb8189172685d2bddf87564fe2a6bc596ce28867fd7bbc300fd241b8e3348df6a0b076a0b438824517e0a87c38946fa69511f4201505fca11bc08f257e7a4bb009b4f16b34b3c15ec63c55a9dac306f4daa6f4e8b31ae700eba47766d0d907e2b9633a957f19398151111a879563cbe719ddb4a4078dd4ba42ebbf15203d75a4ed3dcd126cb86937222d2ee8bddc973df44435f3f9335f062b7b68c3da300e88bf1013847af1203402a3147b6f7ddab422d29d56fc7dcb8ad7297b04ccc52f7bc5fdd90bf9e36d01902e0e16aa4c387294c1605c6859b40dad12ae28fdfd3250a2e9
g = 2


class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        signal.alarm(0)
        main(self.request)


class ReusableTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


def sendMessage(s, msg):
    s.send(msg.encode())


def recieveMessage(s, msg):
    sendMessage(s, msg)
    return s.recv(4096).decode().strip()


def decrypt(encrypted, shared_secret):
    print('decrypt started')
    key = hashlib.md5(long_to_bytes(shared_secret)).digest()
    print('key: {}'.format(key))
    cipher = AES.new(key, AES.MODE_ECB)
    print('cipher {}'.format(cipher))
    print(cipher.decrypt(encrypted))
    try:
        message = cipher.decrypt(encrypted)
        print(message)
    except Exception as e:
        print(str(e))
    return message


def main():
    #print("Generating The Global DH Parameters\n")
    #print(f"g = {g}, p = {p}\n")
    #print(p)
    #print("Calculation Complete\n\n")

    print("Generating The Public Key of CPU...\n")
    c = random.randrange(2, p - 1)
    C = pow(g, c, p)
    print("Calculation Complete\n")
    #print("Public Key is: ???\n\n")

    M = input(">>>int: ")

    try:
        M = int(M)
    except:
        sendMessage("Unexpected Error Occured\n")
        exit()

    print("\nThe CPU Calculates The Shared Secret")
    shared_secret = pow(M, c, p)
    print('shared secret is: {}'.format(shared_secret))
    print("Calculation Complete")

    encrypted_sequence = input("encryption sequence: ")

    try:
        encrypted_sequence = bytes.fromhex(encrypted_sequence)
        assert len(encrypted_sequence) % 16 == 0
    except:
        print('nope!')
        print(len(encrypted_sequence) % 16 == 0)
        print(len(encrypted_sequence))
        print(len(encrypted_sequence) % 16)
        main()
    try:
        print('{} || {}'.format(shared_secret, encrypted_sequence))
        sequence = decrypt(encrypted_sequence, shared_secret)
    except Exception as e:
        print(str(e))
        
    print('I am here')
    #print ('{} | | {}'.format(sys.getsizeof(sequence), sys.getsizeof(b"Initialization Sequence - Code 0")))
    if sequence == b"Initialization Sequence - Code 0":
        print("\nReseting The Protocol With The New Shared Key\n")
        print(f"{FLAG}")
    else:
        print(sequence)
        done = 1
        main()


if __name__ == '__main__':
    '''
    Logic:
        ask for an int (easy pass)
        
    '''
    #socketserver.TCPServer.allow_reuse_address = True
    #server = ReusableTCPServer(("0.0.0.0", 1337), Handler)
    #server.serve_forever()
    #print(p)
    main()

