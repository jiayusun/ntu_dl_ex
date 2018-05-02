#改版之后的keras长什么样？

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


# EVALUATE 已知正确答案，评价正确率
score = model.evaluate(x_test,y_test)

# PREDICT 不知道正确答案，实际应用
result = model.predict(x_test)
