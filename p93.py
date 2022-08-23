from itertools import permutations
from itertools import combinations_with_replacement

class ListElement:
    def __init__(self, value, next):
        self.value = value
        self.next = next
    def nth(self, n):
        o = self
        i = 0
        while i < n and o.next is not None:
            o = o.next
            i += 1
        return o

def init(multiset):
    multiset.sort() # ensures proper non-increasing order
    h = ListElement(multiset[0], None)
    for item in multiset[1:]:
        h = ListElement(item, h)
    return h, h.nth(len(multiset) - 2), h.nth(len(multiset) - 1)

def visit(h):
    """Converts our bespoke linked list to a python list."""
    o = h
    l = []
    while o is not None:
        l.append(o.value)
        o = o.next
    return l

def mpermutations(multiset):
    """Generator providing all multiset permutations of a multiset."""
    h, i, j = init(multiset)

    yield visit(h)
    while j.next is not None or j.value < h.value:
        if j.next is not None and i.value >= j.next.value:
            s = j
        else:
            s = i
        t = s.next
        s.next = t.next
        t.next = h
        if t.value < h.value:
            i = t
        j = i.next
        h = t
        yield visit(h)



"""
This module encodes functions to generate the permutations of a multiset
following this algorithm:
Algorithm 1
Visits the permutations of multiset E. The permutations are stored
in a singly-linked list pointed to by head pointer h. Each node in the linked
list has a value field v and a next field n. The init(E) call creates a
singly-linked list storing the elements of E in non-increasing order with h, i,
and j pointing to its first, second-last, and last nodes, respectively. The
null pointer is given by φ. Note: If E is empty, then init(E) should exit.
Also, if E contains only one element, then init(E) does not need to provide a
value for i.
[h, i, j] ← init(E)
visit(h)
while j.n ≠ φ orj.v <h.v do
    if j.n ≠    φ and i.v ≥ j.n.v then
        s←j
    else
        s←i
    end if
    t←s.n
    s.n ← t.n
    t.n ← h
    if t.v < h.v then
        i←t
    end if
    j←i.n
    h←t
    visit(h)
end while
... from "Loopless Generation of Multiset Permutations using a Constant Number
of Variables by Prefix Shifts."  Aaron Williams, 2009
"""

operators = ['+', '-', '*', '/']
op_permutations = []

for c in combinations_with_replacement(operators, 3):
    for permutation in mpermutations(list(c)):
        op_permutations.append(permutation)



test = ["" for _ in range(13)]

parentheses = [[[0], [5]], [[0], [9]], [[0, 7], [5, 12]], [[0, 3], [9, 9]], [[0, 0], [5, 9]], [[3], [9]], [[3], [12]], [[3, 3], [9, 12]], [[3, 7], [12, 12]], [[7], [12]]]


def expressions_tester(digits):
    global answer_length
    global answer
    results = []

    for digits_perm in permutations(digits, 4):
        for perm in op_permutations:
            temp = test.copy()
            temp[2] = perm[0]
            temp[6] = perm[1]
            temp[10] = perm[2]

            temp[1] = str(digits_perm[0])
            temp[4] = str(digits_perm[1])
            temp[8] = str(digits_perm[2])
            temp[11] = str(digits_perm[3])

            for i in parentheses:
                temp_2 = temp.copy()

                for index in i[0]:
                    temp_2[index] += '('

                for index in i[1]:
                    temp_2[index] += ')'

                expr = ""

                for j in temp_2:
                    expr += j

                try:
                    value = float(eval(expr))

                    if value > 0 and value.is_integer():
                        results.append(int(value))
                except ZeroDivisionError:
                    continue

    results = sorted(list(set(results)))

    if results[0] == 1:
        length = 1

        for index in range(len(results) - 1):
            if results[index] != results[index + 1] - 1:
                break

            length += 1

        if length > answer_length:
            answer_length = length
            answer = list(digits)


answer_length = 0
answer = []

for i in range(1, 10):
    for j in range(i+1, 10):
        for k in range(j+1, 10):
            for l in range(k+1, 10):
                expressions_tester([i, j, k, l])

print(answer)
