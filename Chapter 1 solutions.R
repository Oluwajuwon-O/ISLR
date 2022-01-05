college = read.csv('College.csv')
View(college)
rownames(college) = college[,1]
View(college)
college = college[,-1]
View(summary(college))
pairs(college[,1:10])
plot = college[,1:10]
plot(plot)
boxplot(college$Outstate,college$Private)
college$Private = as.factor(college$Private)
boxplot(college$Outstate,college$Private, col = 'red')

plot(x = college$Private, y = college$Outstate, col = 'red',
     varwidth = T, annot = TRUE, xlab = 'Private', ylab = 'Outstate')
Elite = rep ("No", nrow (college ))
Elite[college$Top10perc > 50] = 'Yes'
Elite = as.factor(Elite)
college = data.frame(college,Elite)
plot(college$Elite,college$Outstate)
par(mfrow = c(2,2))
hist(college$Top10perc)
hist(college$Enroll, breaks = 15)

#Number 10
View(summary(Boston))
length(Boston)
nrow(Boston)
ncol(Boston)
pairs(Boston)
