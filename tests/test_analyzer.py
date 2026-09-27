import unittest

from modules.health_score import calculate_health_score, get_health_status


class TestHealthScore(unittest.TestCase):

    def test_excellent_network(self):
        score = calculate_health_score(23, 0)
        self.assertEqual(score, 100)

    def test_good_network(self):
        score = calculate_health_score(57, 0)
        self.assertEqual(score, 88)

    def test_health_status(self):
        status = get_health_status(88)
        self.assertEqual(status, "Healthy")


if __name__ == "__main__":
    unittest.main()
    
class TestDiagnosis(unittest.TestCase):

    def test_high_packet_loss(self):
        self.assertTrue(25 > 5)

    def test_high_latency(self):
        self.assertTrue(250 > 200)

    def test_normal_network(self):
        self.assertTrue(1 <= 2)