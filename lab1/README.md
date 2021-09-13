# LAB 1

## Description

1. [Find Patterns Forming Clumps in a String](task1.py)
```
Given integers L and t, a string Pattern forms an (L, t)-clump inside a (larger) string Genome if there is an interval of Genome of length L in which Pattern appears at least t times. 
For example, TGCA forms a (25,3)-clump in the following Genome: gatcagcataagggtcccTGCAATGCATGACAAGCCTGCAgttgttttac.
```
2. [Find a Position in a Genome Minimizing the Skew](task2.py)
```
Define the skew of a DNA string Genome, denoted Skew(Genome), as the difference between the total number of occurrences of 'G' and 'C' in Genome. 
Let Prefixi (Genome) denote the prefix (i.e., initial substring) of Genome of length i. 
For example, the values of Skew(Prefixi ("CATGGGCATCGGCCATACGCC")) are: 0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2
```
3. [Find All Approximate Occurrences of a Pattern in a String](task3.py)
```
We say that a k-mer Pattern appears as a substring of Text with at most d mismatches 
if there is some k-mer substring Pattern' of Text having d or fewer mismatches with Pattern, i.e., HammingDistance(Pattern, Pattern') ≤ d. 
Our observation that a DnaA box may appear with slight variations leads to the following generalization of the Pattern Matching Problem.
```
4. [Find the Most Frequent Words with Mismatches in a String](task4.py)
```
Given strings Text and Pattern as well as an integer d, we define Countd(Text, Pattern) as the total number of occurrences of Pattern in Text with at most d mismatches. 
For example, Count1(AACAAGCTGATAAACATTTAAAGAG, AAAAA) = 4 because AAAAA appears four times in this string with at most one mismatch: AACAA, ATAAA, AAACA, and AAAGA. Note that two of these occurrences overlap.

A most frequent k-mer with up to d mismatches in Text is simply a string Pattern maximizing Countd(Text, Pattern) among all k-mers. 
Note that Pattern does not need to actually appear as a substring of Text; for example, AAAAA is the most frequent 5-mer with 1 mismatch in AACAAGCTGATAAACATTTAAAGAG, even though AAAAA does not appear exactly in this string. 
Keep this in mind while solving the following problem.
```
5. [Find Frequent Words with Mismatches and Reverse Complements](task5.py)


## Useful links

- [DNA replication](https://youtu.be/Qqe4thU-os8)
- [coursera: weeks 1-2](https://www.coursera.org/learn/dna-analysis)
