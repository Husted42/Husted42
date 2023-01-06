#Differentiate functions
f=expression(x^2+3*x)
D(f,'x')

#intergrate functions
integrand <- function(x) {1/((x+1)*sqrt(x))}
integrate(integrand, lower = 0, upper = Inf)
