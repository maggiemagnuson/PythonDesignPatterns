from Observer.observer.KPIs import KPIs
from Observer.observer.CurrentKPIs import CurrentKPIs
from Observer.observer.ForecastKPIs import ForecastKPIs

###
# The with block is needed in order to take
# advantage of the Python Context Manager
###
with KPIs() as kpis:
    with CurrentKPIs(kpis), ForecastKPIs(kpis):
        kpis.set_kpis(25, 10, 5)
        kpis.set_kpis(100, 50, 30)
        kpis.set_kpis(50, 10, 20)

print("\n *** Exited context managers. ***\n")
kpis.set_kpis(150,110,120)