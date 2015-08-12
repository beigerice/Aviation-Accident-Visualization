import re
input_file = open('AviationData.txt','rU')
result = {}

for line in input_file:
    items = line.rstrip('\n').split('|')
    if items[0] == 'Event Id ':
        continue
    if items[5] == ' United States ' and items[23] != '  ':
        month = re.findall(r'[^/]([0-9]{2})/', items[3])
        year = re.findall(r'/([0-9]{4})', items[3])
        name = month[0]+'/'+year[0]
        result[name] = result.get(name,0)+int(items[23])

result = sorted(result.iteritems(), key=lambda d:(d[0].split('/')[1],d[0].split('/')[0])) 

output_file = open('time_series.txt', 'w')
for name,count in result:
    output_file.write('[')
    output_file.write("'"+name+"', "+str(count))
    output_file.write('], ')
output_file.close()
