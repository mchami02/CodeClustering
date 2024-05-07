def ToWeight(y):
    w = np.zeros(y.shape, dtype=float)
    ind = y != 0
    w[ind] = 1./(y[ind]**2)
    return w

def rmspe(y, yhat):
    w = ToWeight(y)
    rmspe = np.sqrt(np.mean( w * (y - yhat)**2 ))
    return rmspe

y_test_inv=np.exp(y_test)-1
y_pred_inv=np.exp(y_pred)-1
rmse_test = np.sqrt(mean_squared_error(y_test_inv,y_pred_inv))
rmspe_test = rmspe(y_test_inv,y_pred_inv)
print(rmse_test,rmspe_test)