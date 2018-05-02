
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
# optimizer: 什么方式找最好model
model.compile(loss = 'categorical crossentropy',
              optimizer='adam',
              metrics =['accuracy'])

# STEP3 PICK THE BEST FUNCTION

#batch_size每次随机选一些作为一个batch，计算这个batch的total lost，Update参数
#把所有BATCH都train一遍叫一个epoch
model.fit(x_train, y_train,batch_size=100,nb_epoch=20)
