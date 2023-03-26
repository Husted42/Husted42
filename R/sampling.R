#Discrete variable with support {-4.1, 0.3, 1.5, 9.0} 
#and pmf p(-4.1) = 0.15, p(0.3) = 0.25, p(1.5) = 0.3, p(9.0) = 0.3

discreteRV1 <- sample(c(-4.1, 0.3, 1.5, 9.0), size = 1, replace = TRUE,
            prob = c(0.15, 0.25, 0.3, 0.3)) 
discreteRV10 <- sample(c(-4.1, 0.3, 1.5, 9.0), size = 10, replace = TRUE, #Size changed from 1 to 10
                      prob = c(0.15, 0.25, 0.3, 0.3)) 
set.seed(1)
discreteRV1
set.seed(42)
discreteRV1
discreteRV10

#Poisson distribution with lambda=1.7
#n=(Denotes the sample size)
rpois(n=10, lambda = 1.7)
rpois(n=5, lambda = 2)

#Binomial distribution with n = 7 sand theta = 0.6
rbinom(n=10, size=7, prob=0.6)
rbinom(n=50, size=2, prob=0.2)

#Monte Carlo approach
sample.size <- 10000
poissDis <- sum(rpois(n = sample.size, lambda = 4.6) <= 8)/sample.size

set.seed(1)
poissDis
set.seed(42)
poissDis

rnorm

SS <- 654321
sum(rnorm(n = SS, mean = 0, sd = 1) > 2)/SS

fake <- 77304
total <- 377371

fake / total * 100

