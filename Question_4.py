from Bio.Seq import Seq
import matplotlib.pyplot as plt

def create_dot_plot(sequence1, sequence2):
    # Create a new figure with a specific size
    plt.figure(figsize=(10, 6))
    
    # Set the title of the plot
    plt.title("Dot Plot")
    
    # Set labels for x-axis and y-axis
    plt.xlabel("Sequence 1")
    plt.ylabel("Sequence 2")

    # Iterate over positions in both sequences
    for i in range(len(sequence1)):
        for j in range(len(sequence2)):
            # If nucleotides at the same position match, plot a blue dot
            if sequence1[i] == sequence2[j]:
                plt.scatter(i, j, color='blue')

    # Set sequence letters as ticks on the x-axis and y-axis
    plt.xticks(range(len(sequence1)), sequence1)
    plt.yticks(range(len(sequence2)), sequence2)

    # Add gridlines to the plot
    plt.grid(True)

    # Display the plot
    plt.show()

# Example sequences
sequence1 = Seq("ATCGATCGATCGATCG")
sequence2 = Seq("TAGCATCGATCGTTGC")

# Call the function to create the dot plot
create_dot_plot(sequence1, sequence2)
