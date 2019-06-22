import os
from sys import getsizeof
import sys
import random
import tempfile
import math
from itertools import islice


def caller(smaller_file, memory, size, file_2):
    counter = 0
    memory = int(memory)*(10**6)
    chunk = float(size)
    file = open(smaller_file)
    print(size)
    #deciding chunk size as a function of available memory
    while chunk > (memory/4):
        chunk = chunk/2
    number_of_lines = math.ceil(chunk/18)
    while True:
        hash_set = set()
        next_n_lines = list(islice(file, number_of_lines))
        if not next_n_lines:
            break
        for element in next_n_lines:
            hash_set.add(int(element.strip()))
        counter+=match_checker(hash_set, file_2)

#    for line in open(smaller_file):
#       line = line.strip()
#       hash_set.add(int(line))
    return counter


def match_checker(hash_set, file_in_disk):
    counter = 0
    for line in open(file_in_disk):
        if int(line.strip()) in hash_set:
            counter+=1
    return counter



def determine_size(input1, input2, available_memory):
    size_of_first = os.stat(input1).st_size
    size_of_second = os.stat(input2).st_size
    if size_of_first > size_of_second:
        hash_set = caller(input1,available_memory,size_of_first,input2)
        number_of_matches = match_checker(hash_set, input2)
    else:
        hash_set = caller(input2,available_memory,size_of_second,input1)
        number_of_matches = match_checker(hash_set, input1)
    return number_of_matches

number = determine_size(sys.argv[1],sys.argv[2], sys.argv[3])

#print(number)
