#Opgave 4
#qt - Student t distribution
qt(0.95, 4)

#T6
#propostion 3.6
a <- (1 + 0.5 - 0.5 + 1.5 + 0.5) / 5
a
b <- ( (1 - a)^2 + (0.5-a)^2 + (-0.5 - a)^2 + (1.5 - a)^2 + (0.5-a)^2 ) / 4
sqrt(b)

#Sigmahat ^2 = 0,55

data <- c(1, 0.5, -0.5, 1.5, 0.5)
n <- 5
muHat <- mean(data)
sigmaHat <- sqrt(var(data))
(sqrt(n) / sigmaHat) * muHat


##### -- kontrol -- #####

f <- c(14, 3, 12, 2)
mean(f)
var(f)

meanf <- ((14 + 3 +12 +2 ) / 4)
varf <- 1/3 * ((14 - meanf)^2 + (3 - meanf)^2 + (12-meanf)^2 + (2- meanf)^2)
varf
               
(sqrt(4)/ sqrt(var(f)) ) * mean(f)
(sqrt(4)/ sqrt(var(f)) ) * 7.75

7.75^2

var(f)
((14^2 + 3^2 +12^2 +2^2 ) / 4) - mean(f)^2

((14^2 + 3^2 +12^2 +2^2 ) / 4)
((14 + 3 +12 +2 ) / 4) #mean

a <- mean(f^2)
b <- (mean(f))^2

0.1*14 + 0.2 * 3 +0.3*12 +0.2*2
