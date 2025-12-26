import random

def guess_number(guesses, number=None):
    if number is None:
        number = random.randint(1, 10)

    attempts = 0

    for guess in guesses:
        attempts += 1
        if guess < number:
            print("Too low! ⬇️")
        elif guess > number:
            print("Too high! ⬆️")
        else:
            print(f"🎉 Correct! Guessed in {attempts} attempts.")
            return attempts

    print("❌ Number not guessed")
    return attempts

def test_guess_number():
    # Test case 1
    attempts = guess_number([2, 4, 6, 8], number=6)
    assert attempts == 3

    # Test case 2
    attempts = guess_number([1, 3, 5], number=5)
    assert attempts == 3

    # Test case 3 (not guessed)
    attempts = guess_number([1, 2, 3], number=7)
    assert attempts == 3

    print("✅ All tests passed!")

test_guess_number()
