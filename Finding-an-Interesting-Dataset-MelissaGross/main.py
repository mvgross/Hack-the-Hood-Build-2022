import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

ds_salaries = pandas.read_csv("ds_salaries.csv")

print(ds_salaries)