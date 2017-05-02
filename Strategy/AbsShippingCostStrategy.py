from abc import ABCMeta, abstractmethod

class AbsShippingCostStrategy(ABCMeta):

    @abstractmethod
    def calculate(self, order):
        """Calculate Shipping Cost Required"""