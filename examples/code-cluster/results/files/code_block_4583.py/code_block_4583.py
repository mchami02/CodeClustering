f,axes = plt.subplots(1,3,figsize = (19,7))
sb.despine(left = True)
x = 'Hour'

sb.barplot(x = x , y = 'casual' , data = file, saturation = 1, ax =  axes[0] ,)
sb.barplot(x = x , y = 'registered' , data = file, saturation = 1, ax = axes[1])
sb.barplot(x = x , y = 'count' , data = file, saturation = 1, ax = axes[2])