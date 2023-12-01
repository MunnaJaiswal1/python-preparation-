import datetime

x = datetime.datetime.now()
print(x)

import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))