#!/usr/bin/env python3

# created by: Trinity Armstrong
# created on: September 2019
# This program calculates the circumference of a rectangle
# with user input

import constant


def main():
    # this function calculates circumference

    # input
    radius = int(input("Enter length of the circle (mm): "))

    # process
    circumference = constant.TAU*radius

    # output
    print("")
    print("Circumference is {}mm^2".format(circumference))


if __name__ == "__main__":
    main()
