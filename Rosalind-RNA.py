sample = "GATGGAACTTGACTACGTAAATT"

def transcribe(seq):
    switch = {'T':'U'}
    rna = "".join(switch.get(nuc,nuc)for nuc in seq)
    return rna

print (transcribe(sample))