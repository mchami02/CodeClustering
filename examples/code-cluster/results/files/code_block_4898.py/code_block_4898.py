# df_gender_age_train.device_id[]
in_train_events = df_events[df_events.device_id.isin(set(df_gender_age_train.device_id) & set(df_events.device_id))]
in_train_app_events = df_app_events[df_app_events.event_id.isin(in_train_events.event_id)]
in_train_app_events.event_id.nunique(), in_train_app_events.event_id.size, len(in_train_events)