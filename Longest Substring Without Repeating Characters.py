def length_of_longest_substring(s):
    n = len(s)
    if n == 0:
        return 0

    max_length = 0
    start = 0
    char_index_map = {}

    for i in range(n):
        if s[i] in char_index_map and start <= char_index_map[s[i]]:
            start = char_index_map[s[i]] + 1
        else:
            max_length = max(max_length, i - start + 1)

        char_index_map[s[i]] = i

    return max_length

# Example usage
s = "abcabcbb"
print(length_of_longest_substring(s))  # Output: 3
