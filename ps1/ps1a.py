###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(filename, 'r')
    # wordlist: list of strings
    cows = {}
    for line in inFile:
        line_split = line.rstrip('\n').split(',')
        cows[line_split[0]] = int(line_split[1])
    print(len(cows), "cows loaded")
    
    inFile.close()
    
    return cows


# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    import operator
    x = cows
    sorted_x = sorted(x.items(), key=operator.itemgetter(1), reverse = True)
    print(sorted_x)
    print("\n")
    manifest_weights = []
    manifest_names = []
    trip_weights = []
    trip_names = []
    for i in range(len(cows)):
        
        if (sum(trip_weights)+sorted_x[i][1]) <= limit:
            trip_names.append(sorted_x[i][0])
            trip_weights.append(sorted_x[i][1])
            
        else:
            manifest_names.append(trip_names)
            manifest_weights.append(trip_weights)
            trip_weights = []
            trip_names = []
            trip_names.append(sorted_x[i][0])
            trip_weights.append(sorted_x[i][1])
            
        if i==len(cows)-1:
            manifest_names.append(trip_names)
            manifest_weights.append(trip_weights)
            
    
    return manifest_names
    

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    import ps1_partition
    
    partitions = get_partitions(cows)
    min_trips = 10
    
    for partition in partitions:
        overweight_flag = False

        for trip in partition:
            trip_weight = 0
            
            for name in trip:
                trip_weight += cows[name]
                
            if trip_weight > limit:
                overweight_flag = True
                
        if (overweight_flag == False) and (len(partition) < min_trips):
            best_partition = partition
            min_trips = len(partition)     

    return best_partition
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    start = time.time()
    greedy_manifest = greedy_cow_transport(cows)
    end = time.time()
    print("greedy trips:", len(greedy_manifest), " greedy time: ", end-start)
    
    start = time.time()
    brute_manifest = brute_force_cow_transport(cows)
    end = time.time()
    print("brute trips:", len(brute_manifest), " brute time: ", end-start)
    
    
    pass


if __name__ == '__main__':
    
    cows = load_cows('ps1_cow_data.txt')
    compare_cow_transport_algorithms()
