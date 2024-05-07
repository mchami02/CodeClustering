Y_pred = model.predict(np.array(X_val))

#####predict cat | predict dog
for i in range(0,5):
    if Y_pred[i, 0] >= 0.5: 
        print('I am {:.2%} sure this is a Dog'.format(Y_pred[i][0]))
    else: 
        print('I am {:.2%} sure this is a Cat'.format(1-Y_pred[i][0]))
        
    plt.imshow(X_val[i])    
    plt.show()