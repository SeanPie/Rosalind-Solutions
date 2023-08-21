s = 'GAGCCTACTAACGGGAT'
t = 'CATCGTAATGACGGCCT'

def calc_Hamming(seq1, seq2):
    count = 0
    for i in range(len(seq1)): # Only works if seqs of equal length
        if seq1[i] != seq2[i]:
            count += 1
    return count

print(calc_Hamming(s,t))


