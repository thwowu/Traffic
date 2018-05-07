# Slicing the data 
data_8001 = data[data['page_id']== 8001] 
data_8001['count'] = 1

pd.pivot_table(data_8001,index=["device"], 
               values=["user_agent"], aggfunc=[len]
              ).plot(kind="barh")


# return the position of a specific string in a list
def find(line, word):
    try:
        k = [ i for i,x in enumerate(line) if x == word]

    except:
        print(sys.exc_info()[0],"occured.")
        print(word)
        print(line)
    if len(k) is 0:
        return True
    else:
        return k[0]
    
# to be used in lamda to return the value by the key <- input(word)   
def query(dat, word):
    data_8001[word] = data_8001['trait'].apply(lambda x: x[1 + find(x, word)])

# keyword tag in track url 
attribute = ['arrival', 'departure', 'path', 'room_type', 'cpt', 'clTi', 'mode']

# insert new attributes
for i in attribute:
    query(data_8001, i)

# calculate the search travel length and 
# Calculate the difference between "search" and "arrival time"

L1 = []
L2 = []

for nc in data_8001.index:
    t1 = parse(data_8001['arrival'][nc])
    t2 = parse(data_8001['departure'][nc])
    t3 = data_8001['time'][nc]
    diff1 = t2 - t1
    diff2 = t1 - t3
    L1.append(diff1.days)
    L2.append(diff2.days) 

data_8001['travel_length'] = L1
data_8001['Depart_diff'] = L2
