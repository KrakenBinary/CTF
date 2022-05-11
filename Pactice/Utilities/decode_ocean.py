#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Just base64 so I can test the flow

Imports:
    - haslib: md5, SHA1, SHA224, SHA256, SHA384, SHA512
    - base36:
    - base58:
    - base62:  # Not working!
    - base64:
    - base91:
    - base92:
    - binascii:  # No idea :/
    - urllib.parse:
'''


from urllib.parse import quote, unquote
import argparse  # sudo apt-get install python-argparse
import hashlib  # pip install hashlib
import base64  # pip install pybase64
import base36  # pip install base36
import base58  # pip install base58
# import base62  # pip install pybase62
import base91  # pip install base91
# import base92  # pip install pybase64
# import binascii - no idea :/


def main():
    '''
    this is where the fun happens!

    Todo: fix the sorting and figure out how to print.
    '''
    parser = argparse.ArgumentParser()

    parser.add_argument('-md5', dest='md5', help='MD5 encryption')
    parser.add_argument('-sh1', dest='sh1', help='SH1 encryption')
    parser.add_argument('-b64', dest='b64', help='Base64 encode')
    parser.add_argument('-b32', dest='b32', help='Base32 encode')
    parser.add_argument('-b16', dest='b16', help='Base16 encode')
    parser.add_argument('-a85', dest='b85_1', help='Base85_1 encode')
    parser.add_argument('-b85', dest='b85_2', help='Base85_2 encode')
    parser.add_argument('-b36', dest='b36', help='Base36 encode')
    parser.add_argument('-b58', dest='b58', help='Base58 encode')
    parser.add_argument('-b91', dest='b91', help='Base91 encode')
    parser.add_argument('-db64', dest='db64', help='Base64 decode')
    parser.add_argument('-db32', dest='db32', help='Base32 decode')
    parser.add_argument('-db16', dest='db16', help='Base16 decode')
    parser.add_argument('-da85', dest='db85_1', help='Base85_1 decode')
    parser.add_argument('-db85', dest='db85_2', help='Base85_2 decode')
    parser.add_argument('-db36', dest='db36', help='Base36 decode')
    parser.add_argument('-db58', dest='db58', help='Base58 decode')
    parser.add_argument('-db91', dest='db91', help='Base91 decode')
    parser.add_argument('-urlen', dest='urlen', help='URL encode')
    parser.add_argument('-urlde', dest='urlde', help='URL decode')
    parser.add_argument('-bin', dest='bin', help='Binary To Decimal')
    parser.add_argument('-octal', dest='octal', help='Octal to Decimal')
    parser.add_argument('-hex', dest='hex', help='Hexadecimal to Decimal')
    parser.add_argument('-dbin', dest='dbin', help='Decimal To Binary ')
    parser.add_argument('-doctal', dest='doctal', help='Decimal to Octal ')
    parser.add_argument('-dhex', dest='dhex', help='Decimal to Hexadecimal')
    parser.add_argument('-ord', dest='ord', help='Letter To ASCII')
    parser.add_argument('-chr', dest='chr', help='ASCII To Letter')

    options = parser.parse_args()

    if options.md5:
        md5(options.md5)
    if options.sh1:
        sh1(options.sh1)
    if options.b64:
        string_to_b64(options.b64)
    if options.b32:
        string_to_b32(options.b32)
    if options.b16:
        string_to_b16(options.b16)
    if options.a85:
        string_to_b85(options.a85)
    if options.b85:
        string_to_a85(options.b85)
    if options.b36:
        string_to_base36(options.b36)
    if options.b58:
        string_to_base58(options.b58)
    if options.b91:
        string_to_base91(options.b91)
    if options.da85:
        a85_to_string(options.da85)
    if options.db85:
        b85_to_string(options.db85)
    if options.db36:
        base36_to_string(options.db36)
    if options.db58:
        base58_to_string(options.db58)
    if options.db91:
        base91_to_string(options.db91)
    if options.db64:
        b64_to_string(options.db64)
    if options.db32:
        b32_to_string(options.db32)
    if options.db16:
        b16_to_string(options.db16)
    if options.urlen:
        url_encode(options.urlen)
    if options.urlde:
        url_decode(options.urlde)
    if options.bin:
        bin_to_dec(options.bin)
    if options.octal:
        oct_to_dec(options.octal)
    if options.hex:
        hex_to_dec(options.hex)
    if options.dbin:
        dec_to_bin(options.dbin)
    if options.doctal:
        dec_to_oct(options.doctal)
    if options.dhex:
        dec_to_hex(options.dhex)
    if options.doctal:
        dec_to_oct(options.doctal)
    if options.dhex:
        dec_to_hex(options.dhex)
    if options.ord:
        lett_to_ascii(options.ord)
    if options.chr:
        ascii_to_lett(options.chr)


def md5(string_input):
    '''md5 is a one-way encryption often used to store/obfuscate passwords'''
    hash_md5 = hashlib.md5()
    hash_md5.update(string_input.encode(encoding='utf-8'))
    return hash_md5.hexdigest()


def sh1(string_input):
    '''SH1 is a one-way encryption often used to store/obfuscate passwords'''
    string_hash = hashlib.sha1()
    string_hash.update(string_input.encode())
    return string_hash.hexdigest()


def string_to_b64(string_input):
    '''base64 Convert the encoding format to normal character type'''
    encode = string_input.encode('utf-8')
    encode_base64 = base64.b64encode(encode)
    return encode_base64.decode('utf-8')


def b64_to_string(string_input):
    '''Convert the string to b32 Coding format'''
    decode = base64.b64decode(string_input)
    return decode.decode()


def string_to_b32(string_input):
    '''base32 Convert the encoding format to the normal character type'''
    encode = base64.b32encode(string_input)
    print('Original:' + string_input)
    print('Base32 encode:' + str(encode))


def b32_to_string(string_input):
    '''Convert the string to base16 Coding format'''
    decode = base64.b32decode(string_input)
    # print('Base32:' + string_input)
    print('Base32 decode:' + str(decode))


def string_to_b16(string_input):
    '''base16 Convert the encoding format to the normal character type'''
    encode = base64.b16encode(string_input)
    print('Original:' + string_input)
    print('Base16 encode:' + str(encode))


def b16_to_string(string_input):
    '''Convert the string to base85 The first kind of coding format'''
    decode = base64.b16decode(string_input)
    # print('Base16:' + string_input)
    print('Base16 decode:' + str(decode))


def string_to_a85(string_input):
    '''string to base85'''
    encode = base64.a85encode(string_input)
    print('Original:' + string_input)
    print('Base85_1 encode:' + str(encode))


def a85_to_string(string_input):
    '''Convert the string to base85 The second kind of coding format'''
    decode = base64.a85decode(string_input)
    # print('Base85_1:' + string_input)
    print('Base85_1 decode:' + str(decode))


def string_to_b85(string_input):
    '''base85'''
    encode = base64.b85encode(string_input)
    print('Original:' + string_input)
    print('Base85_2 encode:' + str(encode))


def b85_to_string(string_input):
    '''Convert the string to base36 Coding format'''
    decode = base64.b85decode(string_input)
    # print('Base85_2:' + string_input)
    print('Base85_2 decode:' + str(decode))


def string_to_base36(string_input):
    '''base36 Convert the encoding format to the normal character type'''
    encode = base36.loads(string_input)
    print('Original:' + string_input)
    print('Base36 encode:' + str(encode))


def base36_to_string(string_input):
    '''Converts a string to base58 Coding format'''
    decode = base36.dumps(int(string_input))
    # print('Base36:' + string_input)
    print('Base36 decode:' + str(decode))


def string_to_base58(string_input):
    '''base58 Convert the encoding format to the normal character type'''
    encode = base58.b58encode(str(string_input))
    print('Original:' + string_input)
    print('Base58 encode:' + str(encode))


def base58_to_string(string_input):
    '''Converts a string to base91 Coding format'''
    encode = base58.b58decode(string_input)
    print('Base58 decode:' + str(encode))


def string_to_base91(string_input):
    '''base58 Convert the encoding format to the normal character type'''
    encode = base91.encode(string_input)
    print('Original:' + string_input)
    print('Base91 encode:' + str(encode))


def base91_to_string(string_input):
    '''Convert the string to base Family bucket coding format'''
    decode = base91.decode(string_input)
    # print('Base91:' + string_input)
    print('Base91 decode:' + str(decode))
    # def basefamily(s):
    # b64ToString(s)
    # b32ToString(s)
    # b16ToString(s)
    # base58Tostring(s)
    # base91Tostring(s)
    # base36Tostring(s)
    # base85_1Tostring(s)
    # base85_2Tostring(s)
    # Conduct url code


def url_encode(string_input):
    '''Conduct url code'''
    encode = quote(string_input)
    print('Original:' + string_input)
    print('URL encode:' + encode)


def url_decode(string_input):
    '''Convert binary to decimal'''
    decode = unquote(string_input)
    print('URL encode:' + string_input)
    print('URL decode:' + decode)


def bin_to_dec(string_input):
    '''Convert octal to decimal'''
    result = int(string_input, 2)
    print('Binary :' + str(string_input))
    print('Decimal :' + str(result))


def oct_to_dec(string_input):
    '''Convert hex to decimal'''
    result = int(string_input, 8)
    print('Octal :' + str(string_input))
    print('Decimal :' + str(result))


def hex_to_dec(string_input):
    '''Convert decimal to binary'''
    result = int(string_input, 16)
    print('Hex :' + str(string_input))
    print('Decimal :' + str(result))


def dec_to_bin(string_input):
    '''Convert decimal to octal'''
    string_int = int(string_input)
    result = bin(string_int)
    print('Decimal:' + str(string_int))
    print('Binary:' + str(result))


def dec_to_oct(string_input):
    '''Convert decimal to hexadecimal'''
    string_int = int(string_input)
    result = oct(string_int)
    print('Decimal :' + str(string_int))
    print('Octal :' + str(result))


def dec_to_hex(string_input):
    '''Convert the letters to the corresponding ASCII'''
    string_int = int(string_input)
    result = hex(string_int)
    print('Decimal :' + str(string_int))
    print('Hex :' + str(result))


def lett_to_ascii(string_input):
    '''take ASCII Convert to the corresponding letters and characters'''
    print('Letters:' + string_input)
    result = ''
    for i in string_input:
        result = result + str(ord(i)) + ' '
    print('ASCII :' + result)


def ascii_to_lett(string_input):
    '''yup'''
    list_string = string_input.split(' ')
    result = ''
    print('ASCII :' + string_input)
    for i in list_string:
        i = int(i)
        result = result + chr(i)
    print('Letters :' + result)


if __name__ == '__main__':
    main()