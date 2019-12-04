def test_dividenum():
    print("Give me two numbers, and I'll divide them.")
    print("Enter 'q' to quit.")
    while True:
        first_number = input("\nFirst number: ")
        if first_number == 'q':
            break
        second_number = input("Second number: ")
        try:
            answer = int(first_number) / int(second_number)
        except ZeroDivisionError:
            print("You can't divide by 0!")
        except ValueError:
            print("You can't input non number!")
        else:
            print(answer)

def testReadFile():
    filename = 'test'
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        print(contents)

testReadFile()