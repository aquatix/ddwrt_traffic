import csv
import ddwrt_traffic

file_source = 'traffdata.bak'
file_csv_permonth = 'traffdata_monthly.csv'
file_csv_perday = 'traffdata_daily.csv'

with open(file_source) as f_src:
    content = f_src.readlines()
    result, result_per_month = ddwrt_traffic.parse_traffdata(content)
    result = ddwrt_traffic.as_flat_list(result)
    #print(result)

    with open(file_csv_permonth, 'w', newline='') as f_csv:
        writer = csv.writer(f_csv, delimiter=';', quoting=csv.QUOTE_NONE)
        writer.writerow(['month', 'download', 'upload'])
        writer.writerows(result_per_month)

    with open(file_csv_perday, 'w', newline='') as f_csv:
        writer = csv.writer(f_csv, delimiter=';', quoting=csv.QUOTE_NONE)
        writer.writerow(['date', 'download', 'upload'])
        writer.writerows(result)
