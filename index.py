import sys
import argparse

parser = argparse.ArgumentParser(description='Sapin Generator.')
parser.add_argument('dimension', type=int,
                    help='an integer describing the dimension/size of the generated Sapin.')

args = parser.parse_args()

dimension = args.dimension


def printWithoutSpacing(string):
    sys.stdout.write(string)


def create_tronc_for_one(dimension, base):

    x = 0
    while x < dimension:
        i = 0
        while i < base:
            if i == (((base/2)-1)-(dimension/2)):
                j = 0
                while j < dimension:
                    printWithoutSpacing('|'),
                    j += 1
            else:
                printWithoutSpacing(' '),
            i += 1
        print('\n')
        x += 1


def display_pipes(dimension):
    i = 0
    if dimension % 2 == 0:
        while i < dimension+1:
            printWithoutSpacing('|'),
            i += 1
    else:
        while i < dimension:
            printWithoutSpacing('|'),
            i += 1


def create_tronc(dimension, base):

    x = 0
    while (x < dimension):
        i = 0
        while i < base:
            if i == ((base/2)-(dimension/2)):
                display_pipes(dimension)
            else:
                printWithoutSpacing(' '),
            i += 1
        print('\n'),
        x += 1


def create_sapin_head(base):

    i = 0
    while i < (base / 2)+1:
        j = 0
        while j <= base:
            if j >= (base/2)-i:
                while j <= (base/2)+i:
                    printWithoutSpacing('*'),
                    j += 1
            else:
                printWithoutSpacing(' '),
            j += 1
        i += 1
        print('\n'),


def get_max_lines(dimension):

    i = 0
    base = 7
    spacesToRemove = 0
    lines = 4
    linesTmp = lines

    while i < dimension-1:
        if (i % 2) == 0:
            spacesToRemove += 2
        base = (base - spacesToRemove) + ((lines+i) * 2)
        maxLineNbr = lines + (linesTmp+(i+1))
        linesTmp = maxLineNbr
        i += 1

    return maxLineNbr


def get_current_base(dimension):

    i = 0
    base = 7
    spacesToRemove = 0
    lines = 4
    while i < dimension-1:
        if (i % 2) == 0:
            spacesToRemove += 2
        base = (base - spacesToRemove) + ((lines+i) * 2)
        i += 1

    return base


def display_space_and_stars(line, spacesToRemove, base):

    j = 0
    while j <= base:
        if j >= ((base/2)-line)+spacesToRemove:
            while j <= ((base/2)+line)-spacesToRemove:
                printWithoutSpacing('*'),
                j += 1
        else:
            printWithoutSpacing(' '),
        j += 1
    print('\n'),


def do_sapin(dimension, base, maxLines, defaultLines):
    i = 0
    j = 0
    toAdd = 0
    randomAddRow = 0

    while i < maxLines:
        if i == defaultLines:
            if j == 0:
                randomAddRow = 2
            if j > 0:
                if (j % 2) == 0:
                    toAdd = toAdd + 1
                randomAddRow = randomAddRow + (toAdd+2)
            defaultLines = defaultLines + (4+(1+j))
            j += 1
        display_space_and_stars(i, randomAddRow, base)
        i += 1


def generate_sapin(dimension):

    index = 0
    base = 7
    defaultLines = 4

    if dimension == 1:
        create_sapin_head(defaultLines)
        create_tronc_for_one(dimension, base)
        return

    maxLines = get_max_lines(dimension)
    base = get_current_base(dimension)
    do_sapin(dimension, base, maxLines, defaultLines)
    create_tronc(dimension, base)


print('\n')
generate_sapin(dimension)