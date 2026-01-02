from kafka import KafkaConsumer
import json
import sys

def create_consumer(topics, group_id='test-consumer-group'):
    """Create and return a Kafka consumer instance"""
    return KafkaConsumer(
        *topics,
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id=group_id,
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        key_deserializer=lambda k: k.decode('utf-8') if k else None,
        consumer_timeout_ms=10000  # Stop after 10 seconds of inactivity
    )

def consume_messages(topics):
    """Consume messages from specified Kafka topics"""
    print(f"\n{'='*50}")
    print(f"Starting to consume messages from topics: {topics}")
    print(f"{'='*50}\n")
    
    consumer = create_consumer(topics)
    
    try:
        message_count = 0
        for message in consumer:
            message_count += 1
            
            print(f"Message #{message_count}")
            print(f"  Topic: {message.topic}")
            print(f"  Partition: {message.partition}")
            print(f"  Offset: {message.offset}")
            print(f"  Key: {message.key}")
            print(f"  Value: {message.value}")
            print(f"  Timestamp: {message.timestamp}")
            print("-" * 50)
        
        print(f"\n{'='*50}")
        print(f"Total messages consumed: {message_count}")
        print(f"{'='*50}\n")
        
    except KeyboardInterrupt:
        print("\n\nConsumer interrupted by user")
    except Exception as e:
        print(f"Error consuming messages: {e}")
    finally:
        consumer.close()
        print("Consumer closed")

if __name__ == "__main__":
    # You can specify topics as command line arguments or use defaults
    if len(sys.argv) > 1:
        topics = sys.argv[1:]
    else:
        topics = ['topic1', 'topic2']
    
    print(f"Starting Kafka Consumer for topics: {topics}")
    consume_messages(topics)
    
    print("\nConsumer finished!")