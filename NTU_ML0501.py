#sample出79个点的likelihood最大-》u E -> p(C1|x)
->在图上画出p=0.5

共用E-》减少参数-》防overfitting

L最小时的u1，u2，此时u1=u2 p=0.5是linear的

Logistic Regression + Square error可以吗？
y=1,hx=1 微分是0
y=1,hx=0 微分也是0
所以不好

crossentropy -求和p(x)ln(q(x)) 两个Bernoulli distribution的相似性，等于0是相同

Generative model脑补

softmax-》Multi_class classification 强化最大值

1:(1,1)&(0,0)
2:(0,1)&(1,0)
不能用一条线分开

feature transform
