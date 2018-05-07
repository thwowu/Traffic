# source bar plot
pd.pivot_table(data,index=["system"], values=["user_agent"], 
               aggfunc=[len]).plot(kind="barh")
               
               
# pivot table
pd.pivot_table(data,index=["system"], columns = ["page_id"], 
               values=["user_agent"], aggfunc=[len], margins=True
              ).query('system != ["coccocbot-web", "facebookexternalhit"]')



# Turning pivot table into 3 x 3 bar plots
fig = plt.figure(figsize=(12, 6))
# 4 x 5 (3 x 3)

pd_table = pd.pivot_table(data,index=["system"], 
            columns = ["page_id"], values=["user_agent"], aggfunc=[len]
           ).query('system != ["Carbon", "coccocbot-web", "facebookexternalhit"]')

for num in range(1,10):
        
    xtick = pd_table.iloc[num,].index.levels[:][2].tolist()
    name = pd_table.iloc[num,].name
    
    position = int('33'+ str(num) )
    ax = fig.add_subplot(position) 
    pd_table.iloc[num,].plot(kind=' bar', 
    title = name).set_xticklabels(xtick)
    plt.ylabel('Page ID')

plt.tight_layout()
plt.show()


fig = plt.figure(figsize=(12, 6))

for num in range(1,8):
    nu = num + 9    
    xtick = pd_table.iloc[nu,].index.levels[:][2].tolist()
    name = pd_table.iloc[nu,].name
    
    position = int('33'+ str(num) )
    ax = fig.add_subplot(position) 
    pd_table.iloc[nu,].plot(kind=' bar', title = name).set_xticklabels(xtick)
    plt.ylabel('Page ID')

plt.tight_layout()
plt.show()



















