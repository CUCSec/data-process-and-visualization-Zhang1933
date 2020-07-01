import pandas as pd
import csv
import matplotlib.pyplot as plt

df=pd.DataFrame(columns=('name','MentionedTimes'))

with open('display.csv',encoding='utf-8')as csvfile:
    spamreader=csv.reader(csvfile)
    for row in spamreader:
        l=[]
        for name in row:
            l.append(name)
            tdf=df[df['name'].isin(l)]
            if not tdf.empty: 
                p=tdf.index.tolist()[0]
                df.iat[p,1]+=1
            else:
                df=df.append({'name':name,'MentionedTimes':1},ignore_index=True)
            l.clear()
df=df.sort_values(by='MentionedTimes',ascending=False,ignore_index=True)
df=df[:20]

plt.rcParams['font.sans-serif'] = ['SimHei']


df.plot.barh(x='name',y='MentionedTimes',title='知乎话题:"你会给初看美剧的人推荐哪十部美剧?"\n中被提及次数最多的前20部美剧！！',width=0.7,figsize=(18,6))

for i in range(0,20):
    plt.text(1+df.iat[i,1],i,df.iat[i,1],horizontalalignment='center',verticalalignment='center',fontsize=17,color='Red')
    plt.text(1,i,'第{}名'.format(i+1),horizontalalignment='left',verticalalignment='center',fontsize=13,)

plt.gca().invert_yaxis()


plt.show()