import random
from time import time


def head_tail():
    heads = 0
    tails = 0
    count = 0
    count_2 = 0
    num = int(input('How many flips do you want?: '))

    while True:
        choice = ['heads', 'tails']
        choice = random.choice(choice)
        total = heads, tails

        if choice == 'heads':
            heads += 1
            count += 1
            count_2 += 1
        elif choice == 'tails':
            tails += 1
            count += 1
            count_2 += 1

        if count == num + 1:
            print(total)
            break

        if count_2 == 1000:
            print('Flip #', count, 'Heads:', heads, 'Tails:', tails)
            print('')
            count_2 = 0


def main():
    start = time()
    head_tail()
    print('Total time:', time() - start)


main()