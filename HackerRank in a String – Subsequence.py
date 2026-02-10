# Problem Statement

# We say that a string contains the word "hackerrank" if a subsequence of its characters spells "hackerrank".

# A subsequence:
# Keeps the same order
# Characters do not need to be adjacent

# For each string s, return:
# "YES" if "hackerrank" exists as a subsequence
# "NO" otherwise

# Example: 

# Input:  hereiamstackerrank
# Output: YES

# Input:  hackerworld
# Output: NO


def hackerrankInString(s):
    
    if len(s) < 10:
        return 'NO' 
    
    i = 0 
    j = 0 
    p = "hackerrank"
    
    while i < len(s) and j < len(p):
        if s[i] == p[j]:
            i += 1 
            j += 1 
        else:
            i += 1 
    
    return 'YES' if j == len(p) else 'NO'
