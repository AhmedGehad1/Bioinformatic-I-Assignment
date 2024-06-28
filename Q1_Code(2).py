from Bio.Seq import Seq

def find_all_orfs(dna_sequence):
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]
    
    all_orfs = []
    sequence = Seq(dna_sequence)
    i = 0
    while i < len(sequence):
        # Find the next start codon
        start_pos = sequence.find(start_codon, i)
        if start_pos == -1:
            break  # No more start codons found, exit the loop
        
        # Find the next end codon after the start codon
        for j in range(start_pos + 3, len(sequence) - 2, 3):
            codon = sequence[j:j+3]
            if codon in stop_codons:
                end_pos = j + 2  # Include the end codon
                orf_sequence = sequence[start_pos:end_pos + 1]  # Extract ORF sequence
                orf_length = len(orf_sequence)  # Calculate ORF length

                # Check if ORF length is greater than 6
                if orf_length > 6:
                    all_orfs.append((start_pos, end_pos, codon, orf_sequence, orf_length))  # Store the ORF
                i = end_pos + 1  # Move to the next position after the end codon
                break
        else:
            i = start_pos + 3  # If no stop codon found, move to the next start codon
    
    return all_orfs

# Test the function
dna_sequence = "ATGATGAGCTAGTAAATGATGTAAAGTAGAATGTAA"
all_orfs = find_all_orfs(dna_sequence)
print("All ORFs found:")
for i, orf in enumerate(all_orfs):
    start_pos, end_pos, end_codon, orf_sequence, orf_length = orf
    if orf_length > 6:  # Check if ORF length is greater than 6
        print("ORF {}: Start position ATG: {}, End position: {}, End codon: {}, ORF sequence: {}, Length: {}".format(i+1, start_pos, end_pos, end_codon, orf_sequence, orf_length))