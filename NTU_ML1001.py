CNN->Convolution+Max pooling+..+Convolution+Max pooling+Flatten


Feature Map:Filter1(Neuro) Filter2(Neuro) Filter的parameter要learn
Feature Map是cube

Convolution就是一些fully connnected layer拿掉一些weight的结果

Max pooling 四个像素小方阵挑一个

Flatten -> feature map 拉直

Keras
model.add( Dense( input_dim = 28*28, units = 500, activation='relu'))


model.add( Convolution2D(25,3,3, input_shape=(1,28,28)))
                        25个3*3filter  1:black 3:rgb

                        

