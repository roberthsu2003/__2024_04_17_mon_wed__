import pyinputplus as pyip

class BMI():
    def __init__(self, name: str, height: float, weight: float):
        super().__init__()
        self.name = name
        self.height = height
        self.weight = weight

    def __repr__(self):
        return f'\n{self.name}您好:'
    
    @property
    def bmi(self)->float:
        return self.weight / (self.height / 100) ** 2
    
    def status(self) -> str:
        if self.bmi < 18.5:
            result = '過輕'
        elif self.bmi < 24:
            result = '正常'
        elif self.bmi < 27:
            result = '過重'
        elif self.bmi < 30:
            result = '輕度肥胖'
        elif self.bmi < 35:
            result = '中度肥胖'
        else:
            result = '重度肥胖'
        return result
    
name = input('請輸入姓名: ')
height = pyip.inputFloat('請輸入身高(cm): ', min=0)
weight = pyip.inputFloat('請輸入體重(kg): ', min=0)

p1 = BMI(name, height, weight)
print(f'{p1}\n您的BMI值是: {p1.bmi:.2f}\n您的體重: {p1.status()}\n')