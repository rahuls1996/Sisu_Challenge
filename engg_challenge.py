import os
from sys import getsizeof
import sys
import random
import tempfile
import math
from itertools import islice
from memprof import memprof

@memprof
def caller(smaller_file, memory, size, file_2):
    counter = 0
    number_of_lines = calculate_chunk(size,memory)
    file = open(smaller_file)
    #deciding chunk size as a function of available memory
    while True:
        hash_set = set()
        next_n_lines = list(islice(file, number_of_lines))
        if len(next_n_lines) == 0:
            break
        for element in next_n_lines:
            hash_set.add(int(element.strip()))
        counter += match_checker(hash_set, file_2)
    return counter


def calculate_chunk(size,memory):
    memory = int(memory)*(10**6)
    chunk = float(size)
    while chunk > (memory/4):
        chunk = chunk/2
    number_of_lines = math.ceil(chunk/18)
    return number_of_lines
    



def match_checker(hash_set, file_in_disk):
    counter = 0
    for line in open(file_in_disk):
        if int(line.strip()) in hash_set:
            counter+=1
    return counter



def calculate_intersection(input1, input2, available_memory):
    size_of_first = os.stat(input1).st_size
    size_of_second = os.stat(input2).st_size
    if size_of_first > size_of_second:
        
        number_of_matches = caller(input2,available_memory,size_of_second,input1)
    else:
        number_of_matches = caller(input1,available_memory,size_of_first,input2)
    return number_of_matches



number = calculate_intersection(sys.argv[1],sys.argv[2], sys.argv[3])
print(number)


