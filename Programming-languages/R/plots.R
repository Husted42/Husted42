########## -- plot Binomial distribution -- ##########
success <- 0:15

#pmf
plot(success,dbinom(success,size=15,prob=.3),
     type='h', #h = Histogram-like plot
     main='Binomial Distribution',
     ylab='Probability',
     xlab ='# Successes',
     lwd=3)

#cdf
plot(success,pbinom(success,size=15,prob=.3),
     type='h', #h = Histogram-like plot
     main='Binomial Distribution',
     ylab='Accumulated Probability',
     xlab ='# Successes',
     lwd=3)


########## -- plot Poisson distribution -- ##########
#pmf
plot(0:10, dpois(0:10, lambda = 2),
     type='p', #p = points
     pch=20,   #The symbol of the points in the plot
     main='Poisson Distribution',
     ylab='p(x)',
     xlab ='# of occurrences',
     lwd=3)

#cmf
plot(0:10, ppois(0:10, lambda = 2),
     type='p', #p = points
     pch=20,   #The symbol of the points in the plot
     main='Poisson Distribution',
     ylab='p(x)',
     xlab ='# of occurrences',
     lwd=3)