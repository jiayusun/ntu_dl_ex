
(x_train, y_train),(x_test,y_test)=load_data()

model = Sequential()


model.add( Dense( input_dim = 28*28, units = 633, activation='relu'))

model.add( Dense(units = 633,activation='relu'))
model.add( Dense(units = 633,activation='relu'))

model.add( Dense(units = 10, ctivation='softmax'))

# STEP2 CONFIGURE

model.compile(loss = 'mse',
              optimizer=SGD(lr=0.1),
              metrics =['accuracy'])

# STEP3 PICK THE BEST FUNCTION


model.fit(x_train, y_train,batch_size=100,nb_epoch=20)


# EVALUATE 已知正确答案，评价正确率
score = model.evaluate(x_test,y_test)

# PREDICT 不知道正确答案，实际应用
result = model.predict(x_test)

print'\nTest Acc:',result[1]

#结果很不好，why？欲知后事，请听下回分解
