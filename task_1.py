time = '1h 45m,360s,25m,30m,120s,2h 60s'
total_sec = 0
time_parts = time.split(',')
for t in time_parts:
    sub_parts = t.split()
    for part in sub_parts:
        if 's' in part:
            seconds = int(part.replace('s', ''))
            total_sec += seconds
        elif 'm' in part:
            minutes = int(part.replace('m', ''))
            total_sec += minutes * 60
        elif 'h' in part:
            hours = int(part.replace('h', ''))
            total_sec += hours * 3600
print(total_sec)