from Observer.observer.AbsObserver import AbsObserver

class CurrentKPIs(AbsObserver):
    _open_tickets = -1
    _closed_tickets = -1
    _new_tickets = -1

    def __init__(self, kpis):
        self._kpis=kpis
        kpis.attach(self)

    def update(self):
        self._open_tickets=self._kpis.open_tickets
        self ._closed_tickets=self._kpis.closed_tickets
        self._new_tickets=self._kpis.new_tickets
        self.display()

    def display(self):
        print("********* CURRENT KPIs *********")
        print(f"Current open tickets: {self._open_tickets}")
        print(f"New tickets in last hour: {self._new_tickets}")
        print(f"Tickets closed in last hour: {self._closed_tickets}")
        print("********************************\n")

    ###
    # Clean up to account for dangling references
    ###
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._kpis.detach(self)