df_total_sales_customers = pd.DataFrame({'Sales':  total_sales_customers['Sales'],
                                         'Customers': total_sales_customers['Customers']}, 
                                         index = total_sales_customers.index)

df_total_sales_customers = df_total_sales_customers.reset_index()
df_total_sales_customers.head()