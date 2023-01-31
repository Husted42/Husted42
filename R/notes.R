########## -- The basic -- ##########
#Differentiate functions
f=expression(x^2+3*x)
D(f,'x')

#intergrate functions
integrand <- function(x) {1/((x+1)*sqrt(x))}
integrate(integrand, lower = 0, upper = Inf)



########## -- Dice throw -- ##########
#Mean
mean(1:6)
sample(1:6, 3, replace = T) #T = True 

#Sample of mean
set.seed(10)
mean(sample(1:6, 10000, replace = T))

#Variance
var(1:6)


########## -- Discrete RV pmf -- ##########
#Roll of a dice
#

set.seed(7)
DiscreteRV <- rep(1/6, 6)

plot(DiscreteRV,
  xlab = "Outcome",
  main = "Distribution"
)

## Discrete RV cdf ##
cdfDiscreteRV <- cumsum(DiscreteRV)

plot(cdfDiscreteRV,
     xlab = "Outcome",
     main = "Cumulative Distribution"
)



########## -- Binominial -- ##########
#X ~ Bin(10,03)
#P(X >= 3)
pbinom(q=3, size=10, prob=0.3) 



########## -- Bernouli -- ##########
#Succses / fail (50/50)
sample(c("S", "F"), 1)

#k = 5, size n = 10, P(k=5)
dbinom(x = 5,
       size = 10,
       prob = 0.5)

#P(2<=k<=6)
sum(dbinom(x = 2:6, size = 10, prob = 0.5))

#plot pdf
k <- 0:10
f <- dbinom(x = k, size = 10,  prob = 0.5)
plot(x = k, 
     y = f,
     main = "Probability Distribution Function")

#plot cdf
g <- pbinom(q = k, 
               size = 10, 
               prob = 0.5)

plot(x = k, 
     y = g,
     main = "Cumulative Distribution Function") 



########## -- Normal distribution-- ##########
#### Mean = 0 & sd = 1
#pmf
curve(dnorm(x),
      xlim = c(-3.5, 3.5),
      ylab = "Density", 
      main = "Standard Normal Density Function") 

#Density of certain positions
dnorm(x = c(-1.96, 0, 1.96))

#cdf
curve(pnorm(x), 
      xlim = c(-3.5, 3.5), 
      ylab = "Probability", 
      main = "Standard Normal Cumulative Distribution Function")

curve(dnorm(x, 0, 1), from=-4, to=4)
curve(dnorm(x, 2, 1), from=-4, to=4, add = TRUE)

