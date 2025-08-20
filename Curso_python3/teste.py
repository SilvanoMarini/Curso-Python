from datetime import datetime

data = datetime.now()
data_real = data.timestamp()
data_agr = datetime.fromtimestamp(data_real)

print(data_agr)