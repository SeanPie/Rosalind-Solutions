def find_longest_common_substring(strings):
    common_motif = ""
    
    for length in range(1, len(strings[0]) + 1):
        for i in range(len(strings[0]) - length + 1):
            substring = strings[0][i:i + length]
            if all(substring in seq for seq in strings[1:]):
                if len(substring) > len(common_motif):
                    common_motif = substring
    
    return common_motif

seqs = ['GATTACA','TAGACCA','ATACA']

print(find_longest_common_substring(seqs))