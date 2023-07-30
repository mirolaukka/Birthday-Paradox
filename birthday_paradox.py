import random

def birthday_paradox_probability(num_people):
    """Calculate the probability of at least two people sharing a birthday in a group."""
    num_simulations = 100000  # Number of simulations to run
    success_count = 0

    for _ in range(num_simulations):
        birthdays = set(random.randint(1, 365) for _ in range(num_people))
        if len(birthdays) != num_people:
            success_count += 1

    probability = success_count / num_simulations
    return probability

def main():
    num_people = 23  # Number of people in the group

    probability = birthday_paradox_probability(num_people)
    print(f"The probability of at least two people sharing a birthday in a group of {num_people} is approximately {probability*100:.2f}%")

    num_people = 70
    probability = birthday_paradox_probability(num_people)
    print(f"The probability of at least two people sharing a birthday in a group of {num_people} is approximately {probability*100:.2f}%")

if __name__ == "__main__":
    main()