class SmartPhone:
    def __init__(self, name, phoneNum, battery):
        self.owner = name
        self.number = phoneNum
        self.battery = battery

    def call(self, phoneNum):
        if self.battery >= 10:
            print(f"{self.number}에서{phoneNum}으로 전화를 겁니다.")
            hwcall(phoneNum) ##
    def getBatteryStatus(self):
        return self.battery
    def _hwself ## 