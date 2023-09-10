import math

freq = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702,
         0.02228, 0.02015, 0.06094, 0.06966, 0.00153,
           0.00772, 0.04025, 0.02406, 0.06749, 0.07507,
             0.01929, 0.00095, 0.05987, 0.06327, 0.09056,
               0.02758, 0.00978, 0.02360, 0.00150, 0.01974, 0.00074]

def rot_alpha(n):
    from string import ascii_lowercase as lc, ascii_uppercase as uc
    lookup = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)

def rot_k_all(s):
    return [rot_alpha(k)(s) for k in range(25)]
        
def pk(s,c):
    return sum(l == c for l in s)

def q(c):
    return freq[ord(c)-65]

def cross_entropy(s): 
    summ = sum((pk(s,l)*math.log(q(l),10)) for l in s)
    return summ*(-1)

def cross_entropy_all(all_text):
    return [cross_entropy(text) for text in all_text]

etext = str(input("ROT-k Encrypted Text:"))
all_k_text = rot_k_all(etext)
all_entropy_text = cross_entropy_all(all_k_text)
minimum = all_entropy_text[0]

for ent in all_entropy_text:
    if ent < minimum:
        minimum = ent

index_k = all_entropy_text.index(minimum)
print(''.join(all_k_text[index_k]))



