#p(H|D)，在D的条件下H发生的概率

#先验概率PH
#似然度p(D|H)
#p(H)p(D|H)
#后验概率p(H|D)

#p(A|B) = p(A)p(B|A) / p(B)

from thinkbayes import Pmf

pmf = Pmf()

for x in [1,2,3,4,5,6]:
    pmf.Set(x, 1/6.0)

print(pmf)
