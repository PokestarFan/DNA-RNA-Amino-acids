def dna_to_rna(dna):
    newstring = ''
    dna = dna.upper()
    for i in dna:
        if i == 'T':
            newstring += 'U'
        else:
            newstring += i
    return newstring
