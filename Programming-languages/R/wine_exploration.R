# https://www.geeksforgeeks.org/prediction-of-wine-type-using-deep-learning/?ref=rp 
# Fixed acidity :
  # The total acidity is divided into two groups: the volatile acids and the nonvolatile or fixed acids.
  # The value of this variable is represented by in gm/dm3 in the data sets.
# Volatile acidity: 
  # The volatile acidity is a process of wine turning into vinegar. 
  # In this data sets, the volatile acidity is expressed in gm/dm3.
# Citric acid : 
  # Citric acid is one of the fixed acids in wines. 
  # It’s expressed in g/dm3 in the data sets.
# Residual Sugar : 
  # Residual Sugar is the sugar remaining after fermentation stops, or is stopped. 
  # It’s expressed in g/dm3 in the data set.
# Chlorides :
  # It can be a important contributor to saltiness in wine. 
  # The value of this variable is represented by in gm/dm3 in the data sets.
# Free sulfur dioxide : 
  # It is the part of the sulfur dioxide that is added to a wine. 
  # The value of this variable is represented by in gm/dm3 in the data sets.
# Total Sulfur Dioxide :
  # It is the sum of the bound and the free sulfur dioxide.
  # The value of this variable is represented by in gm/dm3 in the data sets.


########## ---------- Imports ---------- ##########
# install.packages("tidyverse")

library(ggplot2)
library(GGally) # ggcorr
library(stringr) # str_sort

# Read in white wine data
original_white <- read.csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv", sep=";", header=TRUE)
white <- original_white

# Read in red wine data
orginal_red <- read.csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", sep=";", header=TRUE)
red <- orginal_red 

# Merging datasets
red_ <- red
white_ <- white

red_$class <- rep('red', dim(red_)[1])
white_$class <- rep('white', dim(white_)[1])

df = rbind(red_, white_)

head(df)

########## ---------- Exploration ---------- ##########
##### ----- Overview ----- #####
### Dimensions
red_d <- dim(red)
white_d <- dim(white)
red_d
white_d 

### Descirbe
summary(red)
summary(white)

### Structure
str(red)
str(white)

#### Sort columns alphabetically
red = red[, str_sort(names(red))]

names(red)

### Explore quality
# We only have label 3, 4, 5, 6, 7 and 8
# [Note] :
  # It might make sense to do a classification task of low, medium and high, 
  # but this can be a problem sicne the data is quite skewed 

# Simple barplot of quality
labels = as.numeric(str_sort(unique(df$quality)))
p <- ggplot(data=df, aes(x=quality)) +
  geom_bar() +
  # vjust : Adjust text vertically
  geom_text(stat='count', aes(label=after_stat(count)), vjust=-1) + 
  scale_x_continuous(breaks = labels)
p

# 

### Explore Alcohol
# min, max = 8, 14.2
labels = c(8:15)
p <- ggplot(data=red, aes(x=alcohol)) +
  geom_histogram(color="blue", fill="white", binwidth=0.0005) +
  scale_x_continuous(breaks = labels) + 
  geom_density(alpha=.2, fill="blue")
p

labels = c(8:15)
p <- ggplot(data=white, aes(x=alcohol)) +
  geom_histogram(color="blue", fill="white", binwidth=0.0005) +
  scale_x_continuous(breaks = labels) + 
  geom_density(alpha=.2, fill="blue")
p


# [Idea] :
  # Linear regression between density and fixed.acidity
  # E(y) = b_0 * x + b_1
  # H_0 : b_0 = 0 There is not a significant linear correlation between density and fixed.acidity

##### ----- Preprocessing ----- #####
### Scale
min_max_normalization <- function(x) {
  return ((x - min(x)) / (max(x) - min(x)))
}
if (1) {
  red = min_max_normalization(red)  
} else if (0) {
  red <- scale(red)
}

##### ----- Correlation matrix ----- #####
# Copy dataset 
red_ <- red
white_  <- white

### Feature engineering : Remove subcategories
red_$acidity = (red_$fixed.acidity + red_$volatile.acidity) / 2
red_$sulfur.dioxide = (red_$free.sulfur.dioxide + red_$total.sulfur.dioxide) / 2

red_subcategories = c(
  "fixed.acidity", "volatile.acidity",
  "free.sulfur.dioxide", 'total.sulfur.dioxide'
)
red_ = red_[ ,!names(red_) %in% red_subcategories]

### Plot corralation matrix
ggcorr(red_, 
       method = c("everything", "pearson"),
       label = TRUE
)

ggcorr(white_, 
       method = c("everything", "pearson"),
       label = TRUE
)

##### ----- Finding potential linear relationships ----- #####
plot(white$quality, white$alcohol,
     xlab = 'Alcohol', ylab = 'residual.sugar')

##### ----- Linear correlation between alchol and sugar ----- #####
#### From the scatterplot it beacomes obivous that there is not a linear relationship
# Preprocessing : Removin outliers in residual.sugar
boxplot(white$residual.sugar,
        main = 'Boxplot for finding outliers')
white <- subset(white, white$residual.sugar <= 20 )

# Preprocessing : Logarithmic scale
white$residual.sugar <- log(white$residual.sugar + 0.1)


##### Plot the distributions
plot_variable_distribution <- function(data, column) {
  labels <- c(floor(min(column)):ceiling(max(column)))
  ggplot(data = data, aes(x=column)) + 
    geom_histogram(binwidth = 0.1) +
    scale_x_continuous(breaks = labels)
}

plot_variable_distribution(white, white$alcohol)
plot_variable_distribution(white, white$residual.sugar)

##### Scatter the values against each other
plot(white$alcohol, white$residual.sugar,
     xlab = 'Alcohol', ylab = 'residual.sugar')

plot(white$residual.sugar, white$alcohol,
     xlab = 'residual.sugar', ylab = 'Alcohol')


