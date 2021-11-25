# Made by @drkwng (https://github.com/drkwng/keywords__tools)
# Visit my Telegram Channel (https://t.me/drkwng)
# Website: https://drkwng.rocks
import csv


class KeywordsGroup:
    """
    Group keywords by mask map from CSV
    """
    def __init__(self, kw_file, base_file):
        self.kw_file = kw_file
        self.base_file = base_file

    def get_keys(self):
        """
        Get keywords from CSV to dictionary
        :return:
        :rtype: dict
        """
        with open(self.kw_file, 'r', encoding='utf-8', newline='') as file:
            keywords = {}
            reader = csv.reader(file, delimiter=';')
            next(reader)
            for line in reader:
                keywords[line[0]] = [line[1:]]
        return keywords

    def get_basis(self):
        """
        Get base words from CSV to dictionary
        :return:
        :rtype: dict
        """
        with open(self.base_file, 'r', encoding='utf-8', newline='') as file:
            basis = dict()
            reader = csv.reader(file, delimiter=';')
            next(reader)
            for line in reader:
                basis[line[0]] = line[1]
            return basis

    @staticmethod
    def writer(res_dict, res_filename):
        """
        Write dictionary to CSV
        :param res_dict: dictionary with results
        :type res_dict: dict
        :param res_filename: result CSV filename
        :type res_filename: str
        :return:
        :rtype:
        """
        with open(res_filename, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            for key in res_dict.keys():
                row = [key] + res_dict[key][0]
                writer.writerow(row)

    def worker(self, res_filename):
        """
        Group keywords and write to CSV
        :param res_filename: result CSV filename
        :type res_filename: str
        :return:
        :rtype:
        """
        keywords = self.get_keys()
        basis = self.get_basis()
        for term in basis.keys():
            for key in keywords.keys():
                if term in key:
                    keywords[key][0] += [basis[term]]
        self.writer(keywords, res_filename)


if __name__ == '__main__':
    keywords_group = KeywordsGroup('example_keys_group-keywords.csv',
                                   'example_keys_group-base.csv')
    keywords_group.worker('result__keys_group.csv')
