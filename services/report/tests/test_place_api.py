import json

from tests.base import BaseTestCase
from tests.utils import add_report


class TestreportService(BaseTestCase):
    """Tests for the report Service."""

    def test_ping(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get('/reports/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])

    def test_reports(self):
        """Test reports endpoint"""
        add_report("Lugar 1")
        add_report("Lugar 2")
        response = self.client.get('/v1/reports/')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["count"], 2)
        self.assertEqual(data["results"][0]["name"], "Lugar 1")

    def test_reports_not_fount(self):
        """Test report endpoint"""
        unknownId = 33
        response = self.client.get('/v1/reports/{}'.format(unknownId))
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "report Not found with id: {}".format(unknownId))

    def test_reports_by_id(self):
        """Test report endpoint"""
        add_report("Lugar 1")
        report_id = 1
        response = self.client.get('/v1/reports/{}'.format(report_id))
        self.assertEqual(response.status_code, 200)

    def test_update_report(self):
        """Test report endpoint"""
        add_report("Lugar 1")
        report_id = 1
        updated_report_name = "Lugar 1 Edit"
        response = self.client.put(
            '/v1/reports/{}'.format(report_id),
            data=json.dumps({'name': updated_report_name}),
            content_type='application/json'
        )
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["data"]["name"], updated_report_name)
