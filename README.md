# Quantum Coin Flip

Flipping a coin is for losers; use quantum mechanics instead.

I use this repository for Python packaging practice, as the function is so simple.

## The Code

### Hey, *I'm* not a loser. What's going on?

A lab at ANU is continually making measurements on the quantum vacuum and then putting binary versions of that up on the internet.
I originally wrote this code by adapting an html parser from [here](https://github.com/pcragone/anurandom/blob/master/anurandom.py) for my students in a Computational Methods in Physics class that I was a course assistant for, Spring 2019.
The script came later: flipping a coin was too deterministic for me, so I wrote a python script for the shell that gives me truly random quantum measurements!

![Wow!](https://github.com/cqpancoast/qrng/blob/master/sample_output.png)

Need to decide what I'll have for dinner? If I have four options, I just assign each of them a number from 0 to 3, and type `qflip 4` into the prompt.

Need to decide what homework assignment I'll do first? If I have seventeen options... well, you get the point.

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

## Install

### Okay, I'm convinced. How do I download this so I can decide whether to ask this one guy/gal out?

First of all, just ask! If you don't, you'll always be wondering what happened, and the worst that can happen is you get some practice with rejection.

Anyway, just run `pip install qflip` or something.

### Nevermind, this actually sucks, and I want to uninstall it.

You guessed it: `pip uninstall qflip`.

