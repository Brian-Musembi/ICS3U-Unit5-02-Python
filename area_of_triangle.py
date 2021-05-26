#!/usr/bin/env python3

# Created by Brian Musembi
# Created on May 2021
# This program calculates the area of a triangle


def areaOfTriangle(base, height):
    # this function calculates the area of a triangle

    # process
    area_of_triangle = (base * height) / 2

    # output
    print("The area of your triangle is {} cm².".format(area_of_triangle))


def main():
    # this function gets base and height

    # input
    base_of_triangle = input("Enter the base length of the triangle (cm): ")
    height_of_triangle = input("Enter the height of the triangle (cm): ")
    print("")

    try:
        base_int = int(base_of_triangle)
        height_int = int(height_of_triangle)

        if base_int > 0 and height_int > 0:
            # call function
            areaOfTriangle(base_int, height_int)
        else:
            # output
            print("Enter a positive integer for both dimensions, try again.")

    except Exception:
        # output
        print("Enter a number for both dimensions, try again.")


if __name__ == "__main__":
    main()
