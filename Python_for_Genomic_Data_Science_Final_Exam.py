#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on Tue Sep 28 13:30:29 2021

@author: jr3

"""

"""
Write a Python program that takes as input a file containing DNA sequences in multi-FASTA format, 
and computes the answers to the following questions. 

You can choose to write one program with multiple functions to answer these questions, 
or you can write several programs to address them. 


We will provide a multi-FASTA file for you, and you will run your program to answer the exam questions. 

While developing your program(s), please use the following example file to test your work: 
    
    dna.example.fasta


You'll be given a different input file to launch the exam itself.


Here are the questions your program needs to answer. 
The quiz itself contains the specific multiple-choice questions you need to answer for the file you will be provided.
"""


"""
(1) 

    How many records are in the file? A record in a FASTA file is defined as a single-line header,followed by lines of sequence data. 

    The header line is distinguished from the sequence data by a greater-than (">") symbol in the first column. 

    The word following the ">" symbol is the identifier of the sequence, and the rest of the line is an optional description of the entry. 

    There should be no space between the ">" and the first letter of the identifier. 
"""

# Solution to Part 1 begins here -----------------------------------------------------------------------------------------

try:
    f = open('dna.example.fasta','r')   # opens fasta file
except IOError:
    print('the example fasta file selected does not exist!!')
    
f.seek(0)                               # initializes position of the "invisible cursor"

seqs = {}
seqs_lengths = {}

count = 0;

for line in f: 
    # discard the new line at the end (if any)
    line = line.rstrip()                # rstrip([chars]) returns a copy of the string with trailing characters chars removed
    
    #distinguish header from sequence
    if line[0] =='>':
        words = line.split()
        name = words[0][1:]
        seqs[name]=''
        count = count + 1;
        print(count)

    else: 
        seqs[name] = seqs[name] + line
        seqs_lengths[name] = seqs[name] + line


f.close()

# Solution to Part 1 ends here ------------------------------------------------------------------------------------------
    
print("\n \n")

"""
(2) 

    What are the lengths of the sequences in the file? 
    
    What is the longest sequence and what is the shortest sequence? 
    
    Is there more than one longest or shortest sequence? 
    
    What are their identifiers? 

"""

# Solution to Part 2 begins here -----------------------------------------------------------------------------------------

# prints sequence names and associated lengths
for name, seq in seqs.items():
     print("Sequence: ", name,"\nLength: ", len(seq),'\n')

print('------------------------------------------------------------------------- \n')

for name, seq in seqs.items():
   length = len(seq)
   seqs_lengths[name] = [length]
    

#displays values of sequence lengths in a dictionary 'seqs_lengths'
#print(seqs_lengths.values(),'\n')

longest_sequence = max(seqs_lengths.values());
scnd_longest_sequence = sorted(seqs_lengths.values())[1];
shortest_seqeunce = min(seqs_lengths.values());
scnd_shortest_sequence = sorted(seqs_lengths.values())[-2];

# prints longest sequence
print("Length of longest sequence:", longest_sequence,'\n')

# prints shortest sequence
print("Length of shortest sequence:", shortest_seqeunce,'\n')
      
# prints second element of sorted sequence length (second shortest)
print("Length of 2nd longest sequence:", scnd_longest_sequence, '\n')

# prints second-to-last element of sorted sequence length (second longest)
print("Length of 2nd shortest sequence:", scnd_shortest_sequence, '\n')






# # prints longest sequence
# print("Length of longest sequence:", max(seqs_lengths.values()),'\n')

# # prints shortest sequence
# print("Length of shortest sequence:", min(seqs_lengths.values()),'\n')
      
# # prints second element of sorted sequence length (second shortest)
# print("Length of 2nd longest sequence:", sorted(seqs_lengths.values())[1])

# # prints second-to-last element of sorted sequence length (second longest)
# print("Length of 2nd shortest sequence:", sorted(seqs_lengths.values())[-2])

# Solution to Part 2 ends here ------------------------------------------------------------------------------------------


"""
(3) In molecular biology, a reading frame is a way of dividing the DNA sequence of nucleotides into a set of consecutive, 
non-overlapping triplets (or codons). 


Depending on where we start, there are six possible reading frames: 
    three in the forward (5' to 3') direction and 
    three in the reverse (3' to 5'). 

    
For instance, the three possible forward reading frames for the sequence AGGTGACACCGCAAGCCTTATATTAGC are: 

    AGG TGA CAC CGC AAG CCT TAT ATT AGC

    A GGT GAC ACC GCA AGC CTT ATA TTA GC

    AG GTG ACA CCG CAA GCC TTA TAT TAG C 


These are called reading frames 1, 2, and 3 respectively. 

An open reading frame (ORF) is the part of a reading frame that has the potential to encode a protein. 
It starts with a start codon (ATG), and ends with a stop codon (TAA, TAG or TGA). 

For instance, ATGAAATAG is an ORF of length 9.




Given an input reading frame on the forward strand (1, 2, or 3) your program should be able to 
identify all ORFs present in each sequence of the FASTA file, and answer the following questions: 
    
    
    what is the length of the longest ORF in the file?  
        # the ORF should include the starting and ending codons
    
    
    What is the identifier of the sequence containing the longest ORF? 
   
    
    For a given sequence identifier, what is the longest ORF contained in the sequence represented by that identifier? 
   
    
    What is the starting position of the longest ORF in the sequence that contains it? 
   
    
    The position should indicate the character number in the sequence. 


For instance, the following ORF in reading frame 1:

>sequence1

ATGCCCTAG

starts at position 1.

Note that because the following sequence:

>sequence2

ATGAAAAAA

does not have any stop codon in reading frame 1, we do not consider it to be an ORF in reading frame 1. 

"""

# Solution to Part 3 begins here

# for name, seq in seqs.items():
#     print(seqs.values())

stop_codons = ['TAA','TAG','TGA']
example = 'ATGGATTAGCCGTAGAATT'  


# for i in stop_codons:
#     example = example.split(i)
#     example = 'end'.join(example)
#     if i == len(stop_codons):
#         break
# print(example)

# example = example.split('ATG')
# example = 'start'.join(example)
# print(example)

# rf = example.split('start','end')
# rf = ''.join(rf)
# print(rf)
  
# example = 'ATGGATTAGCCGTAGAATT'  
# after_stop = example.split('TAG') # notice the first and last elements of the resultant list 
# after_stop = 'stop'.join(after_stop)
# print(after_stop)
    
#                                   # are not preceded (first element) and followed (last element)
#                                   # by the arguemnt passed into the .split method ('TAG')  

#                                   # if an arugment that is not present in the sequence is 
#                                   # passed to the .split method then the method will return the 
#                                   # entire string / integers that were supposed to be split    
 # after_stop = after_stop.join()
# print(after_stop)


# for i in after_stop:
#     after_start = split(after_stop, 'TAG','TAA', 'TGA')

# print(after_start)    


# find indices of all potential stop codons in sequences
# split the sequences by the stop codons
# search the resultant lists for start codons
    # if the lists contents have stop codons, take the element and feed the latter part (after 'ATG' start codon
    # into another 'list inside a list' associated with the sequence considered) - these should be the 
# find indices of all start codons in sequences
# 




# set the open reading frames in a dictionary for each sequence in "seqs"




# create structure defining the reading frames as the distances between the nearest start codon and the stop codon,
    # using the stop codon as the reference (ensuring the reading frames being considered are open reading frames)


        

# create RF dictionary with the identifiers and locations of the reading frames

# calculate the lengths of the reading frames 

# calculate the length of the longest reading frame 


# create RF dictionary with the identifiers and the lengths of the reading frames





# Solution to Part 3 ends here

"""
(4) A repeat is a substring of a DNA sequence that occurs in multiple copies (more than one) somewhere in the sequence. 

Although repeats can occur on both the forward and reverse strands of the DNA sequence, 
we will only consider repeats on the forward strand here. 

Also we will allow repeats to overlap themselves. 

For example, the sequence ACACA contains two copies of the sequence ACA - once at position 1 (index 0 in Python), and once at position 3.

 Given a length n, your program should be able to identify all repeats of length n in all sequences in the FASTA file. 
 
 Your program should also determine how many times each repeat occurs in the file, and which is the most frequent repeat of a given length.

"""
# Solution to Part 4 begins here







# Solution to Part 4 ends here
