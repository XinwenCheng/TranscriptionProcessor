def dict_preprocess():
    dict_file = open('dict_1.8w.txt', 'r')
    lines = dict_file.readlines()
    outputs = []

    for line in lines:
        if line.__contains__(' / ') is False:
            continue
        outputs.append('%s\n' % line.split(' / ')[0])

    outputs.sort()

    with open('refer_dict.txt', 'w') as refer_dict:
        refer_dict.writelines(outputs)

    print('*** DONE ***')


def dict_process():
    dict_file = open('cmudict-en-us.dict', 'r')
    lines = dict_file.readlines()
    refer_dict = open('refer_dict.txt', 'r')
    words = refer_dict.readlines()
    outputs = []
    latestOutputFirstLetter = ''

    for line in lines:
        item = line.split('(')[0].split(' ')[0]

        if latestOutputFirstLetter != item[0]:
            latestOutputFirstLetter = item[0]
            print('%s %d' % (item, outputs.__len__()))

        for word in words:
            if item.lower() == word.lower().strip('\n'):
                # print(line)
                outputs.append(line)
                break

    with open('cmudict-en-us.txt', 'w') as output_dict:
        output_dict.writelines(outputs)

    print('*** DONE ***')


def prune_language_model():
    pass


if __name__ == '__main__':
    dict_process()
