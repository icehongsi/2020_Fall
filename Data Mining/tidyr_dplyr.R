install.packages("tidyverse")
library(tidyverse)
raw = read.csv(file.choose())
head(raw)

#read_csv의 경우 R에서 불러들이는 속도보다 10배 가량 빠름!
#raw = read_csv(file.choose())
#head(raw)

long_raw = gather(raw, type, temp, -Source, -Year)
#gather(사용할 데이터, 새로 만들 변수명, 값)
long_raw

wide_raw = spread(long_raw, type, temp)
head(wide_raw)
head(raw)

?separate
'''
separate ... character 변수를 구분 (분리)시키는 함수
'''

sep_long_raw = separate(long_raw, type, c("type_head", "type_year"))
head(sep_long_raw)

long_raw = unite(sep_long_raw, type, type_head, type_year, sep = ".")
head(long_raw) #type 변수의 separator가 .으로 변경됨

wide_raw = spread(long_raw, type, temp)
head(wide_raw, 10)

sub_raw = select(wide_raw, Source, Anomaly.1y:Anomaly.10y)
head(sub_raw)

sub_raw = select(wide_raw, 1, 3, 5)
head(sub_raw)

sub_raw = select(wide_raw, Source, starts_with("Anomaly"))
#Anomaly로 시작하는 변수만 선택
head(sub_raw)

fil_raw = filter(sub_raw, Source == 1)
head(fil_raw)
#source가 1인 데이터만 추출

tmp = filter(sub_raw, Anomaly.10y > 0)
head(tmp) # anomaly.10y가 양수인 것만 추출
summary(tmp)

group_raw = group_by(sub_raw, Source)
group_raw #특정 그룹끼리 묶음, SQL GROUP BY와 유사

summarise(sub_raw, Mean5y = mean(Anomaly.5y), Median5y = median(Anomaly.5y))
#5-year에 해당하는 값의 평균과 중앙값 추출

head(sub_raw)

# %>% pipeline operator, Ctrl + Shift + M

sub_raw %>% group_by(Source) %>% summarise(Mean1y = mean(Anomaly.1y), Mean5y = mean(Anomaly.5y))
sub_raw %>% gather(Anomaly, tmp, 2:4) %>% filter(Source == 2) %>% summarise(Mean = mean(tmp), SD = sd(tmp))

#join
'''
inner_join
outer_join
left_join
right_join
...

'''

mu_raw = mutate(wide_raw, Adj = Anomaly.1y / Anomaly.5y)
head(mu_raw)

rank_raw = wide_raw %>% mutate(wide_raw, Adj = Anomaly.1y / Anomaly.5y) %>%
  arrange(desc(Adj)) %>% mutate(Rank = 1:nrow(raw))
head(rank_raw)
rank_raw %>% tail()
