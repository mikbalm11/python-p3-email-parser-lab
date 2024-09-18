import re

class EmailAddressParser:

    def __init__(self, string):
        self.string = string

    def parse(self):
        newList = (re.split(' ,|, | |,', self.string))
        newList = [x for x in newList if '@' in x]
        return sorted(set(newList))
