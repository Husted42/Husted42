x <- 1.8^2
y <- exp(0.5)
z <- x*y - sqrt(2.4)
z

daysPerMonth <- c(31, 28, 31, 30, 31, 31, 30, 31, 30, 31)
daysPerMonth
length(daysPerMonth)

## ----- ##
#BMI calculator
weight  <- c(65, 77, 84, 82, 93) #kg
height  <- c(158, 180, 186, 179, 182) #cm
heightM <- height/100 #meters
bmi     <- weight/heightM^2
log(bmi)

##Logical Expressions
(height>180)
height[height>180] # height where height is above 180
weight[height>180] # weight where height is above 180
bmi[height>180]    # BMI where height is above 180

sex <- c("F","F","M","M","M")
bmi[sex=="M"]

## ----- ##
#Extracting elements from Vectors
daysPerMonth <- c(31, 28, 31, 30, 31, 31, 30, 31, 30, 31) ##Make list
daysPerMonth[5]           ##Element no. 5
daysPerMonth[-3]          ##All elements but no. 3
daysPerMonth[1:4]         ##Elements no. 1-4
testExtract <- c(1, 3, 5)
daysPerMonth[testExtract] ##Elements no. 1, 3 ,5



## ----- ##
#Matrices
A <- matrix(c(1, 4, 5, 6, 9, 11), nrow=2, ncol=3)
B <- matrix(c(1, 4, 5, 6, 9, 11), nrow=2, ncol=3, byrow=TRUE)
A
B[2,3]
B[1, ]
B[ ,2]

#Matrix Modify
C <- matrix(0, nrow=4, ncol=3)
C
C[,2] <- 1                     # Push 1 to col 2
C
C[4,]  <- c(7,9,13)            # Push vec to row 4 
C[1,3] <- 4                    # Push 4 to (row 1, col 3)
C

## ----- ##
#Simpel plot
year <- c(1804, 1927, 1959, 1974, 1987, 1998, 2011)
worldPop <- c(1:7)
plot(year, worldPop, type="b") # Scatter plot with points and lines (right)
plot(year, worldPop, type="l") # Only line segments (not shown)

#Types of plots
cricketdata <- read.table("lecture1-crickets.txt", header=TRUE)
#Plot
   plot(bodywt,eggs)
#histogram
   hist(bodywt)                    # Histogram with default breaks
   hist(bodywt,breaks=c(0,2,4,6))  # Histogram with breaks at 0,2,4,6
#boxplot
   boxplot(bodywt)                 # Boxplot (left in figure below)
#QQ-plots for comparing
   x <- runif(200, 0, 1)           # 200 independent uniform variable
   y <- runif(200, 0, 1)           # 200 independent uniform variable
   z <- y^2
   qqplot(x,y)                     # QQ-plot of x and y (left graph below)
   abline(0,1)                     # Add x=y line
   qqplot(x,z)                     # QQ-plot of x and y (right graph below)
   abline(0,1)                     # Add x=z line

x <- (1:10)
y <- (1:10)^2
plot(x,y)

#Help plot
plot(x,y,ylim=c(-50,50)) #vertical range
plot(x,y,col="red")      #color of points
plot(x,y,lwd=3)          #size of points
plot(x,y,pxh=2)          #shape of points
plot(x,y,type="l")       #type of points

##Example
f1 <- function(x) log(x)
plot(f1, xlim=c(1,10))


## ----- ##
#Data Frames
data(trees) #Loads build-in data set

head(trees) #Gets the first 6 rows
nrow(trees) #The total no. of rows
dim(trees)  #dimmension (row 31, col 3)
str(trees)  #Structure
mean(trees$Girth) #Average girth
attach(trees)
median(Girth)     #Median
sd(Girth)         #Standard deviation    
max(Girth)        #maximum value
min(Girth)        #minimum value
fivenum(Girth)    #min, 24%, Median, 75% max
detach(trees)
summary(trees)

## ----- ##
funSum <- function(value1, value2) {
  results <- value1 + value2
  return(results)
}

funSum(10,20)

funDiv <- function(value1, value2) {
  results <- value1 / value2
  return(results)
}

funDiv (10,20)
funDiv (value2 = 10, value1 = 20)

## ----- ##
#Data from file
getwd()
setwd('C:/C/Statestik/probabilityTheoryAndStatistics/01introduction')
cricketdata <- read.table("lecture1-crickets.txt", header=TRUE)
head(cricketdata)
summary(cricketdata)

#File contains eggs and bodywt
cricketdata$bodywt
cricketdata$eggs

#Attach (direct acsses)
attach(cricketdata)
bodywt
detach(cricketdata)
bodywt                  #Displays error: Criketdata deatached

#Subset of dataframes
cricketdata <- transform(cricketdata, logbodywt=log(bodywt))
cricketdata             #Collum has been added to criketdata


## ----- ##
#Functions
dnorm(0.5, 0, 1, FALSE)
dnorm(sd=1, log=FALSE, x=0.5, mean=0)

f <- function(x) x^3 +4*x - 8
g <- function(x,y) x^2 + y^2
f(3)
g(3, 5)

curve(f, from=-1, to=5)
plot(f, from=-1, to=5)
z <- 3 * 2 + exp(8.5)
i <- sqrt(36)
zi <- z+i
zi

FS <- function(x, y=2){
  return(x^2+y^2)
}
FS(2,3)
FS(2)

# x <- seq(start, slut, afstand mellem værdier)
x <- seq(1, 20, 1)
x

f1 <- function(x,y,z){
  return((sin(x))*y+4*sqrt(z))
}
f1(3/4*pi,17,2)

## ----- ##
#If/Else statements
f1 <- function(x) if(x<10){
  print("x er mindre end 10")
} else {
  print("x er større end 10")
}

f1(11)

choice <- 3
if(choice == 1){
  print("choice: 1")
}else if(choice == 2){
  print("Choice: 2")
}else{
  print("choice>2")
}



f2 <- function(x,y)if(x+y>5){
  return(x^2)
}else{  #Komplentær mængden
  return(y^2)
}

f2(3,1)

f3 <- function(x,y)if(x+y>5){
  return(x^2)
}else if(x+y==5){
  print("x+y=5")
}else{
  return(y^2)
}

f3(2,1)
f3(3,2)
f3(3,3)


## ----- ##
#Exercise 3
#Opgave 1.1
rep(c(0),3)

w <- c(rep(0,3), rep(1,3)) #b
x <- c(2*seq(1,5,1))       #c
y <- c((-1)^seq(1, 5, 1))  #c
z <- c(1, 2^seq(1,6))      #d

x
y
x %*% y
x+z        #g - Short vector start over
z1 -> head(z, -1)  #i

## ----- ##
#Exercise 4
# - a
g <- function(x,y)
  if((y > ((abs(x))^(2/3)) - sqrt(1-x^2))){
    TRUE
  }else if((y > ((abs(x))^(2/3)) + sqrt(1-x^2))){
    TRUE
  }else{
    FALSE
  }
# - b
g((-0.5), (-0.5))
g(0, -0.5)
g(0.5, -0.5)

# - c NOTFIXED
g(c(-0.5, 0, 0.5), c(-0.5, -0.5, -0.5))

#Exercise 1.3a
x <- c(4,9,1,4,5,7,10,1,4,5) #Create vector
x[c(seq(1,length(x),2))]     #Extract 1fs, 3rd, 5th ... element

#Exercise 1.4.
a <- TRUE + 1 #True = 1, FALSE = 0
a

set.seed(80)  #same random values
b <- sample(c(TRUE, FALSE), size = 10, replace = TRUE)  #Random vetor of TRUE and FALSE
b

c1 <- TRUE * TRUE  #1*1=1
c2 <- TRUE * FALSE #1*0=0
c3 <- TRUE * 1     #1*1=1
c4 <- FALSE * 1    #1*0=0
c(c1, c2, c3, c4)

d <- "Hello" + "world" #non-numeric argument to binary operator
d

#Exercise 1.5. -  Extra
a1 <- head(rep(c(letters),1), 5)
b1 <- head(rep(c(paste (letters, rep(1,1), sep=""))), 5)
c1 <- paste(b1, collapse = "")

set.seed(101)                                                                 #Controlled randomness
d1 <- replicate(10, paste(sample(letters, 6, replace = TRUE), collapse = "")) #Vector of random strings
d2 <- substring(d1, first=3, last=4)                                          #Pulls 3rd and 4th letter in every string
e1 <- sapply(lapply(strsplit((d1[1:6]), NULL), rev), paste, collapse="")      #Reverse characters
f1 <- sapply(lapply(strsplit((d2), NULL), rev), paste, collapse="")           #Reversed d2

#Exercise 2.1 
M1 <- matrix(1:12, nrow = 3, byrow = FALSE)  #a: Creates matrix by column
M2 <- matrix(1:12, nrow = 3, byrow = TRUE)   #b: Creates matrix by row

b1 <- M1[1,1]   #1st entry
b2 <- M2[2, ]   #2nd row
b3 <- M2[ ,4]   #4th column

c1 <- M1 %*% M2 #%*% is for summing vectors into entry
c2 <- M1*M2     #Multiplying entries

#Exercise 2.2
M <- matrix(1:9, nrow = 3, ncol = 3)
M[,2] <- letters[1:3]
t(M[,1])%*%M[,1] #a: Can't have to types of data in one object


b1 <- matrix(1:9, nrow = 3, ncol = 3)
t(b1[,1]%*%b1[,1])

#Exercise 2.3
diag(3) #a: diagonal matrix
a1 <- matrix(1:9, nrow = 3, ncol = 3) #row = 3 and column = 3
upper.tri(a1, diag = F) #a: diag - incloude diagonal TRUE or FALSE
lower.tri(a1, diag = T) #a: diag - incloude diagonal TRUE or FALSE

b1 <- matrix(nrow = 4, ncol = 4)
diag(b1) <- 0
b1[upper.tri(b1)] <- 1
b1[lower.tri(b1)] <- 2
b1

#Example 2.3 - Dice
die <- 1:6
result <- sample(x = die, 1000, replace=TRUE) #100 rolls with dice
table(result)                                #Table showing results of rolling 100 times

dfTotal <- data.frame(table(result))
dfProb <- cbind(dfTotal, prop.table(dfTotal$Freq))
names(dfProb) <- c("Resukt", "Freq", "Probability")
dfProb

rbinom(1000, 9, 0.9)
pbinom(7, 9, 0.9)

# define both estimators
hatthetaML <- function(abba) {
  return(max(abba))
}
hatthetaCL <- function(abba) {
  return((length(abba) + 1)/length(abba) * max(abba) - 1)
}
# We first consider a single experiment
set.seed(1)
X <- sample(1:686, size = 4, replace = FALSE)
X














