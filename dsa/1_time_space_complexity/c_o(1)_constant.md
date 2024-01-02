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
- average time for each operation is constant O(1), even though some operation has the worst case time cost, like O(n) or O(log n)
- but the average all operations is O(1)
- doesn't mean all operations is O(1). There are some cases where the complexity is O(n) / O(n log n)
- Example

```
- a list (dynamic array)
- usually when insert an item, the complexity is O(1)
- but if the list capacity is not enough when insert an item, the list will do these operations
    - create a new array with double capacity from the previous array
    - copy item from previous array to new array
    - insert new item to array
- the time complexity is O(n)
- but it only happen a few times
- so the amortized (average) complexity is O(1)
```
