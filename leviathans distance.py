"""
Minimum edit operations to turn string 1 into string2. Mode "m" serves to actually view the
process of tabulation comparison.
"""

import pprint
def levenshteinDistance(str1, str2, mode = "d"):
    edits = [[x for x in range(len(str1)+1)] for y in range(len(str2)+1)]
    for i in range(1, len(str2)+1):
        edits[i][0] = edits[i-1][0]+1
    for i in range(1,len(str2)+1):
        for j in range(1,len(str1)+1):
            if str2[i-1] == str1[j-1]:
                edits[i][j] = edits[i-1][j-1]
            else:
                edits[i][j] =1 + min(edits[i-1][j-1],edits[i][j-1],edits[i-1][j])
    
    return edits if mode == "m" else edits[-1][-1]


string1 = "Lugen"
string2 = "Flughafen"
pprint.pprint(levenshteinDistance(string1,string2,"d"))
pprint.pprint(levenshteinDistance(string1,string2,"m"))