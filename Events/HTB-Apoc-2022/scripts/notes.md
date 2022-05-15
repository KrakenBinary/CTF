Notes on Space entry:
==============
Useful commands:
    dc = run till nex break
    ds = step (execute next command)
    s or F7 = execute next command
    F2 = add/remove break
    . = return to current instruction
==============
r2 -AA ./sp_entrypoint
    open file in r2 and analyze
i?
    look at how to analyze
ia
    look at file basics
afl
    what functions do we have?
        printf? that is exploitable.
izz
    look at strings
        42  0x00000ed0 0x00000ed0 27  28   .rodata            ascii   \n\t\t\t Authentication System\n
        46  0x00002518 0x00002518 57  58   .rodata            ascii   \n%s[+] Door opened, you can proceed with the passphrase: 
        47  0x00002552 0x00002552 9   10   .rodata            ascii   cat flag*
        48  0x0000255c 0x0000255c 21  22   .rodata            ascii   [*] Insert password: 
        49  0x00002578 0x00002578 33  34   .rodata            ascii   0nlyTh30r1g1n4lCr3wM3mb3r5C4nP455
        50  0x0000259a 0x0000259a 9   10   .rodata            ascii   \e[1;5;31m
        51  0x000025a8 0x000025a8 48  55   .rodata            utf8    \n%s[-] Invalid password! Intruder detected! 🚨 🚨\n blocks=Basic Latin,Transport and Map Symbols
        52  0x000025e0 0x000025e0 36  44   .rodata            utf8    \n1. Scan card 💳\n2. Insert password ↪ blocks=Basic Latin,Miscellaneous Symbols and Pictographs,Arrows
        53  0x00002610 0x00002610 71  72   .rodata            ascii   \n[!] Scanning card.. Something is wrong!\n\nInsert card's serial number: 
        54  0x00002658 0x00002658 15  16   .rodata            ascii   \nYour card is: 
        55  0x00002668 0x00002668 46  53   .rodata            utf8    \n%s[-] Invalid option! Intruder detected! 🚨 🚨\n blocks=Basic Latin,Transport and Map Symbols
        56  0x000026a0 0x000026a0 43  50   .rodata            utf8    \n\n%s[-] Invalid ID! Intruder detected! 🚨 🚨\n blocks=Basic Latin,Transport and Map Symbols
        57  0x00002748 0x00002748 4   5    .eh_frame          ascii   \e\f\a\b
s main
V
    going into visual mode
p
    use p to page to debug mode
d
    pull up menu
f
    enter analize fuction
Shift+V
    graph
ood
    open file in debug read/write
dc
    run program
F8 
    step to first fuction call
