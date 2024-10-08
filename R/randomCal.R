(-1.5)^2+1
6+5+4+3+2+1

((2^11 - 1) / 2^11) - ((2^6 - 1) / 2^6)
31/2048

mean(1/10 : 4/10)

curve(dnorm(x),
      xlim = c(-3.5, 3.5),
      ylab = "Density", 
      main = "Standard Normal Density Function") 

100*(1/2)*(1/2)

#intergrate functions
integrand <- function(x) {x}
integrate(integrand, lower = 0, upper = 20)

0.5 / 0.7

v = sqrt(0.02*0.98)
(-2*0.35)+1*0.35+2*0.3
4*0.35+0.35+4*0.3
0.25^2
v = 2.95-0.0625
sqrt(v)

E = -2*0.2+0.1*-1+0.25+0.3*2
E2 = (-2)^2*0.2^2+0.1*-1^2+0.25+0.3*2^2
v = E2-E^2
sqrt(v)

EXY = (-2*0.15*2) + (1*-1*0.1) + (0.25) + (2*2*0.3)
0.75-0.25*2.95

0.125 / (1.6993*1.178)

1-0.59-0.1
(0.16+0.2)*(-1) + (0.13+0.18)*1
0.36*(-1)+0.58*0.31*1
(-0.18)-(0.58*(-0.05))
0.2/0.58
3*2^3
2+2+4+3+1+6+4+6

qt(0.025, df = 2)
qt(0.975, df = 2)

data <- c(-6, -7, -4)
n <- 3
muHat <- mean(data)
sigmaHat <- sqrt(var(data))
(sqrt(n) / sigmaHat) * muHat


0.3*(-3)+0.7*7
27.2-27.2^2
27.2^2

1*0.1+2*0.3+3*0.6
-1*0.8+1*0.2
-1*0.8+1*0.3+2*0.3+3*0.6
1.9- (2.5*(-0.6))

pi
(4/9)
x/0.5=0.7

qt(0.025, df = 2)
qt(0.975, df = 2)

muHat <- 1/3 * (5.2 + 4.8 + 5.3)

sigmaHat2 <- (1/2) * ((5.2-5.1)^2 + (4.8-5.1)^2 + (5.3-5.1)^2) 
sigmaHat <- sqrt(sigmaHat2)

(sqrt(3)/ sigmaHat) * (muHat - 5)


data("cars")
index.test <- c(11, 37, 50)
index.training <- c(1:10, 12:36, 38:49)
test.data <- cars[index.test, ]
training.data <- cars[index.training, ]
training.data$dist

fit <- lm(speed ~ dist, data=training.data)
summary(fit)

mean(training.data$speed)
mean(fit$speed)

plot(fitted(fit), residuals(fit))

training.data


1+ 1/sqrt(2)
sqrt(2)

n = (9.77-((-0.133)*2013+36.416))^2 + (9.79-((-0.133)*2012+36.416))^2 + (9.81-((-0.133)*2011+36.416))^2


yesGivenSunny * YesGivenCool * yesGivenHigh * yesGivenStrong

yesGivenSunny <- 2/5
yesGivenOvercast <- 4/4
yesGivenRainy <- 3/5

yesGivenHot <- 2/4
YesGivenCool <- 3/4
YesGivenMild <- 4/6

yesGivenHigh <- 3/7
yesGivenNormal <- 6/7

yesGivenWeak <- 6/9
yesGivenStrong <- 3/5

P <- yesGivenSunny * yesGivenOvercast * yesGivenRainy * yesGivenHot * YesGivenCool * YesGivenMild * yesGivenHigh * yesGivenNormal * yesGivenWeak * yesGivenStrong
P

fake = 123954
political = 748346 - fake
reliable = 1226052 - political
total = fake + political + reliable

fake / total * 100
political / total * 100
reliable / total * 100


flush <- (factorial(13) / (factorial(5) * factorial(8)) - 9)
flush
cards <- factorial(52) / (factorial(5) * factorial(47))
4*flush / cards


#Matrix mutiplication
1.1 * 3 + 2*4 + (-1)*(-8) #Wrong
1.1 * 3 + (-1) * 6 #Right c11
1.1 * (-8) + (-1) * 10
3.3 + (-6)
4.4 + (-7)
-8.8 + (-10)
6+21
8+30.5
-16+35 
(-3) + 30

(-6)*(-8)

a = matrix(c(1,3,5,7), ncol=2, nrow=2)
b = matrix(c(2,4,6,8), ncol=2, nrow=2)
a*b

# Exercise 18 p. 71 MatAlgDat
A = matrix(c(1.1, (-1), 2, 3.5, (-1), 5), nrow = 3, ncol = 2, byrow = TRUE)
B = matrix(c(3, 4, (-8), 6, 7, 10), nrow = 2, ncol = 3, byrow = TRUE)

A * B #Not possible? 


#Projekt A b)
#For a = 2
x1 = -(2*2^2+4*2-5) / (3*2 - 4) 
x2 = 2*(2^2-1) / (3*2 - 4)
x3 = (2^2 - 1) / (2*(3*2-4))

x1
x2
x3

x1 + 2 * x2 + 2 * x3
2* x1 + 2 * x2 + 4 * 2 * x3
2 * x1 + 2 * x2 + 2* 2^2 * x3

#For a = (4/3)
a <- (4/3)

x1 <- -(2*a^2+4*a-5) / (3*a - 4) 
x2 <- 2*(a^2-1) / (3*a - 4)
x3 <- (a^2 - 1) / (a*(3*a-4))

x1
x2
x3

x1 + 2 * x2 + a * x3
a * x1 + a * x2 + 4 * a * x3
a * x1 + 2 * x2 + 2* a^2 * x3


