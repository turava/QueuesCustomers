import time
import random
import logging
from queue import Queue

"""Queue: The Queue from Python's queue module is used to manage the customers in a first-in-first-out (FIFO) manner."""
# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Customer:
    """Class representing a customer at a service center."""
    id_counter = 0  # Class variable to keep track of unique customer IDs

    def __init__(self, arrival_time):
        self.id = Customer.id_counter  # Unique identifier for each customer
        self.arrival_time = arrival_time
        self.attention_time = None
        self.wait_time = None
        Customer.id_counter += 1

    def set_attention_time(self, attention_time):
        """Set the time when the customer is attended."""
        self.attention_time = attention_time
        self.wait_time = self.attention_time - self.arrival_time
        logging.info(f'Customer {self.id} attended at minute {self.attention_time} after waiting {self.wait_time} minutes.')

def simulate_service_center(runtime_minutes=60, max_arrival_interval=3, service_time_range=(2, 5), speed_up_factor=1):
    customers = Queue()
    current_time = 0
    total_wait_time = 0
    num_customers_served = 0
    next_free_time = 0  # Add a tracker for when the next customer can be attended

    while current_time < runtime_minutes:
        if random.randint(1, max_arrival_interval) == 1:
            customer = Customer(current_time)
            customers.put(customer)

        if current_time >= next_free_time and not customers.empty():
            next_customer = customers.get()
            service_time = random.randint(*service_time_range)
            next_customer.set_attention_time(current_time)
            next_free_time = current_time + service_time  # Update when the next customer can be attended
            total_wait_time += next_customer.wait_time
            num_customers_served += 1

        time.sleep(1 / speed_up_factor)  # Speed up the simulation for testing
        current_time += 1

    average_wait_time = total_wait_time / num_customers_served if num_customers_served > 0 else 0
    return average_wait_time


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    avg_wait_time = simulate_service_center()
    logging.info(f"Average wait time: {avg_wait_time:.2f} minutes")