import os
from sys import getsizeof
import sys
import random

random_sample_1 = random.sample(range(0,((2**63)-1)),100)

with open('/Users/rahulshahaney/Github/Sisu_Challenge/test_cases/file_2', 'w') as f:
    for item in random_sample_1:
        f.write("%s\n" % item)


random_sample_2 = random.sample(range(0,((2**63)-1)),1000)
with open('/Users/rahulshahaney/Github/Sisu_Challenge/test_cases/file_3', 'w') as f:
    for item in random_sample_1:
        f.write("%s\n" % item)


random_sample_1 = random.sample(range(0,((2**63)-1)),1000000)
with open('/Users/rahulshahaney/Github/Sisu_Challenge/test_cases/file_4', 'w') as f:
    for item in random_sample_1:
        f.write("%s\n" % item)

random_sample_1 = random.sample(range(0,((2**63)-1)),10)
with open('/Users/rahulshahaney/Github/Sisu_Challenge/test_cases/file_1', 'w') as f:
    for item in random_sample_1:
        f.write("%s\n" % item)

random_sample_1 = random.sample(range(0,((2**63)-1)),1000000)
with open('/Users/rahulshahaney/Github/Sisu_Challenge/test_cases/file_5', 'w') as f:
    for item in random_sample_1:
        f.write("%s\n" % item)
