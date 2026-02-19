# Name: Cristina Wood
# Date: January 7, 2026
# Title: Assignment 1, Formal Languages and Automata


# Task 1 - language membership testing
# implement a function that determines if a string belongs to a language.

# L = {a^n * b^n | n >= 1} over alphabet {a, b}
# The number of 'a's equals the number of 'b's
# All 'a's come before all 'b's.
# there is at least one 'a' and one 'b'

# create function that inputs string and returns boolean
# define variables a, b and n
# increment through inputed string length, and count a's and b's
# set rules:
#   1) must be an a or a b.
#   2) length must be greater than 1 for both a and b
#   3) a's must come before all b's
# count a's
# count b's
# verify that they follow rules
# return true if count of each are the same (and they passed previously stated rules)
# return false otherwise.


# create function that inputs string and returns boolean
def is_in_language(s: str) -> bool:

    # //////// variables //////////
    a_count = 0
    b_count = 0
    i = 0
    n = len(s)

    # /////////  rules //////////

    # must be at least 'ab' (1 char each)
    if len(s) < 2:
        return False

    # only allow 'a' and 'b' as symbols
    if any(ch not in ('a','b') for ch in s):
        return False

    # verify quantity greater than 1
    # verify equal quantity

    # //////// counting ///////////
    # incrementing i through n length of string s[]; loop counting a's
    while i < n and s[i] == 'a':
        a_count += 1
        i += 1

    # verify has at least one a
    if a_count == 0:
        return False

    # incrementing i through n length of string s[]; loop is counting b's
    while i < n and s[i] == 'b':
        b_count += 1
        i += 1

    # verify has at least one b
    if b_count == 0:
        return False

    # if i kept going after n counted all b's, then these two will be unequal.
    if i != n:
        return False

    # rule that a quantity must be equal to be quantity
    return a_count == b_count

# TEST task 1 (input array of strings into function)
# tests = ['ab', 'aabb', 'aaabbb', 'aabbb', 'aba', 'bbb', 'aaa', '', 'a', 'b', 'aabbab']
#
# for t in tests:
#     print(t, is_in_language(t))




# Task 2 Kleene closure generator

# GOAL: find all words in language given rules
# create function where input is base language and its max length (['a', 'bb', etc.], 4)
# create string of final result
# create array copy of base language, without the '' (that way there is not infinite loop)
# (loop through base_language, and keep any input that isn't '')
# create expandable list of words...
#   start list with '', and apply base language to it
#   verify that new word length is less than or equal to the max length
#   if it still follows rules, add it back into the expandable list, and to the final result
# return final result, once there are no more words in expandable list

def kleene_closure_generator(base_language, max_length):

    # final result (with '', as it is always in L*)
    result = {''}

    # remove empty string from base language to avoid infinite repetition
    # base = working copy of base_language inputted by user
    base = []

    for s in base_language:
        if s != '':
            base.append(s)

    # unexpanded strings
    frontier = ['']

    # I received ChatGPT's help with this section. The comments are all mine and my understanding.
    while frontier:
        # steal string from frontier (pop it out)
        current = frontier.pop(0)

        # expand upon unexpanded string, using base language to expand with (s)
        for s in base:
            new_string = current + s

            # if new length is not too long, accept, and send to final result and frontier.
            if len(new_string) <= max_length and new_string not in result:
                result.add(new_string)
                frontier.append(new_string)

    return result

# print(sorted(
#     kleene_closure_generator(['a', 'bb'], 4),
#     key=lambda x: (len(x), x)
# ))

# Test Task 2: Kleene closure
# result = kleene_closure_generator(["a"], 3)
# expected = {"", "a", "aa", "aaa"}
# assert result == expected
#
# result2 = kleene_closure_generator(["ab"], 4)
# assert "" in result2
# assert "ab" in result2
# assert "abab" in result2
# assert len([s for s in result2 if len(s) <= 4]) >= 3



# Task 3 Recursive Language Definitions
# get language M (as function) that reads in n as repetitions of recursion
# wrap y and z around it n times by calling itself n times
# each time it is called, decrement 'n', that way it doesn't loop infinitely

# inside function, make sure that
def generate_recursive_language_M(n: int) -> str:
    # use a recursive definition
    # generate nth string
    # language : M

    # received ChatGPT's help with error catching syntax, notes are all mine.
    if not isinstance(n, int):
        raise TypeError('n must be an integer') # type error for data type
    if n < 0:
        raise ValueError('n must be non-negative') # value error for negative values

    if n == 0:
        return "x"

    # call function *recursively* 'u'
    return "y" + generate_recursive_language_M(n - 1) + "z"

#quick checks
# print(generate_recursive_language_M(0)) # x
# print(generate_recursive_language_M(1)) # yxz
# print(generate_recursive_language_M(2)) # yyxzz
# print(generate_recursive_language_M(3)) # yyyxzzz

# Task 4 Regular Expressions
# GOAL: return TRUE if string matches regex pattern

# create function where user inputs pattern, and string
# read pattern in
# turn pattern into text structure
#   -- character
#   -- concatenation (2 presedence)
#   -- union | (3 presedence)
#   -- star * (1 presedence)
# cut union off first, that way we can work with remnants (concat, then star)

# if pattern empty, then string must be empty
# if pattern |, split string left and right
# check pattern both sides (left and right)
# if *, check following characters to see if pattern matches otherwise
# if matching, return TRUE
# else if there are no more checkable *matching* characters, return false
# if normal characters, run through function again, and make sure they all match.



def regex_match(pattern, string):
    # If pattern empty, string must also be empty
    if pattern == "":
        return string == ""

    # Union (|) -- split into right and left, and run function on both sides
    if "|" in pattern:
        left, right = pattern.split("|", 1)
        return regex_match(left, string) or regex_match(right, string)

    # Kleene star (only on single char: a*)
    # -- if the second character is a *, and the pattern continues on past *, check following characters and match
    if len(pattern) >= 2 and pattern[1] == "*":
        char = pattern[0]

        # start at 0 as repitition count then continue
        i = 0
        while True:
            # try rest of pattern after star
            if regex_match(pattern[2:], string[i:]):
                return True

            # stop if no more matching chars
            if i >= len(string) or string[i] != char:
                return False

            #increment repetition count
            i += 1

    # check normal characters
    # -- make sure string isn't empty
    # -- run following characters through function again (*recursively*)
    if string != "" and pattern[0] == string[0]:
        return regex_match(pattern[1:], string[1:])

    # if it is anything else not checked.. fall back on false.
    return False





