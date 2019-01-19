def proteins(strand):
    """
    Translates the codons in a DNA strand into its corresponding proteins.

    Codon                 | Protein
    :---                  | :---
    AUG                   | Methionine
    UUU, UUC              | Phenylalanine
    UUA, UUG              | Leucine
    UCU, UCC, UCA, UCG    | Serine
    UAU, UAC              | Tyrosine
    UGU, UGC              | Cysteine
    UGG                   | Tryptophan
    UAA, UAG, UGA         | STOP

    If any of the terminating codons (the "STOP" codon) is encountered, then
    all translation ends and the protein is terminated. All subsequent codons
    after are ignored
    """
    translation = {"Methionine": ["AUG"],
                   "Phenylalanine": ["UUU", "UUC"],
                   "Leucine": ["UUA", "UUG"],
                   "Serine": ["UCU", "UCC", "UCA", "UCG"],
                   "Tyrosine": ["UAU", "UAC"],
                   "Cysteine": ["UGU", "UGC"],
                   "Tryptophan": ["UGG"],
                   "STOP": ["UAA", "UAG", "UGA"]}

    result = []
    for letter in range(0, len(strand), 3):
        codon = strand[letter: letter + 3]
        protein = [k for k, v in translation.items() if codon in v]
        if protein == ["STOP"]:
            return result
            break
        else:
            result.extend(protein)

    return result
