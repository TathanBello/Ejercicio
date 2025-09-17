import itertools

# --------------------- Closure Properties ---------------------
def union(L1, L2):
    """Return union of two regular languages represented as sets."""
    return L1.union(L2)

def intersection(L1, L2):
    """Return intersection of two regular languages represented as sets."""
    return L1.intersection(L2)

def complement(L, sigma):
    """Return complement of a regular language with respect to alphabet sigma."""
    all_strings = set(''.join(p) for i in range(1, 3) for p in itertools.product(sigma, repeat=i))
    return all_strings - L

def concatenation(L1, L2):
    """Return concatenation of two regular languages."""
    return set(x + y for x in L1 for y in L2)

def kleene_star(L):
    """Return Kleene star of a language (limited to length <= 3 for demonstration)."""
    result = {""}
    for i in range(1, 4):
        for prod in itertools.product(L, repeat=i):
            result.add("".join(prod))
    return result

# Example regular languages
sigma = {'a', 'b'}
L1 = {'a', 'ab'}
L2 = {'b', 'ba'}

print("=== Closure Properties ===")
print(f"L1 = {L1}, L2 = {L2}")
print(f"Union: {union(L1, L2)}")
print(f"Intersection: {intersection(L1, L2)}")
print(f"Complement of L1: {complement(L1, sigma)}")
print(f"Concatenation: {concatenation(L1, L2)}")
print(f"Kleene Star of L1: {kleene_star(L1)}")


# --------------------- Decision Procedure (DFA Membership) ---------------------
class SimpleDFA:
    """Simple DFA that accepts strings ending with 'ab'."""
    def __init__(self):
        self.states = {'q0', 'q1', 'q2'}
        self.start = 'q0'
        self.accept = {'q2'}
        self.transitions = {
            ('q0', 'a'): 'q1', ('q0', 'b'): 'q0',
            ('q1', 'a'): 'q1', ('q1', 'b'): 'q2',
            ('q2', 'a'): 'q1', ('q2', 'b'): 'q0'
        }

    def run(self, string):
        state = self.start
        for symbol in string:
            state = self.transitions.get((state, symbol), self.start)
        return state in self.accept

dfa = SimpleDFA()
print("\n=== DFA Membership Check ===")
for s in ["ab", "aab", "bba", "bbab"]:
    print(f"String '{s}' accepted? {'Yes' if dfa.run(s) else 'No'}")


# --------------------- DFA Minimization Example ---------------------
# States: q0,q1,q2,q3
# Accepting: q2,q3
# Transitions: simplified for demonstration
dfa_transitions = {
    'q0': {'a': 'q1', 'b': 'q2'},
    'q1': {'a': 'q1', 'b': 'q2'},
    'q2': {'a': 'q3', 'b': 'q2'},
    'q3': {'a': 'q3', 'b': 'q2'}
}

# Partition refinement algorithm (very simple example)
def minimize_dfa(states, accepting, transitions, alphabet):
    # Initial partition: accepting and non-accepting
    P = [accepting, states - accepting]
    W = [accepting]
    while W:
        A = W.pop()
        for c in alphabet:
            X = {q for q in states if transitions[q][c] in A}
            newP = []
            for Y in P:
                inter, diff = Y.intersection(X), Y - X
                if inter and diff:
                    newP.extend([inter, diff])
                    if Y in W:
                        W.remove(Y)
                        W.extend([inter, diff])
                    else:
                        W.append(inter if len(inter) <= len(diff) else diff)
                else:
                    newP.append(Y)
            P = newP
    return P

states = {'q0', 'q1', 'q2', 'q3'}
accepting = {'q2', 'q3'}
alphabet = {'a', 'b'}

print("\n=== DFA Minimization ===")
partitions = minimize_dfa(states, accepting, dfa_transitions, alphabet)
print(f"Minimized state groups: {partitions}")
