class Node:
    def __init__(self, attribute=None, value=None, results=None, t=None, f=None):
        self.attribute = attribute
        self.value = value
        self.results = results
        self.t = t
        self.f = f

def class_counts(rows):
    d = {}
    for r in rows:
        d[r[-1]] = d.get(r[-1], 0) + 1
    return d

def entropy(rows):
    from math import log2
    c = class_counts(rows)
    return -sum(v/len(rows)*log2(v/len(rows)) for v in c.values())

def information_gain(rows, col):
    e = entropy(rows)
    vals = set(r[col] for r in rows)
    we = sum(len([r for r in rows if r[col]==v])/len(rows)*entropy([r for r in rows if r[col]==v]) for v in vals)
    return e - we

def build_tree(rows):
    if not rows or len(set(r[-1] for r in rows)) == 1:
        return Node(results=rows[0][-1])
    best = max(range(len(rows[0])-1), key=lambda c: information_gain(rows, c))
    v = rows[0][best]
    t = build_tree([r for r in rows if r[best]==v])
    f = build_tree([r for r in rows if r[best]!=v])
    return Node(best, v, None, t, f)

def print_tree(n, i=""):
    if n.results is not None:
        print(i+n.results)
    else:
        print(i+f"A{n.attribute}={n.value}")
        print_tree(n.t, i+" ")
        print_tree(n.f, i+" ")

data = [
    ['Sunny','Hot','High','Weak','No'],
    ['Sunny','Hot','High','Strong','No'],
    ['Overcast','Hot','High','Weak','Yes'],
    ['Rain','Mild','High','Weak','Yes'],
    ['Rain','Cool','Normal','Weak','Yes'],
    ['Rain','Cool','Normal','Strong','No'],
    ['Overcast','Cool','Normal','Strong','Yes'],
    ['Sunny','Mild','High','Weak','No'],
    ['Sunny','Cool','Normal','Weak','Yes'],
    ['Rain','Mild','Normal','Weak','Yes']
]

tree = build_tree(data)
print_tree(tree)

sample = ['Sunny','Cool','High','Strong']
n = tree
while n.results is None:
    n = n.t if sample[n.attribute]==n.value else n.f

print(n.results)
