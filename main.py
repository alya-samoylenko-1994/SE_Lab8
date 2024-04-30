import csv

ticket_prices = {1: 0, 2: 0, 3: 0}

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        p_class = int(row[2])
        fare = float(row[9])
        ticket_prices[p_class] += fare

for p_class, total_price in ticket_prices.items():
    print(f"Суммарная стоимость билетов для класса {p_class}: {total_price}")
