from Strategy.AbsShippingCostStrategy import AbsShippingCostStrategy

class FedExShippingCost(metaclass=AbsShippingCostStrategy):

    def calculate(self, order):
        return order.weight * .20
