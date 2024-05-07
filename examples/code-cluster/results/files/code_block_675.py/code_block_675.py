df_t=df_t.drop('Open Date',axis=1)
df_t['Type'].value_counts()
ty={'FC':0,'IL':1,'DT':2}
df_t['Type']=df_t['Type'].map(ty)
cg={'Big Cities':0,'Other':1}
df_t['City Group']=df_t['City Group'].map(cg)
x=0
c={}
for i in df_t['City'].unique():
    c.update({i:x})
    x=x+1
df_t['City']=df_t['City'].map(c)