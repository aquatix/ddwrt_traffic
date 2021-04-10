def formatline(traffline):
    """
    Parse line of format:
    traff-<mm>-<yyyy>=<download_day1>:<upload_day1> <download_day2>:<upload_day2> ... <download_dayN>:<upload_dayN> [<download_month>:<upload_month>]
    """
    line_data = traffline.strip().split('=')
    line_result = []
    day_counter = 0
    #print(line_data[0])
    # line_data[0] is the month, of format traff-01-2009 (mm-yyyy)
    traff, month, year = line_data[0].split('-')
    days = line_data[1].split()
    # last tuple is the month total, parse:
    month_down, month_up = days.pop(-1)[1:-1].split(':')
    for day_data in days:
        day_counter += 1
        day = "{0:0{1}d}".format(day_counter, 2)
        down, up = day_data.split(':')
        line_result.append(['{0}-{1}-{2}'.format(year, month, day), down, up])
    return '{0}-{1}'.format(year, month), month_down, month_up, line_result


def parse_traffdata(content):
    """
    Parse the lines from a dd-wrt WAN traffic overview export
    """
    result = []
    result_per_month = []
    for traffline in content:
        if traffline.strip() == 'TRAFF-DATA' or traffline.strip() == "ÿ":
            continue
        month, month_down, month_up, line_result = formatline(traffline)
        result.append(line_result)
        result_per_month.append([month, month_down, month_up])
    return result, sorted(result_per_month, key=lambda month: month[0])


def as_flat_list(all_days):
    """
    Flatten the hierarchical list result from the per-month grouped daily data to a flat list
    """
    result = []
    for month in all_days:
        result.extend(month)
    return sorted(result, key=lambda day: day[0])
