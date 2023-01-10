##### -- Opgave 4 -- #####
#qt - Student t distribution
qt(0.95, 4)

#propostion 3.6
a <- (1 + 0.5 - 0.5 + 1.5 + 0.5) / 5
b <- ( (1 - a)^2 + (0.5-a)^2 + (-0.5 - a)^2 + (1.5 - a)^2 + (0.5-a)^2 ) / 4
sqrt(b)

data <- c(1, 0.5, -0.5, 1.5, 0.5)
n <- 5
muHat <- mean(data)
sigmaHat <- sqrt(var(data))
(sqrt(n) / sigmaHat) * muHat


##### -- kontrol af bog -- #####
f <- c(14, 3, 12, 2)
mean(f)
meanf <- ((14 + 3 +12 +2 ) / 4)
meanf

var(f)
varf <- 1/3 * ((14 - meanf)^2 + (3 - meanf)^2 + (12-meanf)^2 + (2- meanf)^2)
varf
               
(sqrt(4)/ sqrt(var(f)) ) * mean(f)
(sqrt(4)/ sqrt(var(f)) ) * 7.75
