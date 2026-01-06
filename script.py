import time


def main():
    # Burst: 10 logs quickly (tests volume handling)
    print("=== Starting burst phase ===")
    for i in range(10):
        print(f"[BURST] Log message #{i+1}: Hello World variation {i+1}")

    # Steady stream: 5 every 60 seconds for 5 minutes (tests real-time streaming)
    print("=== Starting steady phase ===")
    for batch in range(5):  # 5 batches = 5 minutes
        for i in range(5):
            msg_num = 10 + (batch * 5) + i + 1
            print(f"[STREAM] Log message #{msg_num}: Batch {batch+1}, item {i+1}")
        time.sleep(60)

    print("=== Done ===")


if __name__ == "__main__":
    main()
