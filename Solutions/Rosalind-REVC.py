sample = "AAAACCCGGT"

def reverse_comp(seq):
    nuc_dict = {'A':'T','G':'C','T':'A','C':'G'}
    complement = "".join(nuc_dict.get(nuc,nuc) for nuc in seq[::-1])
    return complement

print (reverse_comp(sample))
            