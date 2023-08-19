#Edit to include reading fasta file functionality

sample = 'CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'

def gc_calculator(seq):
    G_count = 0
    C_count = 0
    for i in range(len(seq)):
        if seq[i] == 'G':
            G_count += 1
        elif seq[i] == 'C':
            C_count += 1
    
    GC_content = (G_count+C_count)/(len(seq))*100
    return GC_content

print(gc_calculator(sample))