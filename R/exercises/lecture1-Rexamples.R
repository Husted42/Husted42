#########################
### SandStat, Rintro
#########################
# This file shows some examples for programming in R. 

# Most importantly, please try R out yourself! It is not 
# possible to learn how to program from just reading about 
# it (this is similar to doing mathematics).  

# This file targets students who do not have any programming 
# experience yet. Thus, the language is meant to be 
# intuitive and may differ from what is taught in 
# computer science, for example.  

# Lines starting with # are ignored by R. This is great for writing comments.

# HINT: You can run commands from a file by opening 
# this file in rstudio and then use a shortcut, e.g., 
# for running individual lines (e.g., Ctrl+Enter).


############################
############################
### PART I
############################
############################


############################
### simple calculations 
############################

5*4
2+3*9
5/7
4^3
sqrt(0.49)
sin(pi/2)
sin(pi)
exp(log(5))
log10(10000)

############################
### defining variables
############################

x <- 0.4
x
y <- 2
x*y
rm(x) # removing a variable
x

############################
### vectors
############################

x <- c(1,6,2,5,9)
x[3] # 3rd entry        
x[c(1,3,4)] 
x[-c(2,5)] # without entry 2 and 5


# There are some easy ways to create vectors in R.
y <- 1:5
y
z <- rep(1,7)
z
w <- seq(1,9,2)
w

# important summary functions
sum(x)
mean(x)
min(x)
max(x)
range(x)
length(x)


# We can apply computations to 
# each element of a vector.
x^2
x+2
log(x)

x + c(1,2) # watch out for warnings

############################
### Logical expressions
############################
# Variables cannot only take values such as 4.2 or 0.0001 
# but also TRUE or FALSE. 

x <- TRUE
42==(2+40) 
y <- (42==(2+40))
y
1==2 
1<1
1<=1
1!=2 
1==2 & 1==1 # & means "and" 
1==2 | 1==1 # | means "or"

(1<2 & 1==3) | (2==3 | 1!=4) # can you guess what this gives us?

x>3
x[x>3]

# there is a difference between && and & (the latter is 'vectorized') 
c(TRUE, FALSE, TRUE) && c(FALSE, TRUE, FALSE)
c(TRUE, FALSE, TRUE) & c(TRUE, TRUE, FALSE)

############################
### "if"-statements
############################
x <- 5
if(x < 5){
  print("x is smaller than 5.")
} 

# distinguishing between two cases
thirsty <- TRUE
if(thirsty){
  take.glass <- TRUE
  print("I will take a glass now.")
} else {
  take.glass <- FALSE
}

# distinguishing between more than three cases
choice <- 1
if(choice == 1){ 
  print("Here you are: a single espresso")
} else if(choice == 2){
  print("Good choice: a double espresso!")
} else if(choice == 3){
  print("Really?")
} else {
  print("I do not understand the choice.")
}


############################
### functions 
############################

mette <- function(x){
  z <- x^2
  return(z)
}
mette(2)


# some functions (but not all) allow for plugging in vectors
mette(1:6) 

## Hint: you can use '=' to set a 'standard' value:
morten <- function(x, y = 2){
  return(x^2 + y^2)
}
morten(x = 2, y = 3)
morten(2, 3)
morten(4)



############################
### plotting
############################

x <- 1:10
y <- (1:10)^2
plot(x,y)
plot(x,y, ylim=c(-50,50)) # changing vertical range
plot(x,y,col="red") # color of points
plot(x,y,lwd=3) # size of points
plot(x,y,pch=2) # shape of points
plot(x,y,type="l") # lines rather than points

plot(mette) # we can even plot a whole function from R to R

?plot # built-in R functions have a 'help'-page, which can be very useful
?sin
?sqrt

crazy <- function(x,y){
  return((cos(x*y+cos(4*y)))^2+sin(y) > 0.4*x+0.1*y^2)
}
crazy(-1,2)
crazy(4,2)
# how can plot the area, where this function is TRUE?



# How would you do it? 

lengout <- 10
x <- seq(-6,6,length.out = lengout)
y <- seq(-6,6,length.out = lengout)
x <- rep(x,times=lengout)
y <- rep(y,each=lengout)
#check out what this is doing
plot(x[crazy(x,y)],y[crazy(x,y)], pch = 16, cex = 0.5)
# now repeat the above with a larger value of lengout. 




## Installing and loading packages

## There are many packages with useful additional functions (that someone
## programmed and then put online). You can install packages using the command
## install.packages. E.g., try to run
permutations(4,4)
## This should give an error because there is no function with this name. 
## Now, run
install.packages("gtools")
## If installed (you only need to do this once). You can then load 
## the package with
library(gtools)
## Now you should be able to run 
permutations(4,4)




# You can skip the rest of this file for now. 
# We will come back to this later.

############################
############################
### PART II
############################
############################

############################
### sampling
############################

sample(x=1:10, size = 5, replace = TRUE) # draw 5 random numbers from 1 to 10 with replacement
sample(x=1:10, size = 5, replace = FALSE) # draw 5 random numbers from 1 to 10 without replacement

rnorm(n=10, mean=1, sd=.5) # draw 10 independent Gaussian variables
rbinom(n=3,size=10,prob=.3) # draw 3 independent binomial variables

rnorm(1)
rnorm(1)

set.seed(17)
rnorm(1)
set.seed(17)
rnorm(1)

############################
### data frames
############################

df <- data.frame(x=rnorm(5), y=rnorm(5))
df
df$x
df$y
df$zz <- c("fire", "water", "air", "earth", 0)
# try running 
# zz
# (that is, without the 'df$' in front of it)
# this gives an error (zz is only defined within the data frame)
df$zz
summary(df)
colnames(df)
rownames(df)





############################
### Reading data from external file
############################

## make sure the file cricket.txt (can be found on absalon under files/data) is in the same folder as this R file
cricketdata <- read.table("lecture1-crickets.txt", header = TRUE)
head(cricketdata)
dim(cricketdata)


############################
### transforming and subsetting data
############################
smallcrickets <- subset(cricketdata, bodywt<4)                # Only small crickets
dim(smallcrickets)
cricketdata <- transform(cricketdata, logbodywt=log(bodywt))  # New variable
head(cricketdata)


############################
### Plotting
############################

plot(cricketdata$bodywt, cricketdata$eggs)   # Method 1: Use $ syntax
with(cricketdata, plot(bodywt, eggs))        # Method 2: Use "with"
plot(cricketdata)

## Graphs
plot(cricketdata$bodywt, cricketdata$eggs)
abline(-72.05, 31.78, col="red")

plot(cricketdata$bodywt, cricketdata$eggs, 
     xlab="Body weight", ylab="Number of eggs",
     xlim=c(0,5.3), ylim=c(0,140), pch=16, 
     col="blue", main="Cricket data")

hist(cricketdata$bodywt)
hist(cricketdata$bodywt,breaks=c(0,2,4,6))



############################
############################
### PART III: SOMETHING EXTRA
############################
############################




############################
### "for"-loops
############################

x <- 1:5
y <- rep(0,5)
for(i in 1:5){
  y[i] <- x[i]^2
}
y

z <- 0
for(i in 1:10){
  z <- z+1
}
z

# To code nice and fast, try to avoid for loops (in particular, the above for 
# loops could be avoided) 

eap.pro.x <- 1
for(i in 1:10){
  eap.pro.x <- eap.pro.x + 1/factorial(i)
  print(eap.pro.x)
}
# Can you guess what this does?



############################
### matrices 
############################

# A matrix is just a table of numbers: You have rows and columns.

A <- matrix(c(1,2,3,4,5,6), nrow = 3, ncol = 2)
A
A <- matrix(c(1,2,3,4,5,6), nrow = 3, ncol = 2, byrow=TRUE) 
A
# The matrix A has 3 rows and 2 columns. We call this a (3x2) matrix. 
# Important to remember: first comes the number of rows, then the number of cols 
# (foeRRRst row, columns ccccenere ;-))

B <- matrix(c(1,2,3,4,5,6), nrow = 2, ncol = 3)
B

B[1,1]
B[1,c(1,2,3)]
B[1,]
B[,1]
B[2,2] <- 17
B
B[1,] <- c(0,0,55)
B

t(B) # the 'transpose' of B


## entry-wise operations
A+2
A^2
A/2

C <- matrix(c(1,4,7,10,0,1), nrow = 2, ncol = 3)
B
C
B*C # will this give an error?

## important functions
rowSums(A)
colSums(A)
rowMeans(A)
colMeans(A)
dim(A)
nrow(A)
ncol(A)

## matrix-vector and matrix-matrix multiplications. 
x <- c(1,2)
A %*% x
A %*% B


## inverse of matrix.
D <- matrix(c(1,2,3,4,5,1,1,1,1), nrow = 3, ncol = 3) # is D invertible?
D
det(D) # indeed!
Dinv <- solve(D)
D %*% Dinv


