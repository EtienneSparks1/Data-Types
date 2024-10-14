def remove_duplicates(numbers):
    """
    Removes duplicates from a list of numbers and returns a new list with unique elements.

    Parameters:
    ----------
    numbers : list
        A list of numbers which may contain duplicate values.

    Returns:
    -------
    list
        A new list with duplicate values removed.
    
    Example:
    --------
    remove_duplicates([1, 2, 2, 3, 4, 4, 5])  # Output: [1, 2, 3, 4, 5]
    """
    # Hint: Convert the list to a set to remove duplicates, then convert it back to a list
    # List --> Set (remove duplicates) --> List (return the list)
    # Write your code here...


    return unique_numbers

list = [1, 2, 3, 4, 5, 6, 2, 6, 7, 8, 4, 6, 9,]
print("Original list: ", list)
list = set(list) #Converting list type to 'set' will remove all duplicate items
print("New list (Without duplicates): ", list)
