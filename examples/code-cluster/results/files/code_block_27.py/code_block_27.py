x_list = [X_train, X_valid]
y_list = [y_train, y_valid]

scoring = list(map(lambda x,y: round(model.score(x,y)*100, 2), x_list, y_list)) 
scoring