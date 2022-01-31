class Atm():
    def __init__(self,cardNo,pin) :
        self.cardNo = cardNo
        self.pin = pin
        
    def cashWithdrawl(self):
        print("cash has been whithdrawn from", self.cardNo)
        
Atm_1 = Atm(123456,789)
Atm_1.cashWithdrawl()
Atm_2 = Atm(7890123,123)
Atm_2.cashWithdrawl()