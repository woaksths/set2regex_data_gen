import rstr


def get_instance_list(regex, set_num):
    instance_set = set()
    early_stop_cnt = 0
    while len(instance_set) < set_num:
        regex = regex.replace('*', '{0,4}')
        string = rstr.xeger(regex)
        if early_stop_cnt == 30:
            break

        if string in instance_set:
            early_stop_cnt += 1
            continue

        if len(string) < 50:
            instance_set.add(string)
            early_stop_cnt = 0

    instance_list = list(instance_set)
    instance_list.sort()
    return instance_list


def process_target(regex):
    regex = list(regex)
    regex = ' '.join(regex)
    regex = regex.replace('[ 0 - 3 ] *', '[0-3]*')
    regex = regex.replace('[ 0 - 3 ]', '[0-3]')
    return regex


def process_source(source_list):
    for i in range(len(source_list)):
        if source_list[i] == 'none':
            continue
        source_list[i] = list(source_list[i])
        source_list[i] = ' '.join(source_list[i])
    return source_list


def fill_none_token(dataset, filled_num, maximum_set):
    none_token = ['none']
    set2regex_dataset = []
    seq2seq_dataset = []

    for data in dataset:
        data = data.split('\t')
        regex = data[-1]
        strings = data[:-1] + none_token*filled_num
        strings = strings[:maximum_set]
        seq2seq_dataset.append(' <sep> '.join(strings)+'\t'+regex)
        set2regex_dataset.append('\t'.join(strings+[regex]))

    return seq2seq_dataset, set2regex_dataset