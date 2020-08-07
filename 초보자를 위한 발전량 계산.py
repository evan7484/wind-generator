"""
1000Wh = 1kWh
1000kWh = 1MWh
Wh = 1시간 동안 하는 일의 양
1Wh = 3600s * 1W = 1J/s * 3600s = 3600J

"""

print("본 프로그램은 풍력발전기의 발전량을 구하기 위한 프로그램입니다. \n")
print(" Output Power (kWh) =(날개의 회전면적) x(날개의 힘) x(효율)x(풍력발전기의의 개수)x(날개 회전시간) \n")
print("를 통해 풍력발전기의 발전량을 구할 수 있습니다. \n")

print("이를 위해서 날개의 반지름, 풍속, 발전효율, 발전기의 개수, 하루동안 바람이 분 시간을 알아야 합니다. \n" )

print("풍력발전기는 표준 모델로 정하겠습니다 : '1'")
print("풍력발전기는 제가 직접  정하겠습니다 : '2'")

Q = input("1 또는 2를 선택해주세요 : ")


if Q == '1':
    print("a")

    print("발전기의 종류가 어떻게 되나요?")
    print("1 : 가정용 발전기 [날개의 반지름 0.12m, 출력값 0.4kW]")
    print("2 : 중형 발전기 [날개의 반지름 28m, 출력값 750kW]")
    print("3 : 대형 발전기 [날개의 반지름 45m, 출력값 2MW]")
    print("\n ==위의 값은 모두 발전효율 30%로 고정됩니다.==")

    Z = input("\n 1, 2, 3 중 하나를 선택해 주세요 : ")

    if Z == '1':

        print("\n ----가정용(소형) 발전기를 선택하였습니다.----")
        r=float(0.12)
        X=float(input("평균 풍속(m/s) : "))
        E=float(30)
        n=float(input("풍력발전기의 갯수(개) : "))
        h=float(input("하루동안 4m/s 이상의 바람이 분 시간(hr/일) : "))


        SweptArea = 3.14*r*r
        PowerDensity = (1/2*1.25)*1.92*X*X*X/1000*1/1000

        print("\n \a 풍력발전기" + str(n) + "개가 1년동안 발전한  평균 발전량은")
        print("\n" + str(SweptArea * PowerDensity * E/100.0*n*h*12*30) + "MW")
        print("\n 입니다.")

    if Z == '2':
        print("\n ----중형 발전기를 선택하였습니다.----")
        r= float(28)
        X=float(input("평균 풍속(m/s) : "))
        E=float(30)
        n=float(input("풍력발전기의 갯수(개) : "))
        h=float(input("하루동안 4m/s 이상의 바람이 분 시간(hr/일) : "))


        SweptArea = 3.14*r*r
        PowerDensity = (1/2*1.25)*1.92*X*X*X/1000*1/1000

        print("\n \a 풍력발전기" + str(n) + "개가 1년동안 발전한  평균 발전량은")
        print("\n" + str(SweptArea * PowerDensity * E/100.0*n*h*12*30) + "MW")
        print("\n 입니다.")


    if Z == '3':
        
        print("\n ----대형 발전기를 선택하였습니다.----")
        r= float(45)
        X=float(input("평균 풍속(m/s) : "))
        E= float(30)
        n=float(input("풍력발전기의 갯수(개) : "))
        h=float(input("하루동안 4m/s 이상의 바람이 분 시간(hr/일) : "))


        SweptArea = 3.14*r*r
        PowerDensity = (1/2*1.25)*1.92*X*X*X/1000*1/1000

        print("\n \a 풍력발전기" + str(n) + "개가 1년동안 발전한  평균 발전량은")
        print("\n" + str(SweptArea * PowerDensity * E/100.0*n*h*12*30) + "MW")
        print("\n 입니다.")

    else:
        print("1, 2, 3 중 하나를 선택해 주세요.")
        sys.exit()

   
if Q == '2':


    print("\n --------------------사용자 지정 모드--------------------")
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
    



else:
     print("1 또는 2를 써주세요.")
