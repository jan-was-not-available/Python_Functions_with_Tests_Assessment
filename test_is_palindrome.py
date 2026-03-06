import sys
from os import system
system("clear")
from module import is_palindrome

############################## Do not modify tests.
def run_all_tests():
    tests = [
        (("racecar",), True),
        (("level",), True),
        (("hello",), False),
        (("a",), True),
        (("",), True),
    ]

    one_or_more_failures = False

    for i, (inputs, expected) in enumerate(tests):
        if one_test_success(inputs, expected, i):
            print(f"Test {i}: Pass!\n")
        else:
            print(f"Test {i}: Fail\n")
            one_or_more_failures = True

    if one_or_more_failures:
        print("❌ One or more tests failed.")
    else:
        print("✅ All tests passed!")


def one_test_success(inputs, expected, test_number):
    try:
        actual = is_palindrome(*inputs)

        print(f"Inputs: {inputs}")
        print(f"Expected: {expected}, Got: {actual}")

        assert actual == expected
        return True

    except AssertionError:
        print(f"Assertion failed on test {test_number}")

    except Exception as e:
        print(f"Error on test {test_number}: {type(e).__name__}: {e}")

    return False


if __name__ == "__main__":
    run_all_tests()
    sys.exit(0)