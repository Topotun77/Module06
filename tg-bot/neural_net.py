# -*- coding: utf-8 -*-

# Сделать генератор текста на основе статистики
# Идея проста: подсчитаем какие буквы наиболее часто стоят рядом
# Точнее, подсчитаем как часто за буковой Х идет буква У, на основе некоего текста.
# После этого начнем с произвольной буквы и каждую следующую будем выбирать в зависимости от
# частоты её появления в статистике.
import zipfile
from pprint import pprint

from random import randint


class Chatterer:
    analize_count = 10

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        self.sequence = ' ' * self.analize_count
        with open(self.file_name, 'r', encoding='utf-8') as file:
            for line in file:
                # print(line, end='')
                self._collect_for_line(line=line)
                # self._collect_for_line(line=line[:-1])
        # pprint(self.stat)

    def _collect_for_line(self, line):
        for char in line:
            if self.sequence in self.stat:
                if char in self.stat[self.sequence]:
                    self.stat[self.sequence][char] += 1
                else:
                    self.stat[self.sequence][char] = 1
            else:
                self.stat[self.sequence] = {char: 1}
            self.sequence = self.sequence[1:] + char

    def prepare(self):
        self.totals = {}
        self.stat_for_generate = {}
        for sequence, char_stat in self.stat.items():
            self.totals[sequence] = 0
            self.stat_for_generate[sequence] = []
            for char, count in char_stat.items():
                self.totals[sequence] += count
                self.stat_for_generate[sequence].append([count, char])
                self.stat_for_generate[sequence].sort(reverse=True)

    def chat(self, N=1000, out_file_name=None, space_num=10, start_txt=None):
        # N = 200
        printed = 0

        if out_file_name is not None:
            if out_file_name != 'return':
                file_ = open(out_file_name, 'w', encoding='utf-8')
            else:
                return_txt = ''
                file_ = None
        else:
            file_ = None

        if start_txt:
            if len(start_txt) < self.analize_count:
                start_txt = ' ' * (self.analize_count - len(start_txt)) + start_txt
            for i in range (len(start_txt)-self.analize_count):
                if i == 0 or start_txt[i-1] == ' ':
                    win_txt = start_txt[i:i+self.analize_count]
                    if win_txt in self.stat:
                        sequence = win_txt
                        return_txt += sequence
                        break
            else:
                return_txt = f'На фразу "{start_txt}" ничего не могу ответить. Спросите что-нибудь еще.'
                print(return_txt)
                if out_file_name == 'return':
                    return [False, return_txt]
                else:
                    if file_:
                        file_.write(return_txt)
                        file_.close()
                    return [False]
        else:
            sequence = ' ' * self.analize_count

        # sequence = 'Брайен не '
        if file_:
            file_.write(sequence[0].upper() + sequence[1:])
        else:
            print()
        spaces_printed = 0
        while printed < N:
            char = self._get_char(char_stat=self.stat_for_generate[sequence], total=self.totals[sequence])
            if file_:
                file_.write(char)
            elif out_file_name == 'return':
                return_txt += char
            else:
                print(char, end='')
            if char == ' ':
                spaces_printed += 1
                if space_num and spaces_printed >= space_num:
                    if file_:
                        file_.write('\n')
                    elif out_file_name == 'return':
                        return_txt += '\n'
                    else:
                        print()
                    spaces_printed = 0
            printed += 1
            sequence = sequence[1:] + char
        if file_:
            file_.close()
        if out_file_name == 'return':
            return_txt = return_txt[0].upper() + return_txt[1:]
            return [True, return_txt]
        else:
            return True

    def _get_char(self, char_stat, total):
        dice = randint(1, total)
        pos = 0
        for count, char in char_stat:
            pos += count
            if dice <= pos:
                break
        return char


if __name__ == '__main__':
    chatterer = Chatterer(file_name='text.txt')
    chatterer.collect()
    chatterer.prepare()
    # chatterer.chat(N=10000, out_file_name='out.txt')
    re_txt = chatterer.chat(N=200, out_file_name='return', space_num=0,
                         start_txt='Свобода - это рабство! Я бы хотел уточнить война - это мир! занимательный момент, котоый случился со мной недавно')
    print('\nМой ответ: ', re_txt)