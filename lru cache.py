class IRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}          # key -> [value, frequency]
        self.usage_order = []    # most recent at end

    def get(self, key):
        if key not in self.cache:
            print("Output: -1 (Key not found)")
            return

        # Increase frequency
        self.cache[key][1] += 1

        # Update recency
        self.usage_order.remove(key)
        self.usage_order.append(key)

        print(f"Output: {self.cache[key][0]}")

    def put(self, key, value):
        if key in self.cache:
            self.cache[key][0] = value
            self.cache[key][1] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            if len(self.cache) >= self.capacity:
                # Find least frequent and least recent
                min_freq = float('inf')
                key_to_remove = None
                for k in self.usage_order:
                    if self.cache[k][1] < min_freq:
                        min_freq = self.cache[k][1]
                        key_to_remove = k
                del self.cache[key_to_remove]
                self.usage_order.remove(key_to_remove)

            self.cache[key] = [value, 1]
            self.usage_order.append(key)

    def display(self):
        print("\nCurrent cache state:")
        for key in self.usage_order:
            value, freq = self.cache[key]
            print(f"Key: {key}, Value: {value}, Frequency: {freq}")
        print()


# ------------------------------
# Manual Input Interface
# ------------------------------
def main():
    cap = int(input("Enter cache capacity: "))
    cache = IRUCache(cap)

    print("\nCommands:")
    print("put key value   --> to insert/update")
    print("get key         --> to retrieve a value")
    print("display         --> to show the cache state")
    print("exit            --> to quit\n")

    while True:
        command = input("Enter command: ").strip().lower()
        if command == "exit":
            break
        elif command == "display":
            cache.display()
        elif command.startswith("put"):
            try:
                _, key, value = command.split()
                cache.put(int(key), int(value))
            except:
                print("Invalid put command. Use: put key value")
        elif command.startswith("get"):
            try:
                _, key = command.split()
                cache.get(int(key))
            except:
                print("Invalid get command. Use: get key")
        else:
            print("Unknown command. Try again.")

if __name__ == "__main__":
    main()
