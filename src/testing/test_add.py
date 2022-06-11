def multiply(a: int | str, b: int) -> int | str:
    return a * b

def test_multiply():
    assert multiply(1,2) == 2, "Should be 3"
    assert multiply("hello", 1) == "hello", "Should be hellohello"
    assert multiply("hello", 2) == 4, "Should be hellohello"

if __name__ == "__main__":
    test_multiply()
    print("Test done")
