#!/usr/bin/python3
decode_me = '112 105 99 111 67 84 70 123 103 48 48 100 95 107 49 116 116 121 33 95 110 49 99 51 95 107 49 116 116 121 33 95 51 100 56 52 101 100 99 56 125 10'

print(decode_me)

splitted = decode_me.split()

print(splitted)

re_list = []
for char in splitted:
    print(chr(int(char)))
    re_list.append(chr(int(char)))

re_list = ''.join(re_list)
print(re_list)
