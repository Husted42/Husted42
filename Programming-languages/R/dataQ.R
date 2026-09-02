##### -- fittet model -- #####
#data
gaatur<-data.frame(dag=c(1,2,3,4,5,8,9,10,15,17,18,
                         19,22,23,24,25,26,29,30),
                   kmtid=c(12.83,13.68,13.58,12.85,12.08,
                           12.27,11.98,11.99,12.79,12.27,12.42,
                           10.88,12.07,13.19,12.18,11.59,12.59,
                           10.22,11.37))

'Skriv R-kode, der kan bruges til at fitte den angivne lineære
regressionsmodel til data'
                           
fit <- lm(kmtid ~ dag, data=gaatur)
summary(fit)

'beta1Hat := estimate (dag) = -0.05200'
'Et qqPlot og et residualplot'
plot(fitted(fit), residuals(fit))
qqnorm(residuals(fit))

'predektion for dag 31'
predict(fit, data.frame(dag=31))

##### -- MSE -- #####
'If we have an gaussian distribution with muHat(0.9, 0.5, 0.8) = -1.
The we can compute f^joint:'
prod(dnorm(x = c(0.9, 1.5, 1.8), mean=-1, sd = 1))
'mean can also be set to -1.2:'
prod(dnorm(x = c(0.9, 1.5, 1.8), mean=-1.2, sd = 1))

##### -- electricity (book) -- ######
#link to dataset can be found on page 39
df <- read.table("data/electricity_data_9am_training.txt", row.names =  NULL,
                 header = TRUE, sep = "\t", 
                 colClasses = c("character", "numeric", "numeric", "numeric"))
summary(df)
