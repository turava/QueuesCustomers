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

def simulate_service_center():
    customers = Queue()
    current_time = 0
    total_wait_time = 0
    num_customers_served = 0
    next_free_time = 0  # Track when the current service will be finished

    while current_time < 60:
        if random.randint(1, 3) == 1:
            customer = Customer(current_time)
            customers.put(customer)
            logging.info(f'New customer {customer.id} arrived at minute {current_time}.')

        if current_time >= next_free_time and not customers.empty():
            next_customer = customers.get()
            service_time = random.randint(2, 5)  # Customer is attended for 1 to 5 minutes
            next_customer.set_attention_time(current_time)
            next_free_time = current_time + service_time  # Update next free time based on service duration
            total_wait_time += next_customer.wait_time
            num_customers_served += 1

        time.sleep(1)
        current_time += 1

    # Output average wait time
    if num_customers_served > 0:
        average_wait_time = total_wait_time / num_customers_served
        logging.info(f'Average wait time for customers: {average_wait_time:.2f} minutes')
    else:
        logging.info("No customers were served.")

if __name__ == "__main__":
    simulate_service_center()