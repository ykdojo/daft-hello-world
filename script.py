import time


def main():
    # Burst: 10 logs immediately
    for i in range(10):
        print(f"Log line {i + 1}")

    # Then 1 log per second
    for i in range(10, 150):
        time.sleep(1)
        print(f"Log line {i + 1}")


if __name__ == "__main__":
    main()
