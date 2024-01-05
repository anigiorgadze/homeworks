
def dna_to_rna(dna):
    rna=""
    for element in dna:
        if element == "T":
            rna += "U"
        else:
            rna += element
    return rna