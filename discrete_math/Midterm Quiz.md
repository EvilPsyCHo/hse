# Midterm Quiz

1. Yes, it is possible. For example:

   Suppose $A = \{1, 2, 3, 4, 5\}$,$B=\{4,5,6\}$. 

   We know $|A|$ = 5 and $|B|=3$

   $A \cup B =\{1,2,3,4,5,6\}$, so the $|A \cup B|=6$.



2. No, it is impossible.

   According to the formula: $|A \cup B| = |A| + |B| - |A \cap B|$, we can calculate the numbers of  both side and check if it is equal.

   - the left side of the equation is 6.

   - the right side of the equation is $5 + 3 - 1 = 7$.
   
   but $ 6 \neq 7$,  so it is impossible.



3. On the right side we have $x \in (A \backslash B) \cup (B \backslash C)$  if x is in one of the set $A \backslash B$ and $B \backslash C$. For decompose this further, $ x \in A \backslash B$ if and only if $ x \in A$ but $x \notin B$, $ x \in B \backslash C$ if and only if $ x \in B$ but $ x \notin C$. So $x \in (A \backslash B) \cup (B \backslash C)$  if and only if x is in at least one of sets A and B, but not in C.

   On the left side we have $x \in (A \cup B) \backslash C$ if and only if $ x \in (A \cup B)$ but $ x \notin C$. For decompose this further, $ x \in A \cup B$ if and only if x is in at least one of set A and B.  So $x \in (A \cup B) \backslash C$  if and only if x is in at least one of set A and B but not in C.

   Thus on both sides of the equation we have the same set and this is equivalence.



4. First, we can divide the plan selection into two stages, the first stage chooses the first and second favorite plans, and the second stage chooses the  overprice plan.

   In stage one, As the two plan cannot be repeated, we just chose 2 plan from 6, This can be calculate by the combination formula, so the number of possible outcomes in stage one is 15.

   In stage two, it can choose any one of the 6 plans, so  the number of possible outcomes in stage two is 6.

   At last, there are 15 outcomes of the first stage and 6 outcomes of the second stage, then there are 15 x 6 = 90 pairs outcomes throughout the process.



5. The solution attempt is wrong, because it calculate the  distance between two house twice. Suppose house A and B, the distance(A, B) is equal to distance(B, A), so we just need calcualte it once, the order is not important.

   According to the above analysis, we need to remove the influence of order,  the number of how many distance we will calculate is 90 / 2 = 45.



6. There are 10 position. Five position for even numbers, and because of the even number is in increasing order, so the internal order is fixed ,  and the same as odd numbers. So we just need to choose 5 position from 10 position for even number,  answer is 10 choose 5 = 252. 



7. Yes,  suppose rolling a fair dice as an random experients, the sample space $ \Omega = \{1, 2, 3,4,5,6\}$, and each outcoms probability of occurrence of each outcomes is 1/6. Let A is event "Roll the dice to appear 1, 2, 3", and B is event "Roll the dice to appear 5, 6". $P(A \cap B)=0$ and $P(A) = 1/2$, $P(B) = 1/3$.



8. The ten people in village represented as $V = \{x_{i}| i = 1, 2, ..., 10\}$. In the  first experiment $A$, it can select 3 of 10 without repeating and the order is not important, so $ A = \{x_i, x_j, x_m \in V| i \neq j, j \neq m\}$, and $|A| = \tbinom{10}{3} = 120$. In the second experiment $B$,  in one year the president would choose 4 times with repeating,  so $ B = \{x_i, x_j, x_m, x_n \in P\}$ and we can use product rule to calculate $|B| = 10 * 10 * 10 * 10 = 1000$. 

   The difference of $A$ and $B$ , in $A$ they select people without repeating in 3 times, and in $B$ they select people with repeating in 4 times.



9. Because of the dice is identical, so the order is not importance, we just focus on the combination of results. And the dice is symmetric, so the probabilities for each side is equal. The sample space of rolling the two dice $\Omega = \{i, j| i, j  = 1,2,3, ..6\}$ and $| \Omega|=18$. 

   Using $A$ denote event "on one dice we obtained 1 and on another we obtained 2",  $P(A) = |A|/|\Omega| = 1/18$.

   Useing $B$ denote evant "we obtained two 1's", $P(B) = |B| / |\Omega| = 1/ 18$.

   I consider the sample space with equal probabilities of outcomes, because the dice is symmetric, so the probabilities of each side should be equal.

