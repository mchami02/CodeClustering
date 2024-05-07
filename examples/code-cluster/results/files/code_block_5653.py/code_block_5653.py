data_dict['MNCAATourneyCompactResults'].groupby(['Season'])['WScore'].mean().plot(kind='line');
plt.title('Mean scores of winning teams by season in tourneys');