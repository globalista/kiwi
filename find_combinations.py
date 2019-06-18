from program import initialize_search
import sys

'''
BAGS_TAKEN = 2
HOURS_TO_TRANSFER_NEEDED = 1


def main():
    if True:#zjisti podminku
        bags_taken = BAGS_TAKEN #zjisti hodnotu
        hours_to_transfer_needed = HOURS_TO_TRANSFER_NEEDED#zjisti hodnotu
        initialize_search(bags_taken, hours_to_transfer_needed)
    else:
        for bags_taken in [1,2,3]:
            for hours_to_transfer_needed in [1,2,3,4]:
                initialize_search(bags_taken, hours_to_transfer_needed)
'''
def check_parameters(argv):
    print(argv)
    print(len(argv))
    print('*********************')
    if len(argv) == 0:
        return False
    if len(argv) == 2:
        try:
            print(argv[0], argv[1])
            return int(argv[0]), int(argv[1])
        except ValueError:
            pass
    raise ValueError('usage: python3 find_combinations.py [bags_taken hours_to_transfer]')


def main(argv):
    parameters = check_parameters(argv)
    if parameters:
        bags_taken = parameters[0]
        hours_to_transfer_needed = parameters[1]
        initialize_search(bags_taken, hours_to_transfer_needed)
    else:
        for bags_taken in [0,1,2]:
            for hours_to_transfer_needed in [1,2,3,4]:
                initialize_search(bags_taken, hours_to_transfer_needed)




if __name__ == "__main__":
    main(sys.argv[1:])
