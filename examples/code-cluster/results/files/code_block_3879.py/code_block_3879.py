test['count'] = np.exp(pd.DataFrame(preds).mean())-1
test[['datetime','count']].to_csv('rf4.csv', index=False)
