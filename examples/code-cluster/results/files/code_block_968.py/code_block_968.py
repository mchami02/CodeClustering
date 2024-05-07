px.choropleth(df_map, 
              locations="iso_alpha", 
              color="ln(ConfirmedCases)", 
              hover_name="Country_Region", 
              hover_data=["ConfirmedCases"] ,
              animation_frame="Date",
              color_continuous_scale=px.colors.sequential.dense, 
              title='Daily Confirmed Cases growth(Logarithmic Scale)')'