#다변량 회귀분석 3번

a <- matrix( c(56,85,34,23,37,21,12,88,58,23,
               63,73,56,14,44,17,32,78,57,52,
               75,69,87,55,29,23,10,23,63,31,
               85,65,65,28,54,74,78,48,42,78,
               3,3,1,2,1,2,1,3,1,1,
               0,0,0,1,1,1,1,0,0,0), byrow = F, ncol = 6)
colnames(a) <- c("y1", "yp", "yc", "v", "e", "s")

x = a[, 4:6]
x1 <- rbind(1,1,1,1,1,1,1,1,1,1)
x <- cbind(x1, x)
x <- as.matrix(x)
x

y <- a[,1:3]
y <- as.matrix(y)
y

b_hat <- solve( t(x) %*% x ) %*% t(x) %*% y
b_hat


# 1 - 6

c(0, 1, 0, 0) # M

#Wilks' Lambda

p = ncol(y)
L = t( c(0,1,0,0))
M = matrix( c(1, -1,
              0, 0,
              1, -1), ncol = 2)
C = cbind(0, 0)
bhat = solve( t(x) %*% x) %*% ( t(x) %*%  y)

H1 = ( t(M) %*% t(bhat) %*% t(L)) - t(C)
H2 = solve(L %*% solve(t(x) %*% x) %*% t(L))
H3 = (L %*% bhat %*% M) - C

H = H1 %*% H2 %*% H3

px = x %*% solve(t(x) %*% x) %*% t(x)
n = nrow(y)
l = diag(n)
E1 = t(M) %*% t(y)
E2 = l - px
E3 = y %*% M
E = E1 %*% E2 %*% E3

det(E) / det(H+E)
