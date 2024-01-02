# O(1) "Constant Time"

- work stay constant
- Example 1

```
res = 0
for i = 0; i < 10; i++
    res += i
    
print(res)

time complexity -> O(1)
becase the number of operations is constant, which is 10 times
```

- Example 2

```
def get_element(array, index):
    return array[index]

# Example usage
my_array = [1, 2, 3, 4, 5]
print(get_element(my_array, 2))  # This will print 3

no matter how large the index, the operation to get an element by index is always O(1)
```

- in space complexity, sometimes the space complexity is O(1)
- because interviewer only care the core space complexity of algorithm (allocate hash table, array)
- don't care about the return variable space

## Amortized O(1)
