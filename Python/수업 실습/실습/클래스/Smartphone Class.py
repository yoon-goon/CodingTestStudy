class SmartPhone:
    def __init__(self, name, phoneNum, battery):
        self.owner = name
        self.number = phoneNum
        self.battery = battery

    def call(self, phoneNum):
        if self.battery >= 10:
            print(f"{self.number}에서{phoneNum}으로 전화를 겁니다.")
            self._hwcall(phoneNum) ##
    def getBatteryStatus(self):
        return self.battery
    def _hwcall(self,phoneNum):
        print(f"하드웨어를 제어하여 {phoneNum}으로 전화겁니다.")

ph1 = SmartPhone("Yoo","010-2222-4444", 80)
ph1.call("010-4252-2422")
print(ph1.getBatteryStatus())