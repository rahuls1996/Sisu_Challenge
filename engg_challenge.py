import os
from sys import getsizeof
import sys
import random
import tempfile


def caller(smaller_file):
    hash_set = ()
    for line in open(smaller_file):
        line = line.strip()
        hash_set.add(int(line))
    close(smaller_file)
    return hash_set



def match_checker(hash_set, file_in_disk):
    counter = 0
    for line in open(file_in_disk):
        if line in hash_set:
            counter+=1
    return counter


def determine_size(input1, input2):
    size_of_first = os.stat(input1)[ST_SIZE]
    size_of_second = os.stat(input2)[ST_SIZE]
    if size_of_first > size_of_second:
        hash_set = caller(input1)
        number_of_matches = match_checker(hash_set, input2)
    else:
        hash_set = caller(input2)
        number_of_matches = match_checker(hash_set, input1)




