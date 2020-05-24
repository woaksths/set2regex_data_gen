import os


def file_write(file_name, regex_set):
    directory = file_name.split('/')[-1]
    path = file_name.replace(directory, '')

    if not os.path.exists(path):
        os.makedirs(path)

    with open(file_name, 'w') as fw:
        for idx, regex in enumerate(regex_set):
            if idx == len(regex_set)-1:
                fw.write(regex)
            else:
                fw.write(regex + '\n')


def get_dataset(f_names):
    with open(f_names, 'r') as rf:
        dataset = rf.read().split('\n')
    return dataset



