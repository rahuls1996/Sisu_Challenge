# Sisu_Challenge

Engineering problem for Sisu Data

Assumptions - 

1. Implementation assumes the input is stored in ASCII text, with one integer (with value ranging from 0 to 2^63) per line, and that each integer appears at most once in each file.

2. Implementation assumes that the memory budget will be no smaller than 1MB, and the input files will be no larger than 500MB, and should execute as efficiently as possible while respecting the memory budget.

Base logic, without any constraints - 

If memory was not an issue, a efficient way to solve this problem is to load both files into hash sets, and then take the intersection of these two hash sets. 

Time complexity - O(n), where n is the size of the larger set (number of integers in the larger file)
Space Complexity - O(n) where n is the number of integers in the file with more numbers. 

Constraints:

The program should use no more memory than a pre-specified budget.

Optimizing given this constraint - 

Idea - Instead of reading the entire file, compute a variable called 'chunk_size', which is a function of this pre-specified budget. After calculating this chunk_size, we can determine the number of lines to be read from the file as - number_of_lines = chunk_size/18 (as we have a maximum of 18 bytes per line, see assumption 1). We then read these number of lines from file1 into a hash set. 

A function number_of_matches is then called which checks the intersection of this hash set with file2, which is in memory. We do not put file2 into a hash set. We just read it line by line, and if a line is present in the hash set, we increment a counter by 1. This counter is then returned to the main function, which adds it to a global counter. the next chunk of lines is then read into the re-initialized hash-set, which does the same again. Pseudo code below - 


    Begin 

        compute chunk_size given memory allocation 
    
        compute number_of_lines = chunk_size/18
    
        while True:
    
            initialize set
        
            insert next_n_lines from file_1 into set (given number_of_lines)
            
            if set is empty:
            
                break
                
            count += match_checker(set, file_2)


Complexity analysis - 
    Space complexity - O(k) where k is the number of lines read at a time
    Time complexity - O(n1 + n2/k)

Computing chunk sizes - 
    For now, in order to take into account the size overhead of the set and the other variables / functions in my program, I compute the chunk size to be as follows - 
    
    Begin
    
    memory = int(memory)*(10**6) - memory in Bytes (10**6 as we are using SI prefixes)
    
    chunk = float(size) - size is the size of the smaller file
    
    while chunk > (memory/4):                
    
        chunk = chunk/2
        
    number_of_lines = math.ceil(chunk/18) - maximum of 18 bytes per line in file (assumption 1)
    
    return number_of_lines
    
chunk > memory/4 was chosen to make sure that we can account for the overhead of having the list containing the next n lines, the hash set and my functions/variables in memory. 

Optimizing for different scenarios  - 

In all cases, the smaller file is the one loaded into the hash set (in chunks) , and then bigger file is kept in memory. This accounts for cases when one file is larger than another, when one file is bigger than the memory available and the other is not and when the files are of different sizes. 

Case: Both files smaller than memory available:

In this case, we take the smaller of the two files. If the computed chunk size is greater than the file size, we can  load the whole file into the hash set. 

Now, we could account for the case when both files can be loaded into memory, and their own sets. This would be slightly faster, but this is also an O(n) operation, where n is the size of the bigger file. 

The main bottleneck with this comes up whe the files are huge and the memory allowed is small. For example, when both the files are >100MB, and the memory size is 1MB. We then read in very small chunks (k) from one file, n/k times. 

Another factor is the number of I/O calls we make. In accessing the files line by line, the number of I/O calls is really high. In order to reduce this, we could first store the files into temp files, and then read from those line by line, since a seek() in a temp file is comparatively faster. 


*********************TEST CASES*********************




                
    





        

        
            


