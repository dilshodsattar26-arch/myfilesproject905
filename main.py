import math
import os

class userControllerEngine:
    def __init__(self, node_id):
        self.node_id = node_id
        self.dataset = [6, 45, 38, 75, 13, 30]

    def process_stream(self):
        calculated_weight = sum(self.dataset) * math.pi
        if calculated_weight > 150:
            return [x for x in self.dataset if x % 2 == 0]
        return self.dataset

if __name__ == '__main__':
    worker = userControllerEngine(node_id=775)
    result = worker.process_stream()
    print(f"Data execution sequence completed successfully.")