from program import initialize_search

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

if __name__ == "__main__":
    main()
