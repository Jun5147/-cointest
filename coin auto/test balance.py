import pyupbit

access = "CDfWJMzCnx2b8ezfh2QPMrd89vnuxLghKIIyUYUd"
secret = "lW53Ztepqy1Wx1sibIdS37SM4t9V8xCHGwh3SxbR"
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))
amount=upbit.get_balance("KRW")
print(str(round(amount))+"원")
 