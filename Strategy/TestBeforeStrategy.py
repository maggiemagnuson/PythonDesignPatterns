from Strategy.Order import Order
from Strategy.PostalShippingCost import PostalShippingCost
from Strategy.ShippingCost import ShippingCost
from Strategy.UpsShippingCost import UpsShippingCost

from Strategy.FedExShippingCost import FedExShippingCost

if __name__ == '__main__':
    order = Order()
    order.weight = 10
    cost_calculator = ShippingCost(FedExShippingCost())
    cost = cost_calculator.shipping_cost(order)
    print(cost)
    assert cost == 2.0

    order = Order()
    order.weight = 10
    cost_calculator = ShippingCost(UpsShippingCost())
    cost = cost_calculator.shipping_cost(order)
    print(cost)
    assert cost == 3.0

    order = Order()
    order.weight = 10
    cost_calculator = ShippingCost(PostalShippingCost())
    cost = cost_calculator.shipping_cost(order)
    print(cost)
    assert cost == 1.0

    print("===========================")
    print(" Passed ALL tests          ")
    print("===========================")