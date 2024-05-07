history = model.fit(train_df.values, y_value.values, nb_epoch=30, batch_size = 64, verbose=1)
predict = model.predict(test_df.values)