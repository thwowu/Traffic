# Room Type
data_8001.pivot_table('count', index=['room_type'], 
                      columns='device', aggfunc='sum').plot(kind ='bar')


# the difference between "search" and "arrival time"
data_8001.pivot_table('count', index=['Depart_diff'], 
                      columns='device', aggfunc='sum'
                     ).plot(kind ='bar', stacked=True)
                   
# Prefered Stay Length
data_8001.pivot_table('count', index=['travel_length'], 
                      columns='device', aggfunc='sum'
                     ).plot(kind ='bar', stacked=True)
