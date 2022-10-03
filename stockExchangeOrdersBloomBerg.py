"""
You are given a list of stock exchange along with startTime and endTime in which these exchanges operate.
0 <= startTime, endTime <= 23

[
	['Exchange A', 2, 7], 
	['Exchange C', 11, 17], 
	['Exchange B', 9, 16],
	['Exchange D',14, 20]
]
Then, given a list of buy/sell orders which need to be executed in the given timeframe you need to find out what all orders can be served with atleast 1 exchange.

[
	['Order 1', '3', '6'],
	['Order 2', '9', '12'],
	['Order 3', '21', '22']
]
So in this case Order 1 and 2 can be served but 3 cannot be served by any exchange.
"""
def stockExchangeOrders(exchanges, orders):
    exchanges_times = []
    for exchange in exchanges:
        exchanges_times.append([exchange[1],exchange[2]])
    exchanges_times.sort()
    print(exchanges_times)
    merged_times = []
    for time in exchanges_times:
        if not merged_times or merged_times[-1][1] < time[0]:
            merged_times.append(time)
        elif merged_times[-1][1] > time[0]:
            merged_times[-1][1] = max(time[1], merged_times[-1][1])

    print(merged_times)
    processed_orders = []
    for order in orders:
        if order[1] <= exchanges_times[0][0] or order[1] > exchanges_times[-1][1]:
            continue
        else:
            for time in merged_times:
                if order[1] >= time[0] and order[2] <= time[1]:
                    processed_orders.append(order[0])
                    break
    print(processed_orders)

def stockExchangeOrders1(exchanges, orders):
    availability = [0]* 24
    for exchange in exchanges:
        if exchange[1] < exchange[2]:
            for i in range(exchange[1],exchange[2]+1):
                if not availability[i]:
                    availability[i] =1
        
        else:
            for i in range(exchange[1],24):
                if not availability[i]:
                    availability[i] =1

            for i in range(0,exchange[2]+1):
                if not availability[i]:
                    availability[i] =1
    processed_orders = []
    processFlag = 1
    print(availability)
    for order in orders:
        if order[1] < order[2]:
            for i in range(order[1],order[2]+1):
                if not availability[i]:
                    processFlag = 0
                    break
        
        else:
            for i in range(order[1],24):
                if not availability[i]:
                    processFlag = 0
                    break

            for i in range(0,order[2]+1):
                if not availability[i]:
                    processFlag = 0
                    break
        if processFlag:
            processed_orders.append(order[0])
        processFlag = 1
    
    return processed_orders

def stockExchangeOrdersNightOrders(exchanges, orders):
    exchanges_times = []
    for i ,exchange in enumerate(exchanges):
        if exchange[1] > exchange[2]:
            exchanges_times.append([exchange[1],23])
            exchanges_times.append([0,exchange[2]])
        else:
            exchanges_times.append([exchange[1],exchange[2]])

    exchanges_times.sort()
    print(exchanges_times)
    merged_times = []
    for time in exchanges_times:
        if not merged_times or merged_times[-1][1] < time[0]:
            merged_times.append(time)
        elif merged_times[-1][1] > time[0]:
            merged_times[-1][1] = max(time[1], merged_times[-1][1])

    print(merged_times)
    processed_orders = []
    for order in orders:
        if order[1] <= exchanges_times[0][0] or order[1] > exchanges_times[-1][1]:
            continue
        else:
            for time in merged_times:
                if order[1] >= time[0] and order[2] <= time[1]:
                    processed_orders.append(order[0])
                    break
    print(processed_orders)
exchanges =[
	['Exchange A', 2, 7], 
	['Exchange C', 11, 17], 
	['Exchange B', 9, 16],
	['Exchange D',14, 20],
    ['Exchange E',23, 4]]
orders =[
	['Order 1', 3, 6],
	['Order 2', 9, 12],
	['Order 3', 21, 22],
    ['Order 4', 23, 2]
]
print(stockExchangeOrders1  (exchanges,orders))
