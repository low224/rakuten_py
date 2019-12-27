# Utility to calculate Rakuten Trade fees
from math import ceil

print('Please input total share number to purchase ')
share_no = int(input())

print('Please input purchse price')
market_price = float(input())

print('Stamp Duty exemption? y / n')
market_exempt = True if input() == 'y' else False

total_price = share_no * market_price

# Calculate broker_fee
if total_price  < 1000:
	broker_fee = 7
elif total_price >= 1000 and total_price <= 9999.99:
	broker_fee = 8
elif total_price >= 10000 and total_price <= 99999.99:
	broker_fee = total_price * 0.001
else:
	broker_fee = 100

# Calulate clearing fee
clearing_fee = float(min(total_price * 0.0003, 1000))

# Calculate stamp duty
if market_exempt is True:
	stamp_duty = 0
else:
	stamp_duty = ceil(total_price / 1000)
	stamp_duty = min(200, stamp_duty)

# Calculate sst
sst = broker_fee * 0.06

total_cost = clearing_fee + stamp_duty + broker_fee + sst
total_fee = total_price + clearing_fee + stamp_duty + broker_fee + sst

print('The total broker fee is %.2f' % broker_fee)
print('The total clearing fee is %.2f' % clearing_fee)
print('The total stamp duty is %.2f' % stamp_duty)
print('The total SST is %.2f' % sst)
print('The total transaction cost is %.2f' % total_cost)
print('The total fee is : %.2f' % total_fee)
