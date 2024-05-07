



###### look at variable importance in the model 

importances = clf.feature_importances_
indices = np.argsort(importances)[::-1]

# Print the feature ranking
print("Feature ranking:")

for f in indices:
    print(X_train.columns[f], importances[f])
    #print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

#for x in range(X_train.shape[1]):
#    print(X_train.columns[x])