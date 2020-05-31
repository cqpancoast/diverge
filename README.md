# diverge

Make your decisions by taking advantage of splits in the universe, becasue flipping a coin is for losers.

## That's a bold claim. What's going on?

A lab at ANU is continually making measurements on the quantum vacuum and then putting binary versions of that up on the internet.
I originally wrote this code by adapting an html parser from [here](https://github.com/pcragone/anurandom/blob/master/anurandom.py) for my students in a Computational Methods in Physics class that I was a course assistant for, Spring 2019.
The shell script came later: flipping a coin was too deterministic for me, so I wrote a shell script that uses those measurements to let me make all decisions at once!

![Wow!](https://github.com/cqpancoast/qrng/blob/master/sample_output.png "splitting the universe")

Need to decide what I'll have for dinner? If I have four options, I just assign each of them a number from 0 to 3, and type `diverge 4` into the prompt.

Need to decide what homework assignment I'll do first? If I have seventeen options... well, you get the point.

## No, but really, what's going on here?

First of all, there's no way of testing the experimentally, but many (including me) are of the opinion that thinking about this any other way requires mangling the beautiful, beautiful math.

In laymans terms, when we observe Schrodinger's cat, it looks *to us* like it has chosen to live or die, but really, *we have split* into someone who saw the cat live and someone who saw the cat die!
This isn't the place to go into how quantum mechanics works, but what you need to know is that there's a *totally real other universe* where the numbers in the picture above are different.
Isn't that cool?

If you DO want further explanation, first do some reading on quantum mechanics ([The Feynman Lectures](https://www.feynmanlectures.caltech.edu/III_toc.html) are always a great place to start), then check out [Hugh Everett's Theory of the Universal Wavefunction](https://www-tc.pbs.org/wgbh/nova/manyworlds/pdf/dissertation.pdf), more popularly known as the "Many Worlds" interpretation of quantum mechanics.

Again, no way of testing this experimentally, but it sure makes the most sense to me.
Debating interpretations of quantum mechanics is exhuasting, so if you're looking for arguments one way or the other, you're free to look online.

## Okay, I'm convinced. How do I download this so I can decide whether to ask this one guy/gal out?

First of all, just ask! If you don't, you'll always be wondering what happened, and the worst that can happen is you get some practice with rejection.

Anyway, run this code to install this on your computer.
I choose `~/.diverge` as the directory to install this in, but you're free to do so anywhere you want.

First, clone this repository into a dot dir in your home directory.

```shell
INSTALL_DIR="~/.diverge"  # This can be anything you want, but I prefer this one
git clone https://www.github.com/cqpancoast/diverge $INSTALL_DIR
```

Then, add alias for the main diverge script to appropriate rc/profile file, so it's easily callable.
If you don't set RC\_FILE to something yourself, this program will chastise you.
For more info on what rc and profile files are, check out [here](https://www.linuxjournal.com/content/profiles-and-rc-files).

```shell
ALIAS_DESC='# Diverge script variables: from https://www.github.com/cqpancoast/diverge'
ALIAS_SCRIPT_VAR="DIVERGE_DIR=$INSTALL_DIR"
ALIAS_STRING='alias diverge="sh $DIVERGE_DIR/diverge.sh"'
```

If you want to add this script to multiple rc/profile files, run the below section multiple times.

```shell
if [ -z "$RC_FILE" ]; then
  echo "You have not set an RC_FILE varaible. Read the directions!"
  exit 1

echo "" >> $RC_FILE
echo ALIAS_DESC >> $RC_FILE
echo ALIAS_SCRIPT_VAR >> $RC_FILE
echo ALIAS_STRING >> $RC_FILE
source $RC_FILE
```

That's it! You should be ready to go.

## Nevermind, this actually sucks, and I want to uninstall it.

Thankfully, the install procedure above wasn't anything complicated.
Just run `rm -rf $DIVERGE_DIR` and then delete the lines from the rc/profile file(s) you chose.

