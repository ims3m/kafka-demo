from kafka import KafkaProducer
import json
import time
from datetime import datetime

def create_producer():
    """Create and return a Kafka producer instance"""
    return KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        key_serializer=lambda k: k.encode('utf-8') if k else None
    )

def produce_messages(topic, num_messages=10):
    """Produce messages to a specified Kafka topic"""
    producer = create_producer()
    
    print(f"\n{'='*50}")
    print(f"Starting to produce messages to topic: {topic}")
    print(f"{'='*50}\n")
    
    try:
        for i in range(num_messages):
            message = {
                'id': i,
                'message': f'Message {i} for {topic}',
                'timestamp': datetime.now().isoformat(),
                'topic': topic
            }
            
            key = f'key-{i}'
            
            # Send message
            future = producer.send(topic, key=key, value=message)
            record_metadata = future.get(timeout=10)
            
            print(f"  Sent: {message}")
            print(f"  Topic: {record_metadata.topic}")
            print(f"  Partition: {record_metadata.partition}")
            print(f"  Offset: {record_metadata.offset}\n")
            
            time.sleep(0.5)
        
        print(f"{'='*50}")
        print(f"Successfully produced {num_messages} messages to {topic}")
        print(f"{'='*50}\n")
        
    except Exception as e:
        print(f"Error producing message: {e}")
    finally:
        producer.flush()
        producer.close()

if __name__ == "__main__":
    # Produce messages to both topics
    print("Starting Kafka Producer...")
    
    # Produce to topic1
    produce_messages('topic1', num_messages=5)
    
    # Produce to topic2
    produce_messages('topic2', num_messages=5)
    
    print("Producer finished!")