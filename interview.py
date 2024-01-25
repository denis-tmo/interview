# import test cases
from word     import test_word_frequency
from circular import test_circular_queue
from password import test_valid_password

########################################################################################################################
#
#
########################################################################################################################

if __name__ == "__main__":

    # 1. test word frequency
    try:
        with open("data\word.txt","r") as data:
            for line in data:
                test_word_frequency(line)
                print()
    except IOError as err:
        print(f'error: {{err}}')
        exit(1)

    # 2. test circular queue using dictionary, queue size is set to 3
    test_circular_queue(max_size = 3)

    # 3. test password validation
    with open("data\password.txt","r") as data:
        for line in data:
            pwd_list = line.split(',')
            for pwd in pwd_list:
                valid = test_valid_password(pwd.strip())
                print(f'password: {pwd.strip()} valid: {valid}')
