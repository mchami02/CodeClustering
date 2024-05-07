# Save predictions in format used for competition scoring
output = pd.DataFrame({'ForecastId': test_df.ForecastId, 'ConfirmedCases': rnd_y1_pred, 'Fatalities': rnd_y2_pred})
output.to_csv('submission.csv', index=False)
print(output.tail(10))
print('Submission file successfully saved..')