



# Creating a frozenset
print("------------------- Create a frozenset and check its type: ---------------------");

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))




# copy() methoid
print("------------------- copy() methoid ---------------------");

fs = frozenset({1, 2, 3})
cp = fs.copy()
print(fs)
print(cp)




# difference() methoid
print("------------------- difference() methoid ---------------------");

a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4, 5})
print(a.difference(b))
print(a - b)




# intersection() methoid
print("------------------- intersection() methoid ---------------------");

a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4, 5})
print(a.intersection(b))
print(a & b)




# isdisjoint() methoid
print("------------------- isdisjoint() methoid ---------------------");

a = frozenset({1, 2})
b = frozenset({3, 4})
c = frozenset({2, 3})
print(a.isdisjoint(b))
print(a.isdisjoint(c))




# issubset() methoid
print("------------------- issubset() methoid ---------------------");

a = frozenset({1, 2})
b = frozenset({1, 2, 3})
print(a.issubset(b))
print(a <= b)
print(a < b)




# issuperset() methoid
print("------------------- issuperset() methoid ---------------------");

a = frozenset({1, 2, 3})
b = frozenset({1, 2})
print(a.issuperset(b))
print(a >= b)
print(a > b)




# symmetric_difference() methoid
print("------------------- symmetric_difference() methoid ---------------------");

a = frozenset({1, 2, 3})
b = frozenset({3, 4, 5})
print(a.symmetric_difference(b))
print(a ^ b)




# union() methoid
print("------------------- union() methoid ---------------------");

a = frozenset({1, 2})
b = frozenset({2, 3})
print(a.union(b))
print(a | b)
