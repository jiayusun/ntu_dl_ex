#�İ�֮���keras��ʲô����

# STEP1 CREATE MODEL
#__define a set of function
model = Sequential()


model.add( Dense( input_dim = 28*28, units = 500, activation='relu'))



model.add( Dense(units = 500,activation='relu'))


model.add( Dense(units = 10, ctivation='softmax'))

# STEP2 CONFIGURE

model.compile(loss = 'categorical crossentropy',
              optimizer='adam',
              metrics =['accuracy'])

# STEP3 PICK THE BEST FUNCTION


model.fit(x_train, y_train,batch_size=100,nb_epoch=20)


# EVALUATE ��֪��ȷ�𰸣�������ȷ��
score = model.evaluate(x_test,y_test)

# PREDICT ��֪����ȷ�𰸣�ʵ��Ӧ��
result = model.predict(x_test)
