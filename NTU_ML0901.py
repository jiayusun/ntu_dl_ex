#Training不好-> Network架构不好e.g. activition不好,得换一个
# 如用sigmoid，Deeper, but worse
"""
why？ Vanishing Gradient Problem
 根据backprobagation
 sigmoid input改一下参数，影响随层衰减，output改变很小
"""
#怎么解决呢？
1. 把第一个layer pre-train
2. 改一下activiation func(ReLU _0/)

#可是这样就linear的呀？变弱了呀？ dl就是为了不linear吗？
#其实不是linear的：如果input改变大小有关

#ReLU还有变体，Leaky ReLU， Parametric ReLU

#Generalization——Maxout Network——自动学Learnable activation function
#把几个z group起来max out

自适应learning rate
Adagrad：一个给定learning rate/这个参数过去所有Gradient值的平方和再根号
即陡峭learning rate小 平坦大

有可能不convex怎么办？
RMSProp 倾向于相信新的Gradient

虽然复杂神经网络 local minimum不多 如何走出非global_minumum呢？

惯性 Movement=偏导+Momentum

Adam = RMSProp + Momentum

新一课：
如果Training data好 labeled testing data不好怎么办？
1.Early stopping testing_set loss最小就停下
2.Regularization
#norm2 每次update 参数都乘0.99（Weight Decay） 其实也是一种减少update的次数的方法
参数越大减得越大
#norm1 每次update if参数正 减一个正数 if参数负 减一个负数
与参数大小无关
3.Dropout
随机抽取要丢掉的neuron
每一次重新sample
注意：multiply （1-p)%(dropout rate) when testing
