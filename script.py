import time


def main():
    # Burst: 100 logs quickly (tests volume handling)
    print("=== Starting burst phase ===")
    for i in range(100):
        print(f"[BURST] Log message #{i+1}: Hello World variation {i+1}")

    # Steady stream: 10 every 5 seconds for 1 minute (tests real-time streaming)
    print("=== Starting steady phase ===")
    for batch in range(12):  # 12 batches = 60 seconds
        for i in range(10):
            msg_num = 100 + (batch * 10) + i + 1
            print(f"[STREAM] Log message #{msg_num}: Batch {batch+1}, item {i+1}")
        time.sleep(5)

    print("=== Done ===")


if __name__ == "__main__":
    main()
