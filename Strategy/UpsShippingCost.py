from Strategy.AbsShippingCostStrategy import AbsShippingCostStrategy

class UpsShippingCost(metaclass=AbsShippingCostStrategy):

    def calculate(self, order):
        return order.weight * .30