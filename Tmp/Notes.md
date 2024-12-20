https://feog.github.io/chap4dm.pdf p. 5 shows that if there exist an optimal solution this solution can be found at an extreme point

Given the a minimization problem
$$ Min \: z =  2p_1 + 4p_2 $$
$$ p_1 \leq 3 $$
$$ p_2 \leq 4 $$

$$ \sum^I_{i=1} p_i = 5 $$
$$ p_i > 0 \: \forall i \in [0,1] $$

And it's correspondign dual problem
$$ \texttt{Max } z = 3 q_1 + 4q_2 + 5p_0 $$
$$ q_1 + q_0 \leq 2 $$
$$ q_2 + q_0 \leq 4 $$
$$ q_0 \texttt{ free} $$
$$ q_1, q_2 \geq 0 $$

How do I find all the solutions to the dual solutions that with the primal solutions furfill complementary slackness?