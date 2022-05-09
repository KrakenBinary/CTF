# OMG

## Summary

No real exploit here. This is just specifically formatted text.

## Process

![alt text](https://github.com/KrakenBinary/CTF-EzCTF2022/blob/main/Images/omg.png)

first we download the payload. We will notice it has no extension. So lets check it with files

```sh
$ file OMG
```
> OMG: ASCII text, with very long lines

ok that is nothing interesting. Lets run strings on this thing.

```sh
$ strings OMG
```
>  a LOT of OMG text repeating. I mean, a LOT

Lets see what this looks like in Geany since the strings are so long.

![alt text](https://github.com/KrakenBinary/CTF-EzCTF2022/blob/main/Images/omg2.png)

and there it is. interesting.

## Flag

> EZ-CTF{1_HAT3_TH15_FL4G}

