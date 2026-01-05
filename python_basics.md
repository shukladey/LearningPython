# Playing with Strings

## Counting substrings efficiently
Instead of generating all substrings:

```python
for i in range(len(word)):
    for j in range(i, len(word)):
        print(word[i:j+1])
