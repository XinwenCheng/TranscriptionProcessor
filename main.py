# coding=utf-8

punctuation_without_dot = """!"#$%&'()*+,-/:;<=>?@[\]^_`{|}~"""


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
        output_lines += parse_to_output_line(line)

    with open(output_file_name, 'w') as output_file:
        output_file.writelines(output_lines)

    print "DONE with %s lines." % output_lines.__len__()


def parse_to_output_line(str):
    if is_empty_string(str):
        return None

    if str.__contains__(':'):
        str = str.split(':')[1]

    str = strip_punctuation(str)

    if str is None:
        return None

    elements = str.split('.')
    results = []

    for element in elements:
        if is_empty_string(element):
            continue
        element = element.strip(' ').strip('\n')
        # Description (xinwen.cheng@easyto.com): Ignore line which only contains a single word.
        if element.split(' ').__len__() < 2:
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
        .replace("'ll", ' will')
    str = str.translate(None, punctuation_without_dot)

    while str.__contains__('  '):
        str = str.replace('  ', ' ')

    return str.strip()


def is_empty_string(str):
    return str is None or str == '' or str == '\n'


def is_empty_array(array):
    return array is None or array.__len__() == 0


main()
