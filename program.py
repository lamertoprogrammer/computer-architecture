import pandas as pd
from pyeda.inter import *
filename = 'file.csv'
df = pd.read_csv(filename)
list = list(map(str,df.columns[:-1]))
df.fillna('-')
df = df.sort_values(by = list)
vars = ttvars('vars', len(list))
table = truthtable(vars, df.values[:,-1])
f = espresso_tts(table)
print('Таблица истинности из файла ', filename)
print(table)
print('Логическое выражение:')
print(f[0].simplify())
