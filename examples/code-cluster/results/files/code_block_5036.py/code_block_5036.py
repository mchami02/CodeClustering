train = pd.merge(train, sessions, how="left", left_on=["id"], right_on=["user_id"])
test = pd.merge(test, sessions, how="left", left_on=["id"], right_on=["user_id"])