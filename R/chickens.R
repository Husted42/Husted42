library(dplyr)

# data <- read.delim('~/home/husted42/Downloads/chickenData.txt',header = F)
# Load dat into table
data <- read.delim(
  'C:/Users/Pia/Downloads/chikenData.csv', 
  sep = ",",
  header = T)
head(data, 5)

# Remove non-numeric variables
data$hens <- as.numeric(data$hens)

data <- data %>% 
  drop_na()


data$Gender
data$hens

aggregate(data$hens, list(data$Gender), FUN=mean) 


