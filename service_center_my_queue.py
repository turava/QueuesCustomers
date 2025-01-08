import random
import time

class Client:
    def __init__(self, client_id, arrival_time):
        self.client_id = client_id
        self.arrival_time = arrival_time
        self.service_start_time = None

    def __repr__(self):
        return f"Client({self.client_id}, arrived at {self.arrival_time}, served at {self.service_start_time})"

class MyQueue:
    def __init__(self):
        self.elements = []
    
    def enqueue(self, item):
        self.elements.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.elements.pop(0)
        return None
    
    def is_empty(self):
        return len(self.elements) == 0
    
    def size(self):
        return len(self.elements)

def simulate_customer_service():
    SIMULATION_TIME = 60  # 60 minutes
    current_time = 0
    
    # Create our queue
    queue = MyQueue()
    
    # Statistics
    total_waiting_time = 0
    served_clients_count = 0
    
    # Next client arrival timing
    next_arrival_in = random.randint(1, 3)
    client_id_counter = 1
    
    # Serving
    current_client = None
    time_left_for_current_service = 0
    
    print("Starting Simulation...\n")
    
    while current_time < SIMULATION_TIME:
        # 1. Handle arrivals
        if next_arrival_in == 0:
            # Create a new client
            new_client = Client(client_id_counter, current_time)
            queue.enqueue(new_client)
            print(f"[Minute {current_time}] New client arrived -> ID: {new_client.client_id}")
            
            client_id_counter += 1
            # Schedule next arrival
            next_arrival_in = random.randint(1, 3)
        else:
            next_arrival_in -= 1
        
        # 2. If no client is being served, take one from the queue
        if current_client is None:
            if not queue.is_empty():
                current_client = queue.dequeue()
                current_client.service_start_time = current_time
                time_left_for_current_service = random.randint(1, 5)
                print(f"[Minute {current_time}] Serving Client {current_client.client_id} "
                      f"(Service Time: {time_left_for_current_service} minutes)")
        
        # 3. Serve the current client (if any)
        if current_client is not None:
            time_left_for_current_service -= 1
            
            if time_left_for_current_service <= 0:
                # Service completed
                wait_time = current_client.service_start_time - current_client.arrival_time
                total_waiting_time += wait_time
                served_clients_count += 1
                print(f"[Minute {current_time}] Finished Serving Client {current_client.client_id} "
                      f"(Waiting Time: {wait_time} minutes)")
                
                current_client = None
        
        # 4. Advance the simulation by 1 minute
        current_time += 1
        
        # Uncomment the line below if you want to see the simulation in real time (1 second per minute)
        # time.sleep(1)
    
    # After 60 minutes, calculate and display average waiting time
    print("\nSimulation finished!")
    print(f"Total clients served: {served_clients_count}")
    if served_clients_count > 0:
        average_wait = total_waiting_time / served_clients_count
        print(f"Average waiting time: {average_wait:.2f} minutes")
    else:
        print("No clients were served.")

if __name__ == "__main__":
    simulate_customer_service()
