import csv

with open('data/output.csv', 'w') as f:
    # QUOTE_ALL = 1 QUOTE_MINIMAL = 0 QUOTE_NONE = 3 QUOTE_NONNUMERIC = 2
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    for _ in range(6):
        writer.writerow(['1', '2', '3'])
