import pyinputplus as pyip

def calc_bmi(height: float, weight: float) -> float:
    return weight / (height / 100) ** 2

def get_status(bmi: float) -> str:
    if bmi < 18.5:
        result = '過輕'
    elif bmi < 24:
        result = '正常'
    elif bmi < 27:
        result = '過重'
    elif bmi < 30:
        result = '輕度肥胖'
    elif bmi < 35:
        result = '中度肥胖'
    else:
        result = '重度肥胖'
    return result

name:str = input('請輸入姓名: ')
height:float = pyip.inputFloat('請輸入身高(120~230)(cm): ', min=120, max=230)
weight:float = pyip.inputFloat('請輸入體重(40~170)(kg): ', min=40, max=170)

bmi:float = calc_bmi(height, weight)
status:str = get_status(bmi)

print(f'\n{name}, 您的BMI: {bmi:.2f}')
print(f'您的體重: {status}')