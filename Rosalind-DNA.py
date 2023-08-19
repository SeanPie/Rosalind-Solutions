sample = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

def nuc_count(seq):
    counts = {}
    for i in range(len(seq)):
        if seq[i] in counts.keys():
            counts[seq[i]] += 1
        else:
           counts.setdefault(seq[i], 1) 
    return counts

test = nuc_count(sample)

for keys, values in test.items():
    print (keys, values)