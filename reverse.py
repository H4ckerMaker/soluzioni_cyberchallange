with open('../input/input8.txt') as f:
    N = int(f.readline().strip())
    t = f.readline().strip()
    
freq = {}
for count, letter in enumerate(t):
    if letter not in freq:
        freq[letter] = sum(_ == letter for _ in t[count:])

groups = {}
for key in freq:
    if freq[key] not in groups:
        groups[freq[key]] = []
        for _ in freq:
            if freq[_] == freq[key]:
                groups[freq[key]].append(_)

enc_str = ""
for char in t:
    char_freq = freq[char]
    group = groups[char_freq]
    group.sort()
    enc_key = group[len(group) - group.index(char) - 1]
    enc_str += enc_key

print(enc_str)