from django.test import TestCase, Client

from tool.models import Tool
from user.models import User


# Create your tests here.
class ToolsTestCase(TestCase):
    def setUp(self) -> None:
        user = User(email="test@example.com", password="test")
        user.save()
        self.tool = Tool(name="gražtas", description="geros būklės, mažai naudotas", rent_price=15, user=user)
        self.tool.save()

    def test_get_all_tools(self):
        client = Client()
        response = client.get("/tools/")
        self.assertIn(b"Tools list", response.content)
        self.assertIn(self.tool.name, response.content.decode("utf-8"))

    def test_get_one_tool(self):
        client = Client()
        response = client.get("/tools/1")
        self.assertIn(self.tool.name, response.content.decode("utf-8"))
        self.assertIn("Kaina: 15.00", response.content.decode("utf-8"))
