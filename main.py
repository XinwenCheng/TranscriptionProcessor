# coding=utf-8
import itertools
import string

import inflect

p_inflect = inflect.engine()

LINE_BREAK = '\n'
DOUBLE_BLANK_SPACES = '  '
EMPTY_STRING = ''
BLANK_SPACE = ' '
DOT = '.'
COLON = ':'


def main():
    input_file_name = 'matrix.txt'
    output_file_name = 'corpus.txt'
    output_lines = []

    with open(input_file_name, 'r') as input_file:
        lines = input_file.readlines()

    if is_empty_array(lines):
        print 'File is empty.'
        return

    for line in lines:
        # Description (xinwen.cheng@easyto.com): Ignore empty lines.
        if is_empty_string(line):
            continue
        output_lines += parse_to_output_lines(line)

    with open(output_file_name, 'w') as output_file:
        output_file.writelines(output_lines)

    print "DONE with %s lines." % output_lines.__len__()


def parse_to_output_lines(str):
    results = []

    if is_empty_string(str):
        return results

    if str.__contains__(COLON):
        str = str.split(COLON)[1]

    str = strip_punctuation(str)

    if str is None:
        return results

    if contains_number(str):
        print str
        return results  # TODO: Shouldn't return, but represent number to string.

    elements = str.split(DOT)

    for element in elements:
        if is_empty_string(element):
            continue
        element = element.strip(BLANK_SPACE).strip(LINE_BREAK)
        # Description (xinwen.cheng@easyto.com): Ignore line which only contains a single word.
        if element.split(BLANK_SPACE).__len__() < 2:
            print 'Ignore line: %s' % element
            continue

        results.append('<s> %s </s>\n' % element.lower())

    return results


def strip_punctuation(str):
    if is_empty_string(str):
        return None

    str = str.replace("won't", ' would not') \
        .replace("can't", 'cannot') \
        .replace("n't", ' not') \
        .replace("'re", ' are') \
        .replace("'s", ' is') \
        .replace("'m", ' am') \
        .replace("'d", ' would') \
        .replace("'ll", ' will') \
        .replace("s' ", 's ') \
        .replace("'ve ", ' have ')
    str = str.translate(None, string.punctuation.replace(DOT, EMPTY_STRING))

    while str.__contains__(DOUBLE_BLANK_SPACES):
        str = str.replace(DOUBLE_BLANK_SPACES, BLANK_SPACE)

    return str.strip()


def contains_number(str):
    for _ in itertools.ifilter(string.digits.__contains__, str):
        return True
    return False


def is_empty_string(str):
    return str is None or str == EMPTY_STRING or str == LINE_BREAK


def is_empty_array(array):
    return array is None or array.__len__() == 0


main()
