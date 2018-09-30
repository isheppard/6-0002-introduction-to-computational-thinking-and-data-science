###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always an egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # TODO: Your code here
    #want to store combo of egg weights
    # ex: 3 of 25lb and 1 of 10lb
    if target_weight == 0:
        result = ""
        total_components = 0
        total_sum = 0
        
        for key in memo:
            result += str(memo[key]) + " * " + str(key) + " + " 
            total_components += memo[key]
            total_sum += memo[key] * key

        return str(total_components) + " (" + result[:-2] + str("= ") + str(total_sum) + ") " 
        
    for egg_weight in reversed(egg_weights):
        
        if target_weight >= egg_weight:

            try:
                memo[egg_weight] += 1
            
            except:
                memo[egg_weight] = 1
                
            
            return dp_make_weight(egg_weights, target_weight - egg_weight)
    


# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()