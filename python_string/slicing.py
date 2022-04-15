S = 'ABCDEFGHI'
print(S[::-1])    # IHGFEDCBA



# Slice first three characters from the string
S = 'ABCDEFGHI'     # ABC
print(S[:3])

# Slice last three characters from the string
S = 'ABCDEFGHI'
print(S[-3:])       #GHI

# Returns every 2nd item between position 6 to 1 in reverse order
S = 'ABCDEFGHI'
print(S[6:1:-2])    #GEC

# Return every 2nd item between position 2 to 7
S = 'ABCDEFGHI'
print(S[2:7:2])     # CEG

#Slice with Positive & Negative Indices
S = 'ABCDEFGHI'
print(S[2:-5])


#Slice with Negative Indices
S = 'ABCDEFGHI'
print(S[-2:-7:-2])