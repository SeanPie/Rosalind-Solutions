def read_fasta(file_path):
    sequences = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('>'):
                continue
            else:
                sequences.append(line.strip())
    return sequences

def profile_matrix(sequences):
    profile_dict = {}
    for i in range(len(sequences[0])):
        column = [seq[i] for seq in sequences]
        for symbol in ['A', 'C', 'G', 'T']:
            profile_dict.setdefault(symbol, []).append(column.count(symbol))

    return profile_dict

def get_consensus(profile_matrix):
    consensus = ''
    for i in range(len(profile_matrix['A'])):
        max_count = 0
        max_count_symbol = ''
        for symbol in ['A','C','G','T']:
            if profile_matrix[symbol][i] > max_count:
                max_count = profile_matrix[symbol][i]
                max_count_symbol = symbol
        consensus += max_count_symbol
    return consensus

seqs = ['ATCCAGCT', 'GGGCAACT', 'ATGGATCT', 'AAGCAACC','TTGGAACT','ATGCCATT','ATGGCACT']
mat = profile_matrix(seqs)
print (get_consensus(mat))