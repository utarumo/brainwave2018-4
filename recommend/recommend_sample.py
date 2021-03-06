#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
import csv
import sys


#len_tmp = 1000
file_name = sys.argv[1]


def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def favorite_genre(genre, input_wave):
    max_value = np.inf
    max_genre = ""
    for k,v in genre.items():
        chart_len = min(len(input_wave), len(genre[k]))
        #sim = cos_sim(input_wave[:chart_len], genre[k][:chart_len])
        inp = np.array(input_wave[:chart_len])
        gen = np.array(genre[k][:chart_len])
        se = np.linalg.norm(inp-gen)
        #if  sim > max_value:
        if se < max_value:
            max_value = se
            max_genre = k
    return max_genre

def read_input_wave(csv_file):
    f = open(csv_file)
    reader = csv.reader(f, delimiter=",")
    # header = next(reader)
    # print(header)
    chart = []
    for row in reader:
        chart.append(float(row[0]))
    return chart

def main():
    genre = {}
    genre["K-POP"] = read_input_wave("recommend/kpop.csv")
    genre["ROCK"] = read_input_wave("recommend/rock.csv")
    genre["VOCALOID"] = read_input_wave("recommend/vocaloid.csv")
    genre["EDM"] = read_input_wave(("recommend/edm.csv"))

    input_wave = read_input_wave(file_name)

    #chart_len = min(len_tmp, len(input_wave))

    return favorite_genre(genre, input_wave)

# def move_average(data, n):
#     return np.convolve(data, np.ones(n)/float(n), 'valid')

if __name__ == '__main__':
    #print(read_input_wave("test.csv"))

    print(main())


