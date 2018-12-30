import string
import random


class Robot(object):
    """Generates a name for a robot in format 2 uppercase letters,
    followed by 3 digits.
    Generated names are stored in set usedNames, so that each robot
    has their own unique name.
    """
    usedNames = set()

    def __init__(self):
        for i in range(100):
            letters = ''.join(random.choices(string.ascii_uppercase, k=2))
            digits = ''.join(random.choices(string.digits, k=3))
            proposedName = letters + digits

            if proposedName not in self.usedNames:
                self.usedNames.add(proposedName)
                self.name = proposedName
                break

        # Panic! All 100 attempt to generate a name have failed!

    def reset(self):
        self.__init__()