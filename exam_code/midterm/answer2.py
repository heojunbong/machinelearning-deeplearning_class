import pandas 
df=pandas.read_csv('/dshome/WoongLab/heo/midterm_homework/temperature-daejeon.csv')
df.drop(columns='지점',inplace=True)
df.rename(columns={'날짜':'date','평균기온(℃)':'average',
                   '최저기온(℃)':'lowest',
                   '최고기온(℃)':'highest'},
          inplace=True)

df['date']=pandas.to_datetime(df['date'])
df.dropna(inplace=True)

df['year']=df['date'].dt.year
july31_df=df[df['date'].dt.strftime('%m-%d')=='07-31']

from sklearn.linear_model import LinearRegression 

X=july31_df[['year','lowest','highest']].to_numpy()
y=july31_df['average'].to_numpy())

model=LinearRegression()            # 모델 생성
model.fit(X,y)

pred=model.predict([[2050,26,32]])

print(f'2050년 7월 31일의 예상 평균 온도는 섭씨 {pred[0]:.2f}도 입니다.')

