##### -- Quiz week 3 -- ######
### Question 10 ###
dbinom(x=3, size=10, prob=0.3)
dbinom(x=10, size=3, prob=0.3)  
pbinom(q=3, size=10, prob=0.3)

#X ~ Bin(10,03)
#P(X >= 3)
pbinom(q=3, size=10, prob=0.3) 

#Approximate
mean(rbinom(n=10000, size=10, prob=0.3) <= 3)

##### -- Quiz week 4 -- ######
### Qustion 10 ###
sample.size <- 10000000
poissDis <- sum(rpois(n = sample.size, lambda = 2) <= 3)/sample.size
1 - poissDis

### Qustion 11 ###
sample.size <- 100000
poiss <- rpois(n = sample.size, lambda = 7)
bin   <- rbinom(n= sample.size , size=25, prob=1/3)
dis   <- sum( poiss * bin > 20)/sample.size
dis

### Qustion 12 ###
discreteRV <- sample(c(-4, -1, 1, 2), size = 100000, replace = TRUE,
                       prob = c(0.1, 0.2, 0.6, 0.1)) 
discreteRV
sum(discreteRV >= 0.8)/length(discreteRV)

##### -- Quiz week 5 -- ######
### Qustion 9 ###
curve(dnorm(x, 0, 1), from=-4, to=4, ylim=c(0,3.5), col = 1)
curve(dnorm(x, 0, 1/4), from=-4, to=4, add = TRUE, col = 2)
curve(dnorm(x, 0, 1/9), from=-4, to=4, add = TRUE, col = 3)

curve(pnorm(x, 0, 1), from=-4, to=4, ylim=c(0,1), col = 1)
curve(pnorm(x, 0, 1/4), from=-4, to=4, add = TRUE, col = 2)
curve(pnorm(x, 0, 1/9), from=-4, to=4, add = TRUE, col = 3)


curve(dexp(x, 1), xlim=c(0,6), ylim=c(0,1), col = 1)
curve(dexp(x, 1/3), col = 1, add = TRUE)

curve(pexp(x, 1), xlim=c(0,10), ylim=c(0,1), col = 1)
curve(pexp(x, 1/3), col = 1, add = TRUE)
