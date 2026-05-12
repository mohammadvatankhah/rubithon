from .chain import Chain


class PrintingChain(Chain):

    def __init__(
        self,
        name: str = "printing"
    ):
        super().__init__(name)

    @Chain.initialize_handler()
    def print_ready(self, client):
        print(f"--- {client} is ready ---")

    @Chain.shutdown_handler()
    def print_stopped(self, client):
        print(f"--- {client} has stopped ---")
