### Determine the similarity between two strings

from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

## Simple Example
similar("Apple","Appel")
similar("Apple","Potato")

## Similarity with Fuzzywuzzy

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

fuzz.ratio("this is a test", "this is a test!")



