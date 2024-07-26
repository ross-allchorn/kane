import string
import random
import datetime

def random_alphanumeric(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

filename = random_alphanumeric(5) + ".txt"
message = f"This random named file was created at precisely {datetime.datetime.now():%Y/%m/%d %H:%M:%S}"

with open(filename, "w") as f:
    f.write(message)
