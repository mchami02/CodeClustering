# using scaler
scaler = StandardScaler()
scaler.fit(scaled_feat)
scaled_feat = scaler.transform(scaled_feat)

scaled_feat = pd.DataFrame(scaled_feat, columns=cont_vars)
scaled_feat.head()