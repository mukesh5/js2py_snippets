import js2py
from js2py import require

res, jsfile = js2py.run_file('example.js')

print(jsfile.fibonacci_series(8))




random_int = require('random-int')

print(random_int)
print(random_int(10, 40))