def formatline(traffline):
    line_data = traffline.strip().split('=')
    line_result = []
    day_counter = 0
    # line_data[0] is the month, of format traff-01-2009 (mm-yyyy)
    traff, month, year = line_data[0].split('-')
    days = line_data[1].split()
    # last tuple is the month total, parse:
    month_down, month_up = days.pop(-1)[1:-1].split(':')
    for day_data in days:
        day_counter += 1
        day = "{0:0{1}d}".format(day_counter, 2)
        down, up = day_data.split(':')
        #line_result.append('{0}-{1}-{2} {3} {4}'.format(year, month, day, down, up))
        line_result.append(['{0}-{1}-{2}'.format(year, month, day), down, up])
    return '{0}-{1}'.format(year, month), month_down, month_up, line_result


def parse_traffdata(content):
    result = []
    result_per_month = []
    for traffline in content:
        if traffline.strip() == 'TRAFF-DATA':
            continue
        month, month_down, month_up, line_result = formatline(traffline)
        result.append(line_result)
        result_per_month.append([month, month_down, month_up])
    return result, result_per_month


filename = 'traffdata.bak'
with open(filename) as f:
    content = f.readlines()
    result, result_per_month = parse_traffdata(content)
    print(result)
    print(result_per_month)
