def longest_increasing_subsequence(seq):
    """Docstrings are lame
    figure out the type signature yourself
    """
    cache = {}  # where we will memoize our answer
    
    def helper(x):
        if x == 0: # base case
            return seq[:1]
        if x in cache:  # checking if we've memoized a previous answer
            return cache[x]
        # recursive case!
        best_so_far = []  # finding the longest sequence for smaller y
        for y in range(x):
            if seq[y] >= seq[x]:  # skipping invalid values of y
                continue
            if len(helper(y)) > len(best_so_far):
                best_so_far = helper(y)
        best_so_far = best_so_far + [seq[x]]  # can't use += as it mutates the original list
        
        cache[x] = best_so_far  # memoizing
        return best_so_far
    
    return max([helper(i) for i in range(len(seq))], key=len)

print(longest_increasing_subsequence([1,2,3,4,9,3,4,1,10,5])) 