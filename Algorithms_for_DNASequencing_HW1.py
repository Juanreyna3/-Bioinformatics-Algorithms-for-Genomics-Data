#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 14:10:56 2021

@author: jr3
"""

"""
First, implement a version of the naive exact matching algorithm that is strand-aware. 

That is, instead of looking only for occurrences of P in T, additionally look for occurrences of the reverse complement of P in T. 

If P is ACT, your function should find occurrences of both ACT and its reverse complement TGA in T.

If P and its reverse complement are identical (e.g. AACGTT), then a given match offset should be reported only once.  # this is going to have to be an if loop 

So if your new function is called naive_with_rc, 

then the old naivefunction and your new naive_with_rc function should return the same results when P equals its reverse complement.

Hint: See this notebook for a few examples you can use to test your naive_with_rc function.

Next, download and parse the lambda virus genome, at: https://d28rh4a8wq0iu5.cloudfront.net/ads1/data/lambda_virus.fa
"""

# function that parses a DNA reference genome from a file in the FASTA format.

def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if not line[0] == '>':
                genome += line.rstrip()
    return genome


# function that parses the read and quality strings from a FASTQ file containing sequencing reads.
    
def readFastq(filename):
    sequences = []
    # qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()  # skip name line
            seq = fh.readline().rstrip()  # read base sequence
            fh.readline()  # skip placeholder line
          #   qual = fh.readline().rstrip() # base quality line
            if len(seq) == 0:
                break
            sequences.append(seq)
        #    qualities.append(qual)
    return sequences

# the following statement is executed at this point so the other functions will take p, t
# and t_2mm

#t = readGenome('lambda_virus.fa')  # this genome is used for Programming HW 1

t2 = readGenome('single_seq.fasta');

# the function below parses the read and quality strings from a FASTQ file containing sequencing reads.

# sequences = readFastq('lambda_virus.fa')


# the function below takes a DNA string and returns its reverse complement

# def reverseComplement(s):
#     complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N'}
#     t = ''
#     for base in s:
#         t = complement[base] + t
#     return t

 
# p should be defined at this point 
# p = 'CTGT'      #this is the p used in HW1
p = 'GGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGG';


# the complement of P is defined to later be used as an input for the new naive exact matching alg
# reverse_complement_p = reverseComplement(p)

# #the following is used as a test to see t, p and p's complement

# print('This is t:')
# #print(t)
# print(t2)

# print('\n')

# print('Sequences: ')

# print('\n')

# print('\n')

# print('This is p:')
# print(p)

# print('\n')

# print('This is the reverse complement of p:')
# print(reverse_complement_p)


# # Naive-Exact Matching Algorithm (this is a reference alg for the creation of the new alg and should be commented or deleted later)

# def naive(p, t):
#     occurrences = []
#     for i in range(len(t) - len(p) + 1):  # loop over alignments
#         match = True
#         for j in range(len(p)):  # loop over characters
#             if t[i+j] != p[j]:  # compare characters
#                 match = False
#                 break
#         if match:
#             occurrences.append(i)  # all chars matched; record
#     return occurrences


# # the function below is a strand-aware naive exact matching algorithm
#     # find complement of P

#     # look for occurences of P in T
#     # look for occurences of the reverse complement of P in T

#         # condition if P and its reverse complement are identical (P is equal to its reverse complement) give match offset only once (if loop?)
#     """
#     Essentially, 
#         if P is in T 
#         --> put in occurences
#         if 'reverse of P' is in T AND not equal to P 
#         --> put in occurences
#     """


# # the function should return the same results as the complement of the old naive-exact algorithm when P equals its reverse complement.

# def naive_with_rc(p, t, reverse_complement_p):
#     occurrences = []
#     for i in range(len(t) - len(p) + 1):  # loop over alignments
#         match_case1 = True
#         for j in range(len(p)):  # loop over characters
#             if t[i+j] != p[j]:  # compare characters
#                 match_case1 = False
#                 break
#     for k in range(len(t) - len(reverse_complement_p) + 1):
#         match_case2 = True
#         for m in range(len(reverse_complement_p)):  # loop over characters
#             if t[k+m] != reverse_complement_p[m]:  # compare characters
#                 match_case2 = False
#                 break

#         # the following needs to be adjusted     
#         if match_case1:
#             occurrences.append(i)  # all chars matched; record
#         if match_case2:
#             if reverse_complement_p != p:
#                 occurrences.append(k)  # all chars matched; record

#     return occurrences
#     """this needs to be adjusted to account for when P and the reverse complement are identical (P is equal to its reverse complement)
#         give match offset only once (if loop?)
#     """

# #occurences = naive_with_rc(p, t, reverse_complement_p);


# # print("The following are the indeces of the occurences of p and the reverse compliment of p in t:")
# # #print(occurences)

# # print('\n') # formatting
# # print('# of occurences of p and the reverse compliment of p in t:')


# # #count_of_occurences = len(occurences)
# # #print(count_of_occurences)

# # print('\n') # formatting
# # #leftmost_occurence = occurences[0]

# # print('The leftmost occurence of p or the reverse compliment of p in t:')
# # #print(leftmost_occurence)

# # once the occurences are returned, sort the occurences for easy finding or use a method like .find to find occurences easily





# # function 'naive_2mm' should return occurences with up to 2 mismatches


# def naive_2mm(p, t):
#     occurrences = []
#     for i in range(len(t) - len(p) + 1):  # loop over alignments
#         count_mismatch = 0
#         for j in range(len(p)):  # loop over characters
#             if t[i+j] != p[j]:  # compare characters
#                 count_mismatch += 1
#         if count_mismatch <= 2:
#             occurrences.append(i)  # all chars matched; record
#     return occurrences

# print('the following should be the amount of occurences with up to 2 mm:')

# #print(len(naive_2mm('TTCAAGCC', t)));


# """
# Question 7: 
# """
# # def readFastq(filename):
# #     sequences = []
# #     qualities = []
# #     with open(filename) as fh:
# #         while True:
# #             fh.readline()  # skip name line
# #             seq = fh.readline().rstrip()  # read base sequence
# #             fh.readline()  # skip placeholder line
# #             qual = fh.readline().rstrip() # base quality line
# #             if len(seq) == 0:
# #                 break
# #             sequences.append(seq)
# #             qualities.append(qual)
# #     return sequences, qualities


# # def phred33ToQ(qual):
# #     return ord(qual) - 33


# # def createHist(qualities):
# #     # Create a histogram of quality scores
# #     hist = [0]*len(qualities[0])
# #     for qual in qualities:
# #         for i in range(len(qual)):
# #             q = phred33ToQ(qual[i])
# #             hist[i] += q
# #     return hist

# # %matplotlib inline
# # reads_file = 'ERR037900_1.first1000.fastq'
# # _, quals = readFastq(reads_file)
# # qual_hist = createHist(quals)
# # plt.plot(range(len(qual_hist)), qual_hist)
# plt.show()

# occurrences = []

def naive_with_counts(p, t2):
    occurrences = []
    count_chrom = 0 # initialized before used in loops
    count_align = 0 # initialized before used in loops
    for i in range(len(t2) - len(p) + 1):  # loop over alignments
        count_align += 1        # counts each time an alignment is started
        match = True
        for j in range(len(p)):  # loop over characters
            count_chrom += 1;    # counts each time a character comparison is made
            if t2[i+j] != p[j]:  # compare characters
                match = False
                break
        if match:
            occurrences.append(i)  # all chars matched; record
    return occurrences, count_align, count_chrom

# print(occurrences)

# print(naive_with_counts(p, t2))

occurrences, num_alignments, num_character_comparisons = naive_with_counts(p, t2)

print(occurrences, num_alignments, num_character_comparisons)






