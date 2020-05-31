from sys import argv
from urllib.request import urlopen

# Determines what number to mod measurement by using input argv
mod_by = 2 if len(argv) == 1 else int(argv[1])
if mod_by < 1:
    raise ValueError("Mod argument must be 1 or above, got: {}".format(mod_by))

# Gets the page
anu_url = 'http://150.203.48.55/RawBin.php'
with urlopen(anu_url, timeout=5) as page:

    # Returns the html of the page as a string
    page_html = page.read().decode()

    # Finds the portion of the html where the random number is, casts to int
    measurement = int(page_html.split('<td>\n')[1].split('</td>')[0])

# Mods measurement and prints
mod_measurement = abs(measurement) % mod_by
print(mod_measurement)

