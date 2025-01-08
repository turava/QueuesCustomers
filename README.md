# QueuesCustomers

This project simulates a Customer Service Center using Python, focusing on queue management and time-based event simulation. It’s designed as an exercise to practice working with queues, randomization, and time-based loops in a real-world scenario. 

## Requirements
- Python 3.x
- Logging module (included in standard Python library)

## How to Run the Script
1. Save the script as `service_center_simulation.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is saved.
4. Execute the script by running: $ python main.py


## What the Console Shows
The console will output logging information that includes:
- When a new customer arrives.
- When a customer is attended and their waiting time.
- The average wait time after the simulation ends.

### Example Output
```text
2025-01-08 19:48:45,248 - INFO - New customer 0 arrived at minute 1.
2025-01-08 19:48:45,248 - INFO - Customer 0 attended at minute 1 after waiting 0 minutes.
2025-01-08 19:48:50,272 - INFO - New customer 1 arrived at minute 6.
2025-01-08 19:48:50,273 - INFO - Customer 1 attended at minute 6 after waiting 0 minutes.
2025-01-08 19:48:52,280 - INFO - New customer 2 arrived at minute 8.
2025-01-08 19:48:53,286 - INFO - New customer 3 arrived at minute 9.
2025-01-08 19:48:54,292 - INFO - New customer 4 arrived at minute 10.
2025-01-08 19:48:55,297 - INFO - Customer 2 attended at minute 11 after waiting 3 minutes.
2025-01-08 19:48:58,307 - INFO - Customer 3 attended at minute 14 after waiting 5 minutes.
2025-01-08 19:49:03,327 - INFO - Customer 4 attended at minute 19 after waiting 9 minutes.
2025-01-08 19:49:04,330 - INFO - New customer 5 arrived at minute 20.
2025-01-08 19:49:05,336 - INFO - New customer 6 arrived at minute 21.
2025-01-08 19:49:07,347 - INFO - Customer 5 attended at minute 23 after waiting 3 minutes.
```

### Notes
- Each minute of real time is simulated as a one-second interval in this script, so the total run time of the script will be approximately 60 seconds.
- Adjust the `time.sleep(1)` to a smaller value for faster simulation.

## Modifications
You can modify the customer arrival rate or service time to see how it affects the waiting times and service efficiency. This can be done by changing the parameters in the random functions within the script.
