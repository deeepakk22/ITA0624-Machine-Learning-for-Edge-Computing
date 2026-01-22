import copy

data = [
    ['Sunny','Warm','Normal','Strong','Warm','Same','Yes'],
    ['Sunny','Warm','High','Strong','Warm','Same','Yes'],
    ['Rainy','Cold','High','Weak','Cool','Change','No'],
    ['Sunny','Warm','High','Strong','Cool','Change','Yes']
]

def candidate_elimination(data):
    n = len(data[0]) - 1
    S = ['0'] * n
    G = [['?'] * n]

    for row in data:
        if row[-1] == 'Yes':
            for i in range(n):
                if S[i] == '0':
                    S[i] = row[i]
                elif S[i] != row[i]:
                    S[i] = '?'
            G = [g for g in G if all(g[i] == '?' or g[i] == S[i] for i in range(n))]
        else:
            G_new = []
            for g in G:
                for i in range(n):
                    if g[i] == '?' and S[i] != row[i]:
                        new_g = g.copy()
                        new_g[i] = S[i]
                        G_new.append(new_g)
            G = G_new

    return S, G

S, G = candidate_elimination(data)
print(S)
print(G)