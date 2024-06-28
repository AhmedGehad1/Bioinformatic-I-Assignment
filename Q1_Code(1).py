from Bio.Seq import Seq

def find_all_orfs(dna_sequence):
    # Define start and stop codons
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]
    
    # Initialize list to store ORFs
    all_orfs = []
    
    # Convert the DNA sequence string to a Seq object
    sequence = Seq(dna_sequence)
    
    # Initialize loop variable
    i = 0
    
    # Iterate through the sequence
    while i < len(sequence):
        # Find the next start codon
        start_pos = sequence.find(start_codon, i)
        
        # If no start codon is found, exit the loop
        if start_pos == -1:
            break
        
        # Find the next end codon after the start codon
        for j in range(start_pos + 3, len(sequence) - 2, 3):
            codon = sequence[j:j+3]
            
            # Check if the codon is a stop codon
            if codon in stop_codons:
                # Define the end position of the ORF
                end_pos = j + 2  # Include the end codon
                
                # Extract the ORF sequence
                orf_sequence = sequence[start_pos:end_pos + 1]
                
                # Store the ORF information
                all_orfs.append((start_pos, end_pos, codon, orf_sequence, orf_length))
                
                # Move to the next position after the end codon
                i = end_pos + 1
                break

    return all_orfs

# Test the function
dna_sequence = "ATGATGAGCTAGTAAATGATGTAAAGTAGAATGTAA"
all_orfs = find_all_orfs(dna_sequence)
print("All ORFs found:")
for i, orf in enumerate(all_orfs):
    start_pos, end_pos, end_codon, orf_sequence, orf_length = orf
    print("ORF {}: Start position ATG: {}, End position: {}, End codon: {}, ORF sequence: {}, Length: {}".format(i+1, start_pos, end_pos, end_codon, orf_sequence, orf_length))
