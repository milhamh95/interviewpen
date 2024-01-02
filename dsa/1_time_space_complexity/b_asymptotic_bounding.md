# Asymptotic Bounding

There are 3 bounds

## 1. Upper Bounds
- algorithm growth (time / space complexity) will not exceed it's upper bounded as defined by Big O Notation (worst case)
- Use Big O Notation
- Example 1
```
Function A time complexity is O(n ^ 2)

That means the algorithm growth will not exceed O(n ^ 2) -> upper bound
```

- Example 2
```
Function A time complexity is O(n ^ 2)
Function B time complexity is O(4n ^ 2)

Both function have the same algorithm growth, which is O(n ^ 2).
This means that as the input size grows, 
the time complexity of both functions scales quadratically 
with the size of input

Even tough the constants are different.

n ^ 2 -> quadratic time complexity
```


## 2. Exact Bounds
- algorithm has the same upper and lower bounds
- usually we use Big Theta Notation (Θ) to describe exact / tight bounds
- Example

```
function calculate(n) {
    res = 0
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            res = res + j
        }
    }
    return res
}

it has exact bound asymptotic, which is teta Θ(n ^ 2)
upper bound -> O(n ^ 2)
lower bound -> lower bound -> Ω(n ^ 2)
```

## 3. Lower Bounds
- algorithm scale use the minimum amount of time / spaces to complete a task 
- algorithm can't be more efficient than this bound
- use Ω symbol
- Example

```
function linearSearch(array, key) {
    for (let i = 0; i < array.length; i++) {
        if (array[i] === key) {
            return i;
        }
    }
    return -1;
}

upper bound -> O(n)
lower bound -> Ω(1) -> we found key in the the first element of array
```