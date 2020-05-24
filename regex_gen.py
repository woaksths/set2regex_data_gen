import rstr
from utils import file_write

operations = ['[0-3]*', '[0-3]', '(0|1)', '(0|2)', '(0|3)', '(1|2)', '(1|3)', '(2|3)',\
              '(0|1|2)', '(0|1|3)', '(0|2|3)', '(1|2|3)', '*']

regex_set0 = set()
regex_set1 = set()
regex_set2 = set()
regex_set3 = set()
set_size = 55000


while len(regex_set0) < set_size or len(regex_set1) < set_size or len(regex_set2) < set_size \
        or len(regex_set3) < set_size:

    regex_instance = rstr.rstr([rstr.rstr('0123*', 0, 4) for _ in range(30)]+operations, 7)
    star_cnt = regex_instance.count('*')

    if regex_instance.strip() == '':
        continue
    if '**' in regex_instance or regex_instance[0] == '*':
        continue

    if star_cnt == 0 and len(regex_set0) < set_size:
        regex_set0.add(regex_instance)
    elif star_cnt == 1 and len(regex_set1) < set_size:
        regex_set1.add(regex_instance)
    elif star_cnt == 2 and len(regex_set2) < set_size:
        regex_set2.add(regex_instance)
    elif star_cnt == 3 and len(regex_set3) < set_size:
        regex_set3.add(regex_instance)
    print(len(regex_set0), len(regex_set1), len(regex_set2), len(regex_set3))


file_write('data/alphabet4/regex/star0.txt', regex_set0)
file_write('data/alphabet4/regex/star1.txt', regex_set1)
file_write('data/alphabet4/regex/star2.txt', regex_set2)
file_write('data/alphabet4/regex/star3.txt', regex_set3)


