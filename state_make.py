import re
input_file = open('AviationData.txt','rU')
result = {}
state_dic = {}

for line in input_file:
    items = line.rstrip('\n').split('|')
    if items[0] == 'Event Id ':
        continue    
    if items[5] == ' United States ' and items[23] != '  ':
        items[14] = items[14].strip()
        state = re.findall(r'\,\s([A-Z]{2})\s', items[4])
        if len(state) != 0:
            state_dic[state[0]] = state_dic.get(state[0],0)+int(items[23])
            if items[14].upper() not in result:
                result[items[14].upper()] = {}
                result[items[14].upper()]['count'] = 0
            result[items[14].upper()]['count'] += int(items[23])
            result[items[14].upper()][state[0]] = result[items[14].upper()].get(state[0],0)+int(items[23])

for state,count in state_dic.items():
    if count < 100:
        state_dic.pop(state,None)
        
state_dic = sorted(state_dic.iteritems(),key=lambda d:d[1],reverse=True)

categories = open('stacked_bar_categories.txt', 'w')
for state,dic in state_dic:
    categories.write("'"+state+"', ")
categories.close()
        
for make,dic in result.items():
    if dic['count'] < 100:
        result.pop(make,None)

result = sorted(result.iteritems(),key=lambda d:d[1]['count'],reverse=True)

series = open('stacked_bar_series.txt', 'w')
for make,dic in result:
    series.write('{')
    series.write("name: '"+make+"',")
    series.write('\n')
    series.write('data: [')
    for state,count in state_dic:
        if state in dic:
            series.write(str(dic[state])+', ')
        else:
            series.write(str(0)+', ')
    series.write(']')
    series.write('}, ')
series.close()




