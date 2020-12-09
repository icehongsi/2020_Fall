#11장
install.packages("xlsx")
library(xlsx)
library(dplyr)
mcars = read.xlsx(file.choose(), 1)
str(mcars)

x = mcars[2:8]
pca = prcomp(x, center = T, scale = T)
pca

#scree plot

screeplot(pca, type = "l", main = "SCREE")
pca %>% summary()

plot(summary(pca)$importance[2, ], ylim = c(0, 1), type = "b",
     ylab = "Proportion", xlab = "PC", main = "Variance Explained")

lines(summary(pca)$importance[3,], type = "b", lty = "dashed")

#행렬도

biplot(pca, cex = 0.8)
