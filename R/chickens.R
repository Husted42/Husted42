library(dplyr)
library(tidyverse)


# Load data into table
# data <- read.delim('~/home/husted42/Downloads/chickenData.txt',header = F)
data <- read.delim(
  'C:/Users/Pia/Downloads/chikenData.csv', 
  sep = ",",
  header = T)
head(data, 5)

# Remove non-numeric variables
data$hens <- as.numeric(data$hens)
data <- na.omit(data)

# Clean strings
data$Gender <- str_trim(data$Gender)

# TODO : Outlier filtration

# View columns
data
data$Gender
data$hens

aggregate(data$hens, list(data$Gender), FUN=mean) 
aggregate(data$hens, list(data$alkohol), FUN=mean) 


# TODO : Boxplot




