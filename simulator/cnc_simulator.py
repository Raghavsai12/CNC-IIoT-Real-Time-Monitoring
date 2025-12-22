import random
import time
import threading
print("CNC simulator running  locally \nPress ctrl+c to stop.\n")
def send_data():
    while True:
        try:
            t= round(random.uniform(25.0, 100.0), 2)
            m= round(random.uniform(1.0, 15.0), 2)
            c= round(random.uniform(100.0, 500.0), 2)
            data = {
                "temperature": t,
                "motor_current": m,
                "cutting_speed": c
            }
            print(f"Simulated data: {data}")
            time.sleep(3)
        except KeyboardInterrupt:
            print("\nSimulation stopped.")
            break
def receive_messages():
    while True:
        try:
            time.sleep(10)
        except KeyboardInterrupt:
            break
threading.Thread(target=receive_messages, daemon=True).start()
send_data()
