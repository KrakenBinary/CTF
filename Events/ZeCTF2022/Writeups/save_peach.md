# Save peach!

## Summary

Similar the the Mario bros! challenge. this jail also uses eval. We know however from the challenge description that this is a Python jail.
one of the biggest vulnerabilities in a python jail is import. either import sys or import os.

> anytime eval() or exec() is run in python the input should be run through the validate() function first to make it safer!

### The Actual Code from the challenge

```python
def main():
    text=raw_input(">>> ")
    for keyword in ['eval', 'exec', 'import']:
        if keyword in text:
            print("Bowser no likey likey!")
            return;
        else:
            exec(text)
            main()
            return;

if __name__ == "__main__":
    main()
```

This jail is using a blacklist to exit when certain things are found in the input.
This version of blacklisting is not comprehensive. it is possible to use ord or some other version of that in python to get around that.

Still, the simply glaring issue is that a non-validated string is being executed. That is a massive security hole. 

## Process

![alt text](https://github.com/KrakenBinary/CTF/blob/main/Events/ZeCTF2022/Images/savepeach.png)

So again, no code to look at. So lets assume our hands will be ties since this one is tagged hard.
Jumping in we connect and looking at the hint mentioning a python I will assume its python shell.
First thing I like to do in a python shell is load os and spawn shell. Its a common solution.

![alt text](https://github.com/KrakenBinary/CTF/blob/main/Events/ZeCTF2022/Images/bowser2.png)

next ... I wont lie: I spent about 3 hours testing various things for blacklist playing with print and trying to get overflow buffers.
What I found in that time, that I started to focus on, was that any time you type the word eval it exits and says "Bowser no likey!"
Ok so it had something to do with an eval? Was the stuff I type being evaled? So, after 3 hours I went back to where I started.

```python
import os; os.system("ls")

# that quickly turned into cat flag

import os; os.system("cat flag.txt")
```
and here is the results:

![alt text](https://github.com/KrakenBinary/CTF/blob/main/Events/ZeCTF2022/Images/bowser3.png)

## Flag

> EZ-CTF{P34CH_H4S_B33N_S4V3D}
