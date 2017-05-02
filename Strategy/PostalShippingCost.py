from Strategy.AbsShippingCostStrategy import AbsShippingCostStrategy

class PostalShippingCost(metaclass=AbsShippingCostStrategy):

    def calculate(self, order):
        return order.weight * .10