
# STEP1 CREATE MODEL
#__define a set of function
model = Sequential()

#Dense: Fully connected layer
model.add( Dense( input_dim = 28*28, output_dim = 500))
model.add( Activation('sigmoid'))

# no need to input the number of layer
model.add( Dense(output_dim = 500))
model.add( Activation('sigmoid'))

model.add( Dense(output_dim = 10))
model.add( Activation('softmax'))

# STEP2 GOODNESS OF FUNCTION
# In this case, crossentropy is used as LOSS FUNCTION
# optimizer: ʲô��ʽ�����model
model.compile(loss = 'categorical crossentropy',
              optimizer='adam',
              metrics =['accuracy'])

# STEP3 PICK THE BEST FUNCTION

#batch_sizeÿ�����ѡһЩ��Ϊһ��batch���������batch��total lost��Update����
#������BATCH��trainһ���һ��epoch
model.fit(x_train, y_train,batch_size=100,nb_epoch=20)
