__author__ = 'student'
import os
import sys
import math
from heapq import*

import array

import statistics

from matplotlib import rc
rc('font', family='Droid Sans', weight='normal', size=14)

import matplotlib.pyplot as plt


class WikiGraph:

    def load_from_file(self, filename):
        print('Загружаю граф из файла: ' + filename)

        with open(filename) as f:
            self._n, self._nlinks = map(int, f.readline().split())
            
            self._titles = []
            self._sizes = array.array('L', [0]*self._n)
            self._links = array.array('L', [0]*self._nlinks)
            self._redirect = array.array('B', [0]*self._n)
            self._offset = array.array('L', [0]*(self._n+1))
            self._offset[0] = 0
            last = 0

            for i in range(self._n):
                title = f.readline()
                sz, re, ln = map(int, f.readline().split())
                title = list(title)
                t = title[0:-1]
                t = ''.join(t)
                self._titles.append(t)
                self._sizes[i] = sz
                self._redirect[i] = re
                self._offset[i+1] = self._offset[i] + ln
                for j in range(ln):
                    self._links[last] = int(f.readline())
                    last += 1

        print('Граф загружен')

    def get_number_of_links_from(self, _id):
        return self._offset[_id + 1] - self._offset[_id]

    def get_links_from(self, _id):
        return self._links[self._offset[_id] : self._offset[_id + 1]]

    def get_id(self, title):
        return self._titles.index(title)

    def get_number_of_pages(self):
        return self._n

    def is_redirect(self, _id):
        fl = self._redirect[_id]
        if fl == 0:
            return False
        else:
            return True

    def get_title(self, _id):
        return self._titles[_id]

    def get_page_size(self, _id):
        return self._sizes[_id]

    def dijkstra(self, startname):
        start = self.get_id(startname)
        d = {v: float('+inf') for v in range(self._n)}
        d[start] = 0
        Q = [(0, start)]
        used = set()
        paths = {start: [self.get_title(start)]}
        work = set(range(self._n))
        while Q:
            d_c, current = heappop(Q)
            if d_c != d[current]:
                continue
            for neighbor in self.get_links_from(current):
                l = d[current] + 1
                if l < d[neighbor]:
                    d[neighbor] = l
                    heappush(Q, (l, neighbor))
                    paths[neighbor] = [i for i in paths[current]]
                    paths[neighbor].append(self.get_title(neighbor))
            used.add(current)
        return paths


def hist(fname, data, bins, xlabel, ylabel, title, facecolor='green', alpha=0.5, transparent=True, **kwargs):
    plt.clf()
    # TODO: нарисовать гистограмму и сохранить в файл

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Использование: wiki_stats.py <файл с графом статей>')
        sys.exit(-1)

    if os.path.isfile(sys.argv[1]):
        wg = WikiGraph()
        wg.load_from_file(sys.argv[1])
    else:
        print('Файл с графом не найден')
        sys.exit(-1)

    # TODO: статистика и гистограммы

