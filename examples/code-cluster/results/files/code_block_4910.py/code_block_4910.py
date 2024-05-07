df_phone_brands.phone_brand = df_phone_brands.phone_brand.map(str.strip).map(str.lower)
df_phone_brands.device_model = df_phone_brands.device_model.map(str.strip).map(str.lower)
df_phone_brands.device_model = df_phone_brands.phone_brand.str.cat(df_phone_brands.device_model)