import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AerkDfLu-eVjvAgWr6OnripVkZMRvcOkyVPJbxJEHFGXo3IpkaxwusXgeoZnzohZr3j7irjsWXO4Jxfe"
        self.client_secret = "EL1gV1g89n-POFElXlhGtL9QmKsosQgyle4cwasU6tTfd900C4o8T22usqsDBuaOTvoZNf-UdwgkQu_X"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
