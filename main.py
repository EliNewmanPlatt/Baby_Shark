"""----------------------------------------------------------------
Name:       Eli Newman
Assignment: Lab - Baby Shark
Course:     CS 1430, Section X, Fall 2026
Purpose:    This program is designed to be practice for Python
            functions

Input: None

Output: The sound Baby Shark, with three verses:
        Baby Shark,
        doo-doo-doo-do-do-do-do *3
        Baby Shark!
        Mommy Shark,
        doo-doo-doo-do-do-do-do *3
        Mommy Shark!
        Daddy Shark,
        doo-doo-doo-do-do-do-do *3
        Daddy Shark!
----------------------------------------------------------------"""

##############
# CONSTANTS
##############
REPEAT = 3

def verse(shark):
    for i in range(REPEAT):
        print(f"{shark},")
        print("doo-doo-doo-do-do-do-do")
    print(f"{shark}!")

def main():
    verse("Baby Shark")
    verse("Mommy Shark")
    verse("Daddy Shark")

if __name__ == "__main__":
    main()