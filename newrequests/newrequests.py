import queue
import threading
import time
import random

# створюємо чергу заявок

request_queue = queue.Queue()
max_requests = 20 # максимальна кількість заявок
processed_requests = 0 # лічильник оброблених заявок

# створюємо нову заявку та додаємо її до черги

def generate_request(request_id):
    global processed_requests
    request = f"Request {request_id}"
    print(f"Generated: {request}")
    request_queue.put(request)

# обробляємо заявку з черги

def process_request():
    global processed_requests
    while processed_requests < max_requests:
        if not request_queue.empty():
            request = request_queue.get()
            print(f"Processing: {request}")
            time.sleep(random.uniform(0.5, 2.0)) # імітація часу обробки
            print(f"Processed: {request}")
            request_queue.task_done()
            processed_requests += 1
        else:
            print("No requests to process, waiting for new requests...")
            time.sleep(1)

# генеруємо нові заявки та обробляємо їх  


def main():
    request_id = 1
    # запускається потік для обробки заявок
    processing_thread = threading.Thread(target=process_request, daemon=True)
    processing_thread.start()

    while request_id <= max_requests:
        generate_request(request_id)
        request_id +=1
        time.sleep(random.uniform(1, 3)) # імітація часу між новими заявками

  
    processing_thread.join()

if __name__ == "__main__":
    main()              
    

