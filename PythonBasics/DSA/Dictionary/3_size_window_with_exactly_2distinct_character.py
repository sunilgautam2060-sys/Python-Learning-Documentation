s = "aabbcabc"
k = 3

count = 0
dictionary = {}
left = 0

for right in range(len(s)):

    # Add right character
    if s[right] not in dictionary:
        dictionary[s[right]] = 1
    else:
        dictionary[s[right]] += 1

    # Window reached size k
    if right - left + 1 == k:

        if len(dictionary) == 2:
            count += 1

        # Remove left character
        dictionary[s[left]] -= 1

        if dictionary[s[left]] == 0:
            del dictionary[s[left]]

        left += 1

print(count)