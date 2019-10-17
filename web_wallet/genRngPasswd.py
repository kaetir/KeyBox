
import string
import random

def randomString(stringLength=10):
    letters = string.ascii_letters + string.punctuation
    return ''.join(random.choice(letters) for i in range(stringLength))


if __name__ == "__main__":
    print(randomString(10))








