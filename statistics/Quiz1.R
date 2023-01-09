### Question 10 ###
dbinom(x=3, size=10, prob=0.3)
dbinom(x=10, size=3, prob=0.3)  
pbinom(q=3, size=10, prob=0.3)

#X ~ Bin(10,03)
#P(X >= 3)
pbinom(q=3, size=10, prob=0.3) 

#Approximate
mean(rbinom(n=10000, size=10, prob=0.3) <= 3)

