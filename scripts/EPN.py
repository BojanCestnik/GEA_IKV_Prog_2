import time
import random
from queue import Queue, Empty
from threading import Thread

# Event generator function
def event_generator(event_queue):
    for i in range(10):
        event = f"Event-{i}"
        event_queue.put(event)
        print(f"Generated: {event}")
        time.sleep(random.uniform(0.1, 1.0))

# Event processor function
def event_processor(event_queue, processed_queue):
    while True:
        try:
            event = event_queue.get(timeout=2)  # Wait for up to 2 seconds for an event
            processed_event = f"Processed {event}"
            processed_queue.put(processed_event)
            print(f"Processed: {event} -> {processed_event}")
            time.sleep(random.uniform(0.1, 0.5))
        except Empty:
            print("No events to process. Exiting.")
            break

# Event consumer function
def event_consumer(processed_queue):
    while True:
        try:
            processed_event = processed_queue.get(timeout=2)  # Wait for up to 2 seconds for a processed event
            print(f"Consumed: {processed_event}")
            time.sleep(random.uniform(0.1, 0.5))
        except Empty:
            print("No processed events to consume. Exiting.")
            break

if __name__ == "__main__":
    event_queue = Queue()
    processed_queue = Queue()

    # Create and start event generator, processor, and consumer threads
    generator_thread = Thread(target=event_generator, args=(event_queue,))
    processor_thread = Thread(target=event_processor, args=(event_queue, processed_queue))
    consumer_thread = Thread(target=event_consumer, args=(processed_queue,))

    generator_thread.start()
    processor_thread.start()
    consumer_thread.start()

    # Wait for all threads to finish
    generator_thread.join()
    processor_thread.join()
    consumer_thread.join()

    print("Event processing network completed.")
