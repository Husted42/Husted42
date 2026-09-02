# Probabilities introduction

Conditional probabilities:
$$
P(\beta | \alpha) = \frac{P(\alpha\cap\beta)}{P(\alpha)}
$$
Chain rule:
$$
P(\alpha \cap \beta) = P(\alpha)P(\beta | \alpha)
$$
Bayes rule:
$$
P(\alpha | \beta ) = \frac{P(\beta | \alpha)P(\alpha)}{P(\beta)}
$$
General version of Bayes rule for some background event gamma:
$$
P(\alpha | \beta \cap \gamma) = \frac{P(\beta | \alpha \cap \gamma)P(\alpha|\gamma)}{P(\beta | \gamma)}
$$

### Independence events

An event $\alpha$ is independent of an event $\beta$ in P:
$$
P :=(\alpha \bot \beta), \text{ if } P(\alpha |\beta ) = P(\alpha) \text{ or if  } P(\beta) = 0
$$
A distribution P satisfies $(\alpha \bot \beta)$ if and only if $ P(\alpha \cap \beta) = P(\alpha) P(\beta) $​​ 

Joint distributions of $(X_1, X_2) \in \{0,1\} \times \{0,1\}$ parametrized by $\theta_1, \theta_2, \theta_3, \theta_4 \geq 0$ satisfying $  \theta_1 + \theta_2 + \theta_3 + \theta_4 = 1  $ 

### Conditional independence

We say that an event $\alpha$ is conditionally independent of event $\beta $ given event $\gamma$ in P
$$
P := (\alpha \bot \beta | \gamma ) \text{ if } P(\alpha | \beta \cap \gamma) = P(\alpha | \gamma ) \text{ or if } P(\beta \cap \gamma) = 0
$$
Alternative definition:
$$
P \text{ satisfy } (\alpha \bot \beta | \gamma) \text{ if and only if } P(\alpha \cap \beta | \gamma ) = P(\alpha | \gamma ) P(\beta | \gamma)
$$
Example: If a student applies to two universities Stanford and MIT and both universities decides applicants only based on grade. Then MIT is conditionally independent of Standford given Grade, meaning that the fact that the student get's in to Standford does not change the probability of that student getting in to MIT.
$$
P(MIT | stanford, Grade) = P(MIT | Grade)
$$
**Using this we can rewrite the joint distributions as follows:**
$$
P(S,I) = P(S|I)P(I)
$$
Which we can interpret graphically as

![](.\Assets\r1-two-notes.png)

Pointing from what we condition on $I \rightarrow P(I)$ to the other variable $S \rightarrow P(S|I)$​

Let's consider an additional variable, where G is the grade, S is the SAT score and I is the IQ
$$
P(G,S,I) = P(G,S|I)P(I)
$$
Assume $ G \bot S | I $ then we have
$$
P(G,S|I) = P(G|I)P(S|I)
$$
and we get the joint probability
$$
P(G,S,I) = P(G|I)P(S|I)P(I)
$$
![r2-three-notes](C:\C\github\code\modComp\Assets\r2-three-notes.png)

### Independence of random variable

This is just the generalization of independence to sets of random variables:

We say that **X** is conditionally independent of **Y** given **Z** in a distribution P:
$$
P(X=x \bot Y = y |Z = z) \: \forall \: x \in Val(X), y \in Val(y), z \in Val(Z)
$$
The distribution P satisfy $ (X \bot Y | Z ) $ if and only if  $ P(X,Y | Z) = P(X|Z)P(Y|Z) $ 

### Random variables

We define a random variable X  and use Val(X) to denote the set of values

 st.
$$
P(X = x) \geq 0 \forall x \in Val(X)
$$

### LSE : Linearly Structured Equation model

Consider the SAT example and let $Val(I) = \mathbb{R}, Val(G) = \mathbb{R}, Val(S) = \mathbb{R} $  then we can consider the linear factor model:

$ I \textasciitilde \mathcal{N}(\alpha_1;\sigma_1^2) $ 
$$
G |I = x \textasciitilde \mathcal{N}(\alpha_G + \beta_Gx; \sigma_G^2)
$$

$$
S |I = x \textasciitilde \mathcal{N}(\alpha_S + \beta_Gx; \sigma_S^2)
$$

Which can be written as a LSE model
$$
I = \alpha_1 + \sigma_1 \epsilon_1
$$

$$
G = \alpha_G + \beta_G I + \sigma_G\epsilon_2
$$

$$
S = \alpha_S + \beta_S I + \sigma_S\epsilon_3
$$

where $\epsilon_1, \epsilon_2, \epsilon_3$ are independent with a $\mathcal{N}(0;1)$ distribution

## Map queries

The task of finding a high-probability join assignment to some subset of variables.

To find the most likely assignment to the variables in W given the evidence E = e:
$$
MAP(W|e) = arg \max_w P(w,e)
$$
"However, the assignment where each variable individually picks its most likely value can be quite different from the most likely joint assignment to all variables simultaneously"

Let the probabilities in a two node chain $ A \rightarrow B $ where both are binary be $a_0 = 0.4$ and $a_1 = 0.6$ Then we have that $ MAP(A) = a_1 $ , but because of the joint probabilities with B:
$$
\begin{bmatrix}
	A & b_0 & b_1 \\
	a_0 & 0.1 & 0.9 \\
	a_1 & 0.5 & 0.5
\end{bmatrix}
$$
We see that $MAP(A,B) = (a_0, b_1)$ and thus we have that
$$
arg \max_{a,b} P(a,b) \neq (arg \max_{a} P(a), arg \max_{b}P(b))
$$

# Distributions 

### Multinomial distribution

Consider looking at SS notes

### Bernoulli distribution

# Bayesian networks

A
