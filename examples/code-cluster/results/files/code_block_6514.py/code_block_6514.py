#DATA preporcessing

#standardizing
std_scale = preprocessing.StandardScaler().fit(train)
train_std = std_scale.transform(train)
test_std = std_scale.transform(test)


# #PCA
# pca_std = PCA(n_components=10).fit(train_std)
# train_stdwPCA = pca_std.transform(train_std)
# test_stdwPCA = pca_std.transform(test_std)

#normalize
train_normalized = preprocessing.normalize(train_std, norm='l2')
test_normalized = preprocessing.normalize(test_std, norm='l2')


