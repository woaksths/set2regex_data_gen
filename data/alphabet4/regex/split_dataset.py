from utils import get_dataset, file_write

set_list = ['set5'] + ['set{}'.format(i) for i in range(10, 110, 10)]
regex_files = ['star0.txt', 'star1.txt', 'star2.txt', 'star3.txt']
num = 5000

for regex_file in regex_files:
    dataset = get_dataset(regex_file)
    cnt = 0

    for set_dir in set_list:
        each_set = dataset[cnt:cnt+num]
        cnt += num
        file_name = set_dir +'/' + regex_file
        file_write(file_name, each_set)

