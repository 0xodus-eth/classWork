# Lamport's Logical Clock 
class LamportClock: 
    def __init__(self): 
        self.time = 0 
 
    def send_message(self): 
        self.time += 1 
        return self.time 
 
    def receive_message(self, received_time): 
        self.time = max(self.time, received_time) + 1 
        return self.time 
 
# Example usage 
clock1 = LamportClock() 
clock2 = LamportClock() 
 
# Simulate messages 
message_time1 = clock1.send_message() 
print(f"Clock1 Time after sending: {message_time1}") 
 
message_time2 = clock2.receive_message(message_time1) 
print(f"Clock2 Time after receiving: {message_time2}") 
 
 