import pyupbit
import numpy as np

#ohlcv(당일 시가, 고가 ,저가, 종가, 거래량)
df = pyupbit.get_ohlcv("KRW-BTC",count=7)

# 변동성 돌차 기준 범위 계산, (고가-저가)*k값 / k는 변동폭
df['range'] = (df['high'] - df['low']) * 0.5

# target(매수가), range 칼럼을 한칸씩 밑으로 내림
df['target'] = df['open'] + df['range'].shift(1)

#수수료
fee = 0.0032

# np.where(조건문, 참값, 거짓값)
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'] - fee,
                     1)

#누적 곱 계산(coumprod) => 누적 수익률
df['hpr'] = df['ror'].cumprod()

#Draw Down 계산(누적 최대 값과 현재 hpr 차이/ 누적 최대값 *100)
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

#MDD 계산(일정 기간 고점대비 주가하락)
print("MDD(%): ", df['dd'].max())

print(df)
#range(변동폭*k), target(매수가), ror(수익률), hpr(누적수익률), 