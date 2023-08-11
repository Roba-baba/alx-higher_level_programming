#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    grand_total = 0

    for index in range(len(sys.argv) - 1):
        grand_total += int(sys.argv[index + 1])
    print("{}".format(grand_total))
