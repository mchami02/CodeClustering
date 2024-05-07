X_test=test.iloc[:,1:].values
m_test=X_test.shape[0]
one=np.ones((m_test,1))
X_test=np.hstack((X_test,one))