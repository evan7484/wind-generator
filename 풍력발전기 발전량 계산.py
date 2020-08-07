"""
1000Wh = 1kWh
1000kWh = 1MWh
Wh = 1시간 동안 하는 일의 양
1Wh = 3600s * 1W = 1J/s * 3600s = 3600J

"""
print("본 프로그램은 풍력발전기의 발전량을 구하기 위한 프로그램입니다. \n")
print(" Output Power (kWh) =(날개의 회전면적) x(날개의 힘) x(효율)x(풍력발전기의의 개수)x(날개 회전시간) \n")
print("를 통해 풍력발전기의 발전량을 구할 수 있습니다. \n")

print("이를 위해서 날개의 반지름, 풍속, 발전효율, 발전기의 개수, 하루동안 바람이 분 시간을 알아야 합니다. \n")



r=float(input("날개의 반지름(m) : "))
X=float(input("평균 풍속(m/s) : "))
E=float(input("풍력발전기의 발전효율(%) : "))
n=float(input("풍력발전기의 갯수(개) : "))
h=float(input("하루동안 4m/s 이상의 바람이 분 시간(hr/일) : "))


SweptArea = 3.14*r*r
PowerDensity = (1/2*1.25)*1.92*X*X*X/1000*1/1000

print("\n \a 풍력발전기" + str(n) + "개가 1년동안 발전한  평균 발전량은")
print("\n" + str(SweptArea * PowerDensity * E/100.0*n*h*12*30) + "MW")
print("\n 입니다.")


