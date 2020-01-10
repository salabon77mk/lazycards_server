#!/usr/bin/python3

MIN_ARGS = 3


def check_arg(args):
    if len(args) < MIN_ARGS:
        print("Too few arguments")
        exit()
