#Training����-> Network�ܹ�����e.g. activition����,�û�һ��
# ����sigmoid��Deeper, but worse
"""
why�� Vanishing Gradient Problem
 ����backprobagation
 sigmoid input��һ�²�����Ӱ�����˥����output�ı��С
"""
#��ô����أ�
1. �ѵ�һ��layer pre-train
2. ��һ��activiation func(ReLU _0/)

#����������linear��ѽ��������ѽ�� dl����Ϊ�˲�linear��
#��ʵ����linear�ģ����input�ı��С�й�

#ReLU���б��壬Leaky ReLU�� Parametric ReLU

#Generalization����Maxout Network�����Զ�ѧLearnable activation function
#�Ѽ���z group����max out

����Ӧlearning rate
Adagrad��һ������learning rate/���������ȥ����Gradientֵ��ƽ�����ٸ���
������learning rateС ƽ̹��

�п��ܲ�convex��ô�죿
RMSProp �����������µ�Gradient

��Ȼ���������� local minimum���� ����߳���global_minumum�أ�

���� Movement=ƫ��+Momentum

Adam = RMSProp + Momentum

��һ�Σ�
���Training data�� labeled testing data������ô�죿
1.Early stopping testing_set loss��С��ͣ��
2.Regularization
#norm2 ÿ��update ��������0.99��Weight Decay�� ��ʵҲ��һ�ּ���update�Ĵ����ķ���
����Խ�����Խ��
#norm1 ÿ��update if������ ��һ������ if������ ��һ������
�������С�޹�
3.Dropout
�����ȡҪ������neuron
ÿһ������sample
ע�⣺multiply ��1-p)%(dropout rate) when testing
