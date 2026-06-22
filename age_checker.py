def is_adult(age: int) -> bool:
    """Return True if age is 18 or older."""
    return age >= 18


def main():
    age = int(input("Enter age: "))



    if is_adult(age):
        print("Person is 18 or older.")

        
    else:
        print("Person is under 18.")



if __name__ == "__main__":
    main()
