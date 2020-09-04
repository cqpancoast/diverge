# Quantum Coin Flip

Flipping a coin is for losers; use quantum mechanics instead.

## Install

It's on pypi [here](https://pypi.org/project/qflip-CQPANCOAST/): `pip install qflip-CQPANCOAST`.
To uninstall, `pip uninstall qflip-CQPANCOAST`.

I use this repository for Python packaging practice, as the function is so simple.

## The Code

### Hey, *I'm* not a loser. What's going on?

A lab at ANU is continually making measurements on the quantum vacuum and then putting binary versions of that up on the internet. [Here it is!](https://qrng.anu.edu.au)

I originally wrote this code by adapting an html parser from [here](https://github.com/pcragone/anurandom/blob/master/anurandom.py) for my students in a Computational Methods in Physics class that I was a course assistant for, Spring 2019.
The script came later: flipping a coin was too deterministic for me, so I wrote a python script for the shell that gives me truly random quantum measurements!
Most of the code is mine now, but I figure I should still credit the guy or gal.

### How do I use it?

Just type in qflip and then the number of things you have to choose between.
The program will:
- take a huge number from the ANU quantum random number generator,
- split it into a bunch of still big ones),
- store those numbers in a json file in `~/.qflip`,
- and mod it by the number you specify.

If you don't spefcify a number, it'll choose 2.

```shell
$ qflip
0
$ qflip
1
$ qflip
1
$ qfilp 27
13
$ qflip 0      # This will throw a ValueError.
$ qflip -1     # So will this...
$ qflip beans  # ...and this.
$ qflip 1      # This is fine, though not useful.
0
```

Need to decide what I'll have for dinner?
If I have four options, I just assign each of them a number from 0 to 3, and type `qflip 4` into the prompt.

Need to decide what homework assignment I'll do first?
If I have seventeen options... well, you get the point.

## The Physics

### No, but really, what's going on here?

First of all, there's no way of testing the experimentally, but many (including me) are of the opinion that thinking about this any other way requires mangling the beautiful, beautiful math.

Here's what's up: in laymans terms, before we observe Schrodinger's cat, it is in a superposition of states: neither dead nor alive.
Then, we open the box to make our observation.
It looks *to us* like cat is now definitely alive or dead, but really, *we have split* into someone who saw the cat live and someone who saw the cat die, just like the cat had split earlier!
This isn't the place to go into how quantum mechanics works, but what you need to know is that there's a *totally real other universe* where the numbers in the picture above are different.
Isn't that cool?

When I use this program to decide what shirt to wear, I end up wearing all of them – but it looks to me like I chose one.
We are part of the universe, and we *also* follow the strange laws of quantum mechanics.

If you want further explanation, first do some reading on quantum mechanics ([The Feynman Lectures](https://www.feynmanlectures.caltech.edu/III_toc.html) are always a great place to start), then check out [Hugh Everett's Theory of the Universal Wavefunction](https://www-tc.pbs.org/wgbh/nova/manyworlds/pdf/dissertation.pdf), more popularly known as the "Many Worlds" interpretation of quantum mechanics.

Again, no way of testing this experimentally, but it sure makes the most sense to me.
Debating interpretations of quantum mechanics is exhuasting, so if you're looking for arguments one way or the other, you're free to look online.

## Dear reader, there are so many people smarter than I am.

If you're looking to use the ANU quantum random number server for actual work, don't use this repo — this is just a silly thing I made, functional though it is.
[This project](https://github.com/lmacken/quantumrandom), on the other hand, has a wide array of utility.
Check it out!

[This](https://www.youtube.com/watch?v=oHg5SJYRHA0) is also pretty cool.

