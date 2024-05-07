df_ga_full['app_lab']= df_ga_full['device_id'].map(df_events)
df_ga_full['time_most']= df_ga_full['device_id'].map(time_most)
df_ga_full['time_large']= df_ga_full['device_id'].map(time_large)
df_ga_full['time_small']= df_ga_full['device_id'].map(time_small)