import random as rd


def menu():
    item_ = {'1': 'simple operations with numbers 2-9', '2': 'integral squares of 11-29'}
    while 1:
        print('Which level do you want? Enter a number:')
        for x in item_:
            print(f'{x} - {item_[x]}')
        choice = input()
        if choice in {'1', '2'}:
            break
        print('Incorrect format')
    return choice, item_[choice]


def quiz(choice):
    mark = 0
    for i in range(5):
        a, b, sign = *[rd.randint(2, 9) for _ in range(2)], rd.choice(["+", "-", "*"])
        c = rd.randint(11, 29)
        while 1:
            if choice == '1':
                # noinspection PyTupleAssignmentBalance
                print(f'{a} {sign} {b}')
                true_answer = eval(f'{a} {sign} {b}')
            elif choice == '2':
                print(f'{c}')
                true_answer = c ** 2
            answer = input()
            if answer.replace('-', '').isdigit():
                if int(answer) == true_answer:
                    print('Right')
                    mark += 1
                else:
                    print('Wrong!')
                break
            else:
                print('Wrong format! Try again.')
    return mark


def result_save(name, choice, mark):
    with open('results.txt', 'a') as file:
        file.write(f'{name}: {mark}/5 in level {choice[0]} ({choice[1]}).')
        print(f'The results are saved in "{file.name}".')


def main():
    navigation = menu()
    mark = quiz(navigation[0])

    print(f'Your mark is {mark}/5.  Would you like to save the result? Enter yes or no.')
    choice = input()

    if choice in {'yes', 'YES', 'y', 'Yes'}:
        print('What is your name?')
        name_user = input()
        result_save(name_user, navigation, mark)


if __name__ == '__main__':
    main()
