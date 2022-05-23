"""Create a recursive function
Write a program to create a recursive function to 
calculate the sum of number from 0 to 10.

A recursive function is a function that calls itself, 
again and again."""

def addition(num):
    """
    this function takes a number and returns the sum of numbers uptil that number

    Parameters
    ----------
        num (int): The number to count to

    
    Returns
    -------
        int: the result
    """
    if num:
        return num + addition(num-1)
    else:
        return 0

print(addition(10))