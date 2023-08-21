def find_overlap(headers, seqs, k):
    nodes = {} # Dict for node ids
    graph = {} # Dict for adjacent nodes

    for i in range(len(headers)):
        nodes[headers[i]] = seqs[i]

    for key1, value1 in nodes.items():
        for key2, value2 in nodes.items():
            if key1 != key2 and value1[-k:] == value2[:k]:
                if key1 not in graph:
                    graph[key1] = []
                graph[key1].append(key2)
    return graph


headers = ['>Rosalind_0498', '>Rosalind_2391','>Rosalind_2323','>Rosalind_0442', '>Rosalind_5013']
seqs =['AAATAAA','AAATTTT','TTTTCCC','AAATCCC','GGGTGGG']

dict1 = find_overlap(headers, seqs, 3)
for k,v in dict1.items():
    print (k,v)