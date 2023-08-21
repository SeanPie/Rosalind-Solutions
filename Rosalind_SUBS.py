string_s = 'GATATATGCATATACTT'
string_t = 'ATAT'

def string_combing(needle, haystack):
    locations = []

    for i in range(len(haystack)-len(needle)+1): # Range of starting indexes that could contain the needle
        if haystack[i:i+len(needle)] == needle:
            locations.append(i +1)

    return locations

print(string_combing(string_t,string_s))