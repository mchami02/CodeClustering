# Promo

# Plot average sales & customers with/without promo
fig, (axis1,axis2) = plt.subplots(1,2,figsize=(15,4))

sns.barplot(x='Promo', y='Sales', data=rossmann_df, ax=axis1)
sns.barplot(x='Promo', y='Customers', data=rossmann_df, ax=axis2)