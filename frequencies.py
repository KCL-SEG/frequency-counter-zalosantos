"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}  #dictionary
    x=0
    n = len(items)
    while x < n:   #it scans the all the items in the list

       scanner = False
       if frequencies.get(str(items[x])) == None:
           i= frequencies.get(str(items[x]))
           i=0
           frequencies[str(items[x])]= i+1


       else:
           frequencies[str(items[x])]= frequencies.get(str(items[x]))+1
       x=x+1
    return frequencies
