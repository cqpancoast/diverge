from sys import argv
from urllib.request import urlopen

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

    # Parses ANU page into integer.
    # Adapted: https://github.com/pcragone/anurandom/blob/master/anurandom.py
    anu_url = 'http://150.203.48.55/RawBin.php'
    with urlopen(anu_url) as page:

        # Returns the html of the page as a string, finds the number.
        page_html = page.read().decode()
        measurement_str = page_html.split('<td>\n')[1].split('</td>')[0]

        # Casts binary string to int.
        base = 2
        measurement = int(measurement_str, base)

    # Mods measurement and prints.
    mod_measurement = abs(measurement) % mod_by
    print(mod_measurement)

