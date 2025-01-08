# test_service_center_simulation.py
import unittest
from service_center_library_queue import simulate_service_center

class TestServiceCenterSimulation(unittest.TestCase):
    def test_average_wait_time_controlled_conditions(self):
        """Test that the average wait time is calculated correctly under controlled conditions."""
        # Running the simulation with specific parameters to ensure predictability
        average_wait_time = simulate_service_center(runtime_minutes=10, max_arrival_interval=1, service_time_range=(2, 2), speed_up_factor=1000)
        
        # Expected wait time should be closely zero as customers are attended immediately
        self.assertTrue(0 <= average_wait_time <= 2, "Average wait time should be within the range of 0 to 2 minutes under controlled conditions")

if __name__ == '__main__':
    unittest.main()
