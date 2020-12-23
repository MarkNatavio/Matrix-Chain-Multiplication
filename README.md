# Matrix-Chain-Multiplication-Calc

========================================
* PLEASE VIEW THIS READ ME IN RAW FORM *
========================================


This is calculator was programmed using Python and it follows a dynamic programming approach.
When run, the program displays:
  1) All calcualtions for the specific space m[i,j] and their corresponding k value
  2) The smallest value of m[i,j] and its k value
  3) The grid of all smallest values calculated

It essentially creates a grid of values of dimensions ixj as such:

m 1 2 3 4 5 6 ... j
1 0 
2 x 0
3 x x 0
4 x x x 0
5 x x x x 0
6 x x x x x 0
...
i

Each empty space is calculated using the formula
  m[i,j] = m[i,k] + m[k+1,j] + P_(i-1) * P_k * P_j; where i <= k < j

The values of P are the dimensions of the matrixes given.

If we have matrices
  A1           A2             A3                  A4
 __ __      __ __ __      __ __ __ __      __ __ __ __ __ __ __
|     |    |        |    |           |    |                    |
|     |    |        |    |           |    |                    |
 -- --      -- -- --     |           |    |                    |
  2x2         2x3         -- -- -- --     |                    |
                              3x4          -- -- -- -- -- -- --
                                                   4x7

The values of P are
P1 = 2
P2 = 2
P3 = 3
P4 = 4
P5 = 7

Runtime: O(n^3)
Space complexity: O(n^2)

Instructions:
1) Input the values of P into the array in line 38
2) Run
3) Split the matrices based on the k values of the minimum value of m[i,j] caclulated

EXAMPLE:
For the example above, the matrices could be multipled as such:
(A1 (A2 A3)) (A4)
(A1 A2) (A3 A4)
((A1 A2) A3) (A4)
(A1) (A2 A3) (A4)
(A1) (A2 (A3 A4))
(A1) ((A2 A3) A4)

To determine which is correct the user must create a grid (provided by the code)
m   1  2  3  4
1 | 0 12 36 92 |
2 | 0  0 24 80 |
3 | 0  0  0 84 |
4 | 0  0  0  0 |

Now we look into space m[1,4], where the smallest value is 92, where k = 3. So we have
(A1 A2 A3) (A4)

Now we look at space m[1,3] (since the bounds created are between A1 and A3. We find that the smallest value is 36, when k = 2. So
((A1 A2) A3) (A4)

And now we have arrived at the answer.

I plan on making the display of the grid better and possibly automate the matrix splitting process
