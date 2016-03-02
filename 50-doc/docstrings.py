# If the first statement of a module, class or function definition is a string, 
# that string becomes a documentation string for the associated object, as in the
# following example.

# After importing this module, you can invoke help(docstrings.py) to list
# both the module docstring and its containing docstrings. You can also 
# invoke help(fact) to display the docstring for the fact() function.

"docstrings.py: module that illustrates docstrings"

def fact(n):
    "This function computes a factorial"
    if (n <= 1): return 1
    else: return n * fact(n - 1)

def triplequote(n):
    '''This is a multiline docstring.
Another line.
Yet another line.'''
    return n
