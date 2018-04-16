# coding=utf-8

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
        results = parse_to_output_line(line)

        if is_empty_array(results) is False:
            for result in results:
                output_lines.append(result)

    with open(output_file_name, 'w') as output_file:
        output_file.writelines(output_lines)

    print "DONE with %s lines." % output_lines.__len__()


def parse_to_output_line(line):
    if is_empty_string(line):
        return None

    elements = line.split('.')
    results = []

    for element in elements:
        if is_empty_string(element):
            continue
        element = element.strip(' ').strip('\n')
        # Description (xinwen.cheng@easyto.com): Ignore line which only contains a single word.
        if element.split(' ').__len__() < 2:
            print 'Ignore line: %s' % element
            continue
        contains = False
        for r in results:
            if r.lower() == '<s>%s</s>\n' % element.lower():
                contains = True
                continue
        if contains is False:
            results.append('<s>%s</s>\n' % element)

    return results


def is_empty_string(content):
    return content is None or content == '' or content == '\n'


def is_empty_array(array):
    return array is None or array.__len__() == 0


main()
