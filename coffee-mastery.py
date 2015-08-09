#!/usr/bin/python
#
#

import os.path
from sets import Set
import sys


class Mastery():
    """
    """

    def __init__(self):
        """
        """
        pass

    def check(self, tokenList):
        """
        """
        tokenSet = Set(tokenList)

        if self.advanced.intersection(tokenSet):
            return 3
        if self.intermediate.intersection(tokenSet):
            return 2
        if self.basic.intersection(tokenSet):
            return 1
        else:
            return 0


class Abstraction(Mastery):
    """
    """

    def __init__(self):
        """
        """
        self.basic = Set(["->"])
        self.intermediate = Set([])  # FIXME
        self.advanced = Set([])  # FIXME


class Parallelism(Mastery):
    """
    """

    def __init__(self):
        """
        """
        self.basic = Set([])  # FIXME
        self.intermediate = Set([])  # FIXME
        self.advanced = Set([])  # FIXME


class Logic(Mastery):
    """
    """

    def __init__(self):
        """
        """
        self.basic = Set(["if"])
        self.intermediate = Set(["else"])
        self.advanced = Set(["and", "or", "not"])


class Synchronization(Mastery):
    """
    """

    def __init__(self):
        """
        """
        self.basic = Set([])  # FIXME
        self.intermediate = Set([])  # FIXME
        self.advanced = Set([])  # FIXME


class Flow(Mastery):
    """
    """

    def __init__(self):
        """
        """
        self.basic = Set(["for", "while", "forever"])
        self.intermediate = Set(["button", "keydown", "click"])
        self.advanced = Set([])  # FIXME


class Interactivity(Mastery):
    """
    """

    def __init__(self):
        """
        """
        self.basic = Set(["read", "pressed"])
        self.intermediate = Set(["play", "tone"])
        self.advanced = Set(["Audio"])


class Data_representation(Mastery):
    """
    """

    def __init__(self):
        """
        """
        self.basic = Set(["="])
        self.intermediate = Set(["new"])
        self.advanced = Set([])  # FIXME


if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("Usage: python coffee-mastery.py filename.coffee")

    coffeefile = sys.argv[1]

    if not os.path.exists(coffeefile):
        print "Error: filename does noe exist"
        sys.exit("Usage: python coffee-mastery.py filename.coffee")

    with open(coffeefile) as filed:
        code = filed.read()

    tokenList = code.replace('[', '').replace(']', '').split()

    print tokenList
    print "Abstraction:", Abstraction().check(tokenList)
    print "Parallelism:", Parallelism().check(tokenList)
    print "Logic:", Logic().check(tokenList)
    print "Synchronization:", Synchronization().check(tokenList)
    print "Flow:", Flow().check(tokenList)
    print "Interactivity:", Interactivity().check(tokenList)
    print "Data representation:", Data_representation().check(tokenList)
