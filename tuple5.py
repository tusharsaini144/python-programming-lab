# Program to remove the given character from first element of Tuple

# Creating and printing the List of Tuple 
tupList = [("py_t_hon", 4), ("p_ro_gra_m", 5)]
print("Initial List of Tuples : " + str(tupList))
char = "_"

convTupList = [(tup[0].replace(char, ''), tup[1]) for tup in tupList]

# printing the tuple list after removing character
print("List of tuples after removing character from first element : " + str(convTupList))
