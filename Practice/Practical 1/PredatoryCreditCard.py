from CreditCard import Credit_Card


class PredatoryCreditCard(Credit_Card):

    def __init__(self, customer, bank, acc, limit, apr):
        super().__init__(customer, bank, acc, limit)
        self._apr = apr
        self._chargeCount = 0

    def charge(self, price):
        success = super().charge(price)

        self._chargeCount += 1
        if self._chargeCount > 10:
            self._balance += 1

        if not success:
            self._balance += 5
        return success

    def process_month(self):
        self._chargeCount = 0

        if self.get_balance() > 0:
            interest = pow((1+self._apr), 1/12)
            self._balance += interest