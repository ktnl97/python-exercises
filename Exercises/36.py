import json
from collections import Counter
from bokeh.plotting import figure, output_file, show
from datetime import datetime

def get_month_count():
    birthday_dict = dict()
    with open("birthdays.json") as input_file:
        birthday_dict = json.load(input_file)
    months = [(datetime.strptime(date, '%d/%m/%Y')).strftime('%m') for date in birthday_dict.values()]
    return Counter(months)

month_counter = sorted(get_month_count().items())
months = []
no_of_birthdays = []

for key, value in month_counter:
    months.append((datetime.strptime(key, '%m')).strftime('%B'))
    no_of_birthdays.append(value)

output_file("density_by_month.html")

plot = figure(title="Plot indicating your friend's birthday density against month", x_range = months, x_axis_label='Months', y_axis_label='No. of birthdays', plot_width= 1000)

plot.line(months, no_of_birthdays, legend_label="Birthday density", line_width=2)

show(plot)