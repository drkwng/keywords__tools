# Made by @drkwng (https://github.com/drkwng/keywords__tools)
# Visit my Telegram Channel (https://t.me/drkwng)
# Website: https://drkwng.rocks

import csv
from itertools import chain, combinations, permutations, product


class KeywordsGenerator:
    """
    Generates combinations of keywords based on lists of queries in CSV
    """
    def __init__(self, _filename, _mode='full'):
        self.filename = _filename
        self.mode = _mode

    def get_queries(self):
        """
        Open CSV file and get basis phrases with
        :return: A dictionary with basis phrases
        :rtype: dict
        """
        with open(self.filename, 'r', encoding='utf-8') as file:
            file_data = csv.DictReader(file, delimiter=';')
            all_dicts = [dict(i) for i in file_data]

        final_dict = {}
        for elem in all_dicts:
            for key in elem.keys():
                if len(elem[key]):
                    if key in final_dict.keys():
                        final_dict[key].append(elem[key].lower())
                    else:
                        final_dict[key] = [elem[key].lower()]
        return final_dict

    @staticmethod
    def powerset(iterable):
        iterable = list(iterable)
        return chain.from_iterable(
            combinations(iterable, r)
            for r, _ in enumerate(iterable, start=1))

    def perm_powerset(self, iterable):
        """
        Generates permuted combinations of sets
        :param iterable:
        :type iterable:
        :return: Generator of elements
        """
        for each_set in self.powerset(iterable):
            for elem in permutations(each_set):
                yield elem

    def worker(self, _res_file):
        with open(_res_file, 'w', encoding='utf-8') as res:
            if self.mode == 'full':
                for elem in self.perm_powerset(chain.from_iterable(self.get_queries().values())):
                    res.write(" ".join(elem) + '\n')

            elif self.mode == 'all-to-all':
                values = self.get_queries().values()
                for keyword in product(*values):
                    res.write(" ".join(keyword) + '\n')

            else:
                print("You've set the wrong 'mode'. Please choose one of the following: \n"
                      "full, all-to-all, all-to-all_permuted")
                exit()


if __name__ == '__main__':
    filename = 'example_keys_gen.csv'
    res_file = 'result.txt'

    mode = 'full'
    # modes supported:
    # full (default) - all possible unique combinations permuted (ALL, CAAAAAAARL)
    # all-to-all - all to all unique combinations (not permuted). This means that basis1 queries would be

    keywords = KeywordsGenerator(filename, mode)
    keywords.worker(res_file)
    print(f'Done! Check the {res_file}')
