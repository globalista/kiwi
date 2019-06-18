import program
import sys


def check_parameters(argv):
    if len(argv) == 0:
        return False
    if len(argv) == 2:
        try:
            return int(argv[0]), int(argv[1])
        except ValueError:
            pass
    raise ValueError('usage: python3 find_combinations.py [bags_taken hours_to_transfer]')


def main(argv):
    all_flights = program.all_flights_init()
    parameters = check_parameters(argv)
    if parameters:
        bags_taken = parameters[0]
        hours_to_transfer_needed = parameters[1]
        program.initialize_search(bags_taken, hours_to_transfer_needed, all_flights)
    else:
        for bags_taken in [0, 1, 2]:
            for hours_to_transfer_needed in [1, 2, 3, 4]:
                program.initialize_search(bags_taken, hours_to_transfer_needed, all_flights)


if __name__ == "__main__":
    main(sys.argv[1:])
