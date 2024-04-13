from collections import Counter

s = "leetcode"
counter = Counter(s)

unique_chars = set([c for c in counter if counter[c] == 1])

print(counter)
print(unique_chars)
