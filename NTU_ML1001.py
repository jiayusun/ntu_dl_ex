CNN->Convolution+Max pooling+..+Convolution+Max pooling+Flatten


Feature Map:Filter1(Neuro) Filter2(Neuro) Filter��parameterҪlearn
Feature Map��cube

Convolution����һЩfully connnected layer�õ�һЩweight�Ľ��

Max pooling �ĸ�����С������һ��

Flatten -> feature map ��ֱ

Keras
model.add( Dense( input_dim = 28*28, units = 500, activation='relu'))


model.add( Convolution2D(25,3,3, input_shape=(1,28,28)))
                        25��3*3filter  1:black 3:rgb

                        

