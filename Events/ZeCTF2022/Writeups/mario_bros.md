# Mario bros!

## Summary

This is a "break out of the jail shell" pwn challenge. Turns out, as you will see in my process section, it was using eval to echo my text. ‘eval’ is used to interpret (evaluate) strings into live logic. 
Experienced Bash scriptwriters will describe the outcome of implementing ‘eval’ in two different ways: 

1. a really bad idea
2. consciously introducing a vulnerability into your script. 

With this specific vulnerability you can touch files and generally cause mayhem up to and including making the script delete itself.

### Ways in which this vulnerability might go sideways:

delete the entire file system (delete the computer)

```sh
$ curl '127.0.0.1:8080/$(rm${IFS}-rf${IFS}/*)'
```

make the script delete itself:

```sh
$ curl '127.0.0.1:8080/$(rm${IFS}${PWD}/*.sh)'
```

### The Actual Code from the challenge

```sh
#!/bin/sh

echo 'Are you root?'
read -p "> " answer

eval "echo $answer"

echo 'lol ur not root!'
exit 1
```

so you can see that your inputs are pushed through an eval in order to run them through the shell's echo command.

> Eval is the most common CTF jail. With more sophisticated jails using blacklists to protect the eval.

## Process

![alt text](https://github.com/KrakenBinary/CTF-EzCTF2022/blob/main/Images/mariobros.png)

This one is a netcat pwn with no files. So we cant see the source. I assume its a jail shell of some sort.

![alt text](https://github.com/KrakenBinary/CTF-EzCTF2022/blob/main/Images/mariobros2.png)

yeap. connecting to netcat we get a prompt asking if we are root. with a simple yes the shell mocks us.
Normally a shell should not mock you. lets figure out what kind of shell this is.

Lets run it through the alphabet to make sure it isn't black listing any of the basic things.

![alt text](https://github.com/KrakenBinary/CTF-EzCTF2022/blob/main/Images/mariobros3.png)

ok looks like our alphabet is intact ... lets try some other characters

![alt text](https://github.com/KrakenBinary/CTF-EzCTF2022/blob/main/Images/mariobros4.png)


that did break something. lets make sure we cant just open shell

![alt text](https://github.com/KrakenBinary/CTF-EzCTF2022/blob/main/Images/mariobros5.png)

apparently not. Lets try to echo something. The idea behind an $echo or $ls or something is that we are trying to access shell commands. This ended up working and I will just post my terminal so you can see how I played with it till I found how to use ls. 

![alt text](https://github.com/KrakenBinary/CTF-EzCTF2022/blob/main/Images/mariobros6.png)

So there is the flag!

## Flag

> EZ-CTF{UNSECUR3_B4SH}

