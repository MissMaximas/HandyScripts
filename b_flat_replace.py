""" B Flat Replace

Demoing to someone the different ways you can replace b flat ("♭") in a string
"""
import re

B_FLAT = "♭"
TEST_STRING = "here is my test ♭ string"
REPLACE_VALUE = "b"


def simple_replace():
    print(TEST_STRING.replace(B_FLAT, REPLACE_VALUE))


def regex_replace():
    regex = "♭"
    print(re.sub(regex, REPLACE_VALUE, TEST_STRING))


def ascii_replace():
    ascii_list = [ord(x) for x in TEST_STRING]
    replaced_ascii_list = [ord(REPLACE_VALUE) if code == ord(B_FLAT) else code for code in ascii_list]
    print("".join([chr(x) for x in replaced_ascii_list]))


print(f"Starting string: {TEST_STRING}\nSimple Replace")
simple_replace()
print("Regex Replace")
regex_replace()
print("ASCII replace")
ascii_replace()

# Results:
#
# Starting string: here is my test ♭ string
#
# Simple Replace
# here is my test b string
# Regex Replace
# here is my test b string
# ASCII replace
# here is my test b string
