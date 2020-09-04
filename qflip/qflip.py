"""Returns a modded number from the ANU quantum random number generator."""


from sys import argv
from urllib.request import urlopen
from json import dump
from json import load
from os.path import expanduser

def main():
    """Queries ANU random number measurement lab and mods the huge
    number obtained from there with a command line argument castable to
    an integer greater than zero."""

    # Determines what number to mod measurement by using input argv.
    if len(argv) == 1:
        mod_by = 2
    else:
        try:
            mod_by = int(argv[1])
        except ValueError:
            raise ValueError("Expected arg castable to int, received {}."
                             .format(argv[1]))
        if mod_by < 1:
            raise ValueError("Expected int greater than zero, received {}."
                             .format(mod_by))

    meass_store_file = expanduser("~/.qflip")
    bit_size = 10

    mod_measurement = take_measurement(mod_by, meass_store_file, bit_size)

    print(mod_measurement)


def take_measurement(mod_by, meass_store_file, bit_size) -> int:
    """Pops a number off of the json list in the measurements file, mods by
    another number, and returns the result."""

    try:
        f = open(meass_store_file, "r")
        meass = load(f)
        f.close()
    except:
        meass = []

    if len(meass) == 0:
        meass = get_new_measurements(bit_size)

    meas = meass.pop()
    with open(meass_store_file, "w") as f:
        dump(meass, f)

    return meas % mod_by


def get_new_measurements(bit_size,
                         anu_url="https://qrng.anu.edu.au/wp-content/plugins/colours-plugin/get_block_binary.php"):
    """Parses ANU binary page into a list of integers.

    Args:
        bit_size: size of bits to store in the file. Limits the range of
            validity of a given quantum flip — you can't split 2^17 ways
            if the bit size is only 2^10.
        anu_url: page to grab the binary integer from.
    """

    with urlopen(anu_url) as page:

        # Returns the binary number encoded in the page as a string.
        meass_str = page.read().decode()
        meas_size = len(meass_str)
        base = 2
        meass = [int(meass_str[i:i+bit_size], 2)\
                for i in range(0, meas_size - 1, bit_size)]

        return meass
