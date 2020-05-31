from sys import argv
from urllib.request import urlopen

def main():
    """Queries ANU random number measurement lab and mods the huge
    number obtained from there with a command line argument."""

    # Determines what number to mod measurement by using input argv
    mod_by = 2 if len(argv) == 1 else int(argv[1])
    if mod_by < 1:
        raise ValueError("Mod argument must be 1 or above, got: {}".format(mod_by))

    # Gets the page.
    # Adapted from https://github.com/pcragone/anurandom/blob/master/anurandom.py
    anu_url = 'http://150.203.48.55/RawBin.php'
    with urlopen(anu_url) as page:

        # Returns the html of the page as a string, finds the number
        page_html = page.read().decode()
        measurement_str = page_html.split('<td>\n')[1].split('</td>')[0]

        # Cast binary string to int
        base = 2
        measurement = int(measurement_str, base)

    # Mods measurement and prints
    mod_measurement = abs(measurement) % mod_by
    print(mod_measurement)

