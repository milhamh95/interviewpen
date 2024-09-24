# Description

Given an integer as input, determine if it is a palindrome.

Input-Output

Example 1

Input: 1234
Output: false

Example 2

Input: 321123
Output: true

Example 3

Input: -12321
Output: false

Constraints

• You may not cast the number to a string

## Solution

- Leetcode: [https://leetcode.com/problems/palindrome-number/submissions/1401022030/](https://leetcode.com/problems/palindrome-number/submissions/1401022030/)
- Edit Explanation: [https://www.tldraw.com/r/1Mwm97cNrLF5AmQn6GACp?d=v-73.-509.1669.1701.page](https://www.tldraw.com/r/1Mwm97cNrLF5AmQn6GACp?d=v-73.-509.1669.1701.page)
- View Explanation: [https://www.tldraw.com/ro/Q4wmzPImyuN6jYBjHMS0a?d=v-73.-509.1669.1701.page](https://www.tldraw.com/ro/Q4wmzPImyuN6jYBjHMS0a?d=v-73.-509.1669.1701.page)

### a. Reverse All Number
- Time complexity: O(log 10 n)
- Space complexity: O(1)

### b. Reverse Half Number
- Time complexity: O(log 10 n)
- Space complexity: O(1)

- we're working with decimal number, base 10
- so we use log base 10
- we can ignore base number (10,2), because in time complexity we only care about the growth / scale of the algorithm as the input size grows very large