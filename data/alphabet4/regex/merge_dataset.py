from utils import get_dataset
from utils import file_write

import os
set_size = ['set5'] + ['set{}'.format(i) for i in range(10, 110, 10)]
max_set = ['max_set20', 'max_set50', 'max_set100']

for max_set_val in max_set:
    seq2seq_train = [] 
    seq2seq_valid = []
    seq2seq_test = []

    set2regex_train = []
    set2regex_valid = []
    set2regex_test = []

    for set_val in set_size:
        set_num = int(set_val.replace('set',''))
        max_set_num = int(max_set_val.replace('max_set',''))
        if set_num > max_set_num:
            continue
        prefix_path = '{}/{}'.format(set_val, max_set_val)

        for model_type in ['seq2seq','set2regex']:
            path = prefix_path + '/'+model_type

            if model_type == 'seq2seq':
                for f_name in os.listdir(path):
                    f_name = path + '/' + f_name
                    if 'train' in f_name:
                        seq2seq_train.extend(get_dataset(f_name))
                    elif 'valid' in f_name:
                        seq2seq_valid.extend(get_dataset(f_name))
                    elif 'test' in f_name:
                        seq2seq_test.extend(get_dataset(f_name))

            elif model_type == 'set2regex':
                for f_name in os.listdir(path):
                    f_name = path + '/' + f_name
                    if 'train' in f_name:
                        set2regex_train.extend(get_dataset(f_name))
                    elif 'valid' in f_name:
                        set2regex_valid.extend(get_dataset(f_name))
                    elif 'test' in f_name:
                        set2regex_test.extend(get_dataset(f_name))

    file_write('../total/{}/seq2seq/train.txt'.format(max_set_val), seq2seq_train)
    file_write('../total/{}/set2regex/train.txt'.format(max_set_val), set2regex_train)

    file_write('../total/{}/seq2seq/valid.txt'.format(max_set_val), seq2seq_valid)
    file_write('../total/{}/set2regex/valid.txt'.format(max_set_val), set2regex_valid)

    file_write('../total/{}/seq2seq/test.txt'.format(max_set_val), seq2seq_test)
    file_write('../total/{}/set2regex/test.txt'.format(max_set_val), set2regex_test)
