# function to calculate reverse hash
def revHash(hashCode):
    letters = "acdegilmnoprstuw"
    # define original string to be returned
    originalStr = ""
    while hashCode>=37:
        # i should always be in range 0 <= i <= (letters.length -1)
        index = (hashCode%37)
        originalStr = originalStr + letters[index]
        hashCode=hashCode//37
    #return reverse of computed original string
    return originalStr[::-1]


# Test Case (should show leepadg)
# result = revHash(680131659347)
# print result

# Test Case (should return nothing)
# result = revHash(10)
# print result