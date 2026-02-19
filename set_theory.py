
#making a set
#CURLY BRACES
a_set = {1, 2, 3}
#CONSTRUCTOR
another_set = set([1, 2, 3, 4]) # duplicates not doubled
print(another_set)

# empty set -- uses () not {}
empty_set = set()




the_set = {1, 2, 3}

#add dynamically
the_set.add(4) # {1, 2, 3, 4}

#remove dynamically
the_set.remove(2) # has error message if 2 does not exist
the_set.discard(2) # has no error message if 2 does not exist

#check subsets or elements within a set
1 in the_set # in operator

t = {'a', 'b', 'c'} # in method
u = {'a', 'b'}
u.issubset(t)

# length (cardinality)
len({1, 3, 5, 7})

# cartesian product
A = set([1, 2])
B = set(['a', 'b', 'c'])

def cartesian_product(A: set, B: set) -> set[tuple]:
    return {(a, b) for a in A for b in B}

cartesian_product(A, B)