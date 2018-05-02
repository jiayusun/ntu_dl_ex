#Hinge Loss + Kernel Method-> SVM

#Hinge Loss?
"""
Binary Classification
LOSS代表在training data上犯了几次错误,是离散的，求不了微分
换一个非离散的LOSS function
"""

#e.g. Square Loss:
"""
if y^n=1, f(x)->1
if y^n=-1, f(x)->-1
公式形式(yf-1)^2 不合理 yf很大 loss也很大
"""
#e.g. Sigmoid+Square Loss: 没有回报 不想努力


#e.g. Sigmoid+ Cross entropy:努力可以 有回报

#e.g. Hinge Loss\_ _/
#得到正确答案还不够好 要好过一段距离 这段距离是Margin
#HL只要大于1就及格，及格就好，不要做得更好
