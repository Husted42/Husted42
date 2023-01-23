### Question 10 ###
dbinom(x=3, size=10, prob=0.3)
dbinom(x=10, size=3, prob=0.3)  
pbinom(q=3, size=10, prob=0.3)

#X ~ Bin(10,03)
#P(X >= 3)
pbinom(q=3, size=10, prob=0.3) 

#Approximate
mean(rbinom(n=10000, size=10, prob=0.3) <= 3)

#Calculations
EXY <- 1/4*1/4 * -1 + 1/4 * 1/4 * 1
EXY

# q. 2
EX <- 1/6 * 1 + 2/6 + 3/6 + 4/6 + 5/6 + 1
EY <- 1/8 + 2/8 + 3/8 + 4/8 + 5/8 + 6/8 + 7/8 + 1
EY
6 * EX + 2 * EY + 5