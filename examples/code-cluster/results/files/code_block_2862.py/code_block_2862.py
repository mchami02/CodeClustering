

print("Train Dataset Graphical Representation of Counrtry Region w.r.t. Fatalities")
plt.figure(figsize=(20,10))
sns.barplot(x='Fatalities',y='Country_Region',data=show_cumulatively[show_cumulatively['Fatalities'] != 0].sort_values(by='Fatalities',ascending=False).head(50))'