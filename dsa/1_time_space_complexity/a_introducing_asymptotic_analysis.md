# Asymptotic Analysis
- Describe the eficiency of an algorithm in the input size become very large
- Focus: `What is the behavior of the algorithm if the input grows larger`
- Not focusing on exact running time or space for specific values of `n`
- In asymptotic analysis, we're mostly interested in how things scale up
- TLDR: Focus on scalability and large input
- Example:

```
In kitchen, we don't care exact minutes it takes to turn on the oven.

We care about tasks that take significantly more time as the number of guests increases.
```

# Why we focus on how things scale up?

## 1. Predicting Performance for Large Inputs

- Asymptotic analysis gives us an understanding of how an algorithm will perform with large inputs
- In real world, we handle a lot of data
- By knowing how algorithm perform with large input, we can
  - Manage resource utilization
  - Bottlenecks and performance issues
  - Competitive advantage
  - Prepare for worst case scenario

## 2. Simplification of Analysis

- Focusing on algorithm scale with large input, we can ignore constant factors
- Those factors don't significantly affect performance for large n
- Example

```
3n ^ 2 + 10n + 5

n ^ 2 -> dominate for large n, greatest factor on algorithm scalability
```