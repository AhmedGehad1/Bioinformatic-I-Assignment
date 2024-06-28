### Bioinformatics I Assignment

**Prepared by:**
Ahmed Gehad Mohamed Aly 

## 1. Open Reading Frames Detection

### Code_1 Explanation:
Create a function that finds all the ORFs in a given DNA sequence. Return a list of ORFs along with their start and end positions.

- Define start codon (ATG) and stop codons (TAA, TAG, TGA).
- Initialize an empty list to store ORFs.
- Convert DNA sequence to a Seq object.
- Iterates through the DNA sequence to find ORFs.
  - Finds start codon and then searches for stop codon in a loop.
  - Extracts ORF sequence based on codon positions.
- Store ORF information in a list and return it.
- Example sequence provided for testing ORF detection.

### Output:
![image](https://github.com/AhmedGehad1/Bioinformatic-I-Assignment/assets/125567504/d9ed16e1-73d0-4e8e-9ca1-4324d2b54fa9)

### Code_2 Explanation:
Modified function to filter out ORFs shorter than 6 nucleotides.

- Added calculation of ORF length.
- Conditionally appends ORFs longer than 6 nucleotides to the list.
- Example sequence used to demonstrate filtered ORFs.
  
### Output:
  ![image](https://github.com/AhmedGehad1/Bioinformatic-I-Assignment/assets/125567504/19484352-23c7-47f8-8f52-04b46ea58ef6)

## 2. Create a Python program that generates a dot plot to visualize sequence similarities.

### Code Explanation:
- Function takes two DNA sequences as input.
- Creates a dot plot using Matplotlib to visualize matching nucleotides.
- Iterates over positions in both sequences, plotting blue dots for matches.
- Labels x-axis and y-axis with sequence letters for clarity.
- Example sequences provided for generating visual output.

### Output:
![image](https://github.com/AhmedGehad1/Bioinformatic-I-Assignment/assets/125567504/ac7f72f2-2fce-4531-b079-4a188821c83d)
