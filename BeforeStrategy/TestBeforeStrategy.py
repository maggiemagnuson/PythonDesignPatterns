from BeforeStrategy.Order import Order
from BeforeStrategy.Shipper import Shipper
from BeforeStrategy.ShippingCost import ShippingCost

if __name__ == '__main__':
    order = Order(Shipper.FEDEX)
    cost_calculator = ShippingCost()
    cost = cost_calculator.shipping_cost(order)
    assert cost == 3.0

    order = Order(Shipper.UPS)
    cost_calculator = ShippingCost()
    cost = cost_calculator.shipping_cost(order)
    assert cost == 4.0

    order = Order(Shipper.POSTAL)
    cost_calculator = ShippingCost()
    cost = cost_calculator.shipping_cost(order)
    assert cost == 5.0

    print("Tests Passed")