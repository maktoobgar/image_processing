# Question

Write an equation which will result a 2nx2n from a 2x2 hadamard matrix.

# Answer

To answer that, let's define what `Kronecker Product` is:

Just take a look at this example:

![](kronecker1.png)

It is obvious what is happening and I gotta say doesn't really matter if they have the same size or not.

Just take a look at this other example:

![](kronecker2.png)

Based on these examples, we can define which when a 2x2 matrix goes through a Kronecker Product with another 2x2 matrix, it becomes a 4x4 matrix and when a 2x3 goes through with a 4x4 matrix, it becomes 8x24, in general:

When a AxB matrix goes through a Kronecker Product with a CxD matrix, it will result a (A\*C)x(B\*D) matrix.

## Solve it With Kronecker

With that same functionality in mind, we can now define:

```
H2 = H1 ⊗ H1
```

or:

```
H4 = H2 ⊗ H2
```

And then define the general rule of:

```
H2n ​= Hn ⊗ Hn ⊗ . . . ⊗ Hn (n times)
```

# Resources

https://en.wikipedia.org/wiki/Kronecker_product

https://mathworld.wolfram.com/HadamardMatrix.html
