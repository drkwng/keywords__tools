import re
import csv


class FilterKeywords:
    """
    Parse a CSV of any size, search terms by RegEx and write found data into CSV
    """
    def __init__(self, _terms_file, _work_file, _res_file, _separator):
        """
        :param _terms_file: Search terms (1 term 1 line) .txt filename
        :type _terms_file: str
        :param _work_file: Original CSV filename
        :type _work_file: str
        :param _res_file: Result CSV filename
        :type _res_file: str
        :param _separator: CSV separator
        :type _separator: str
        """
        self.terms = _terms_file
        self.my_csv = _work_file
        self.res_csv = _res_file
        self.sep = _separator

    def read_terms(self):
        """
        Read .txt file and join into RegEx str
        :return: Joined lines by '|' symbol
        :rtype: str
        """
        all_terms = []
        with open(self.terms, 'r', encoding='utf-8') as file:
            for line in file:
                all_terms.append(line.strip())
        return '|'.join(all_terms)

    def writer(self, row, mode):
        """
        Write found data into CSV
        :param row: Found row
        :type row: list
        :param mode: File open mode
        :type mode: str
        :return:
        :rtype:
        """
        with open(self.res_csv, mode, encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=self.sep)
            writer.writerow(row)

    def worker(self):
        terms = self.read_terms()

        with open(self.my_csv, 'r', encoding='utf-8', newline='') as file:
            reader = csv.reader(file, delimiter=self.sep)
            self.writer(next(reader), 'w')

            for row in reader:
                if re.search(terms, row[0]):
                    self.writer(row, 'a')


if __name__ == '__main__':
    work_file = 'filter_file.csv'
    terms_file = 'filter_terms.txt'
    res_file = 'result_filter.csv'

    kw_filter = FilterKeywords(terms_file, work_file, res_file, ';')
    kw_filter.worker()
