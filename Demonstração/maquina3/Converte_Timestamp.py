import datetime
# 01 dia => 86400 s
# 01 ano => 31356000 s
# 42 anos => 42 * 31356000 s

ajusteTempo = 42 * 31536000 + 200*86400

i = 10753295594424116
f  = 14879639146403495

fator = 1e12

ti = i - i
tf = f - i
print(tf)
print(ti/fator + ajusteTempo)

dateti = datetime.datetime.fromtimestamp(ti/fator + ajusteTempo)
datetf = datetime.datetime.fromtimestamp(tf/fator + ajusteTempo)

print("ti = ",dateti)
print("tf = ",datetf)
