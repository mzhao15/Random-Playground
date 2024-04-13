

def missing_words(s, t):
    s_words = s.split(' ')
    t_words = t.split(' ')

    m, n = len(s_words), len(t_words)

    if m == 0 or n == 0:
        return s
    
    ans = []

    j = 0
    for i in range(m):
        if j < n and s_words[i] == t_words[j]:
            j += 1
            continue
        
        ans.append(s_words[i])
    
    return ' '.join(ans)


s = "I like eating cheese do you like cheese"
t = "like cheese"

print(missing_words(s, t))


s = "I like soft cheese and hard cheese yum"
t = "like cheese yum"

print(missing_words(s, t))