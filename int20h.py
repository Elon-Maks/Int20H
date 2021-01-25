import pandas as pd

df = pd.read_csv('data_analytics.csv')

weeks = 6
dev_proceeds = 0.7
price = 9.99

subscriptions = list(df.pivot_table(index=['Subscriber ID'], aggfunc='size'))

all_customers = len(subscriptions)
weeks_count = [all_customers]
LTV = []

for i in range(1, weeks+1):
    weeks_count.append(subscriptions.count(i))

for i in range(1, weeks+1):
    weeks_count[i] = sum(weeks_count[i:])
    LTV.append(weeks_count[i] / weeks_count[i-1])

LTV = LTV[1:]
LTV[0] = LTV[0] * dev_proceeds
for i in range(1, weeks-1):
    LTV[i] *= LTV[i-1]

LTV = sum(LTV) * price

print(LTV)
