class SmartPhone:
    def __init__(self, name, phNum, bat):
        #        print("__init__")
        self.name = name
        self.phoneNum = phNum
        self.battery = bat

    def call(self, phoneNum):
        if self.battery > 10:
            print(f"{self.phoneNum}에서 {phoneNum}으로 전화 겁니다.")
            self.hwCall(phoneNum)
        else:
            print("배터리가 부족해서 전화를 못겁니다.")

    def hwCall(self, phoneNum):
        print(f"3G 네트워크를 사용해서 {phoneNum}으로 전화 걸기")

    def getBatteryStatus(self):
        return self.battery

    def printVar(self):
        print(f"name: {self.name}\nphNum: {self.phoneNum}\nbattery: {self.battery}")


class FourGSmartPhone(SmartPhone):
    def __init__(self):
        super().__init__("cho", "111", 50)

    def hwCall(self, phNum):
        print(f"4G 네트워크를 사용해서 {phNum}으로 전화")

    def func(self):
        print("func()출력")


ph1 = SmartPhone("Cho", "2222-2222", 80)
ph2 = SmartPhone("Cho2", "3333-2222", 50)
ph1.call("111-1111")
ph2.call("222-2222")
ph1.printVar()
ph2.printVar()


fsp1 = FourGSmartPhone()
fsp1.func()
fsp1.call("2222-2222")