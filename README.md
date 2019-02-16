# Moloco Coding Challenge

### 

### Q1.

**Execution Guide:**

```python3 -m doctest q1.py```

If you want to add more test cases, you can add more doctest in the `q1.py` file.



**Runtime Analysis:**

Generally, it should be $O(|x| + |y|)​$ given that we do not know the length of x and y.

However, 

if $|x| > |y|​$,

​	$O(|x|)​$

if $|x| < |y|$,

​	$O(|y|)$

if $|x| == |y|$,

​	$O(|x|)$ **or** $O(|y|)$



### Q2.

**Execution Guide:**

Type following on your bash and compare the results.

```python
>>> solver = Solution() 
>>> solver.process('sample.csv')
>>> solver.printRank()
```



**Runtime Analysis:**

>  N: nubmer of json files

>  P: number of product 

>  U: number of users

If max(N, P, U) == N,

​	$O(N)​$

If max(N, P, U) == P,

​	$O(P\log P)​$

(This is because `Counter#most_common` is based on heap)

If max(N, P, U) == U,

​	$O(U)​$	

