# Utility to calculate Rakuten Trade fees

print('Please input total share number to purchase ')
share_no = int(input())

print('Please input purchse price')
market_price = float(input())

print('Stamp Duty exemption? Y ? N')
market_exempt = True if input() == 'Y' else False

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
clearing_fee = min(total_price * 0.003, 1000)

# Calculate stamp duty
if market_exempt is False:
	stamp_duty = 0
else:
	stamp_duty = max(1, int(total_price / 1000))
	stamp_duty = min(200, stamp_duty)

total_fee = total_price + clearing_fee + stamp_duty

print('The total fee is : %.2f' % total_fee)
