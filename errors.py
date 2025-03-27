result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("a should be > or = to b")
        if b > 100:
            raise IndexError("b should not be > than 100")
        return a / b
    except Exception as e:
        print(f"Exception in divider: {type(e).__name__}: {e}")
        return None
data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}
for key in data:
    try:
        key_int = int(key)
        value = data[key]
        res = divider(key_int, value)
        if res is not None:
            result.append(res)
    except Exception as e:
        print(f" {type(e).__name__}: {e}")

print("Result:", result)
