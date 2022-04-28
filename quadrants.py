#!/usr/bin/env python3

# Created by Aidan Lalonde-Novales
# Created April 2022
# This program receives an XY coordinate, then tells the user
# what quadrant (I, II, III, IV) that coordinate lies in.


def main():
    # this function finds out what quadrant an XY coordinate is in

    # input
    x_coord_string = input("Enter your X coordinate: ")
    y_coord_string = input("Enter your Y coordinate: ")

    # process & output
    try:

        x_coord = float(x_coord_string)
        y_coord = float(y_coord_string)

        if x_coord > 0 and y_coord > 0:
            print("\nYour coordinate is in quadrant I.")
        elif x_coord < 0 and y_coord > 0:
            print("\nYour coordinate is in quadrant II.")
        elif x_coord < 0 and y_coord < 0:
            print("\nYour coordinate is in quadrant III.")
        elif x_coord > 0 and y_coord < 0:
            print("\nYour coordinate is in quadrant IV.")
        elif x_coord == 0 and y_coord == 0:
            print("\nYour coordinate is on the origin.")
        else:
            print("\nYour coordinate is between quadrants.")

    except Exception:
        print("\nInvalid Coordinates. Please Re-Run.")

    print("\nDone.")


if __name__ == "__main__":
    main()
