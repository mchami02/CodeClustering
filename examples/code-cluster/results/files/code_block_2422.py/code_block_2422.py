y_test_inv=np.exp(y_test)-1
y_pred_inv=np.exp(y_pred)-1
print('RMSE',np.sqrt(mean_squared_error(y_test_inv,y_pred_inv)))
print('Accuracy',r2_score(y_test_inv,y_pred_inv))