def analyze_dna():
    print("Welcome to the DNA Sequence Analyzer!")
    
    sequence = input("Enter your DNA sequence: ").upper().strip()

    if len(sequence) == 0:
        print("Error: You didn't enter a sequence. Please try again.")
        return

    count_A = sequence.count('A')
    count_T = sequence.count('T')
    count_G = sequence.count('G')
    count_C = sequence.count('C')

    total_length = len(sequence)
    gc_content = ((count_G + count_C) / total_length) * 100

    start_codons = []
    for i in range(total_length - 2):
        codon = sequence[i:i+3] 
        if codon == 'ATG':
            start_codons.append(i) 

    stop_codons = []
    for i in range(total_length - 2):
        codon = sequence[i:i+3]
        if codon in ['TAA', 'TAG', 'TGA']:
            stop_codons.append((codon, i)) 

    print("\n" + "="*30)
    print("      DNA ANALYSIS REPORT      ")
    print("="*30)
    print(f"Total Sequence Length: {total_length} base pairs")
    
    print("\n--- Nucleotide Counts ---")
    print(f"Adenine  (A): {count_A}")
    print(f"Thymine  (T): {count_T}")
    print(f"Guanine  (G): {count_G}")
    print(f"Cytosine (C): {count_C}")
    
    print(f"\nGC Content: {gc_content:.2f}%")

    print("\n--- Codon Identification ---")
    
    if len(start_codons) > 0:
        print(f"Start Codon (ATG) found at positions: {start_codons}")
    else:
        print("Start Codon: None found.")

    if len(stop_codons) > 0:
        print("Stop Codon(s) found:")
        for codon, position in stop_codons:
            print(f"  - '{codon}' at position {position}")
    else:
        print("Stop Codons: None found.")
        
    print("="*30)

if __name__ == "__main__":
    analyze_dna()
  
