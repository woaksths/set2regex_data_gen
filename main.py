from utils import get_dataset, file_write
from string_gen import get_instance_list, process_target, process_source, fill_none_token


def main():
    set_list = ['set5'] + ['set{}'.format(i) for i in range(10, 110, 10)]
    prefix_path = 'data/alphabet4/regex/'
    star_num = [0, 1, 2, 3]
    max_set = [20, 50, 100]

    for set_dir in set_list:
        path = prefix_path + set_dir
        set_num = int(set_dir.replace('set', '').strip())

        for star_idx in star_num:
            star_file = '/star{}.txt'.format(star_idx)
            file_path = path + star_file
            regex_set = get_dataset(file_path)
            pairs_data = []

            for regex in regex_set:
                pairs = []
                strings = get_instance_list(regex, set_num)
                strings = process_source(strings)

                if set_num - len(strings) > 0:
                    for _ in range(set_num - len(strings)):
                        strings.append('none')

                pairs.extend(strings)
                regex = process_target(regex)
                pairs.append(regex)
                pairs = '\t'.join(pairs)
                pairs_data.append(pairs)

            for maximum_set in max_set:
                diff = maximum_set - set_num
                if set_num > maximum_set:
                    diff = 0

                seq2seq_data, set2regex_data = fill_none_token(pairs_data, diff, maximum_set)
                print('set_dir {}, maximum_set{}'.format(set_dir, maximum_set))
                print(len(seq2seq_data[-1].split('<sep>'))+1)
                print(len(set2regex_data[-1].split('\t')))
                test_ratio = int(len(seq2seq_data) * 0.1)
                seq2seq_test = seq2seq_data[0:test_ratio]
                seq2seq_valid = seq2seq_data[test_ratio:2*test_ratio]
                seq2seq_train = seq2seq_data[2*test_ratio:]
                train_fname = path + '/max_set{}/seq2seq/star{}_train.txt'.format(maximum_set, star_idx)
                test_fname = path + '/max_set{}/seq2seq/star{}_test.txt'.format(maximum_set, star_idx)
                valid_fname = path + '/max_set{}/seq2seq/star{}_valid.txt'.format(maximum_set, star_idx)
                file_write(train_fname, seq2seq_train)
                file_write(test_fname, seq2seq_test)
                file_write(valid_fname, seq2seq_valid)

                set2regex_test = set2regex_data[0:test_ratio]
                set2regex_valid = set2regex_data[test_ratio:2*test_ratio]
                set2regex_train = set2regex_data[2*test_ratio:]
                train_fname = path + '/max_set{}/set2regex/star{}_train.txt'.format(maximum_set, star_idx)
                test_fname = path + '/max_set{}/set2regex/star{}_test.txt'.format(maximum_set, star_idx)
                valid_fname = path + '/max_set{}/set2regex/star{}_valid.txt'.format(maximum_set, star_idx)
                file_write(train_fname, set2regex_train)
                file_write(test_fname, set2regex_test)
                file_write(valid_fname, set2regex_valid)


if __name__ == "__main__":
    main()


