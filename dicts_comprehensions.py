def run():
    my_dict = {}

    for i in range(1,101):
        if i % 3 != 0:
            my_dict[i] = i**3

    dict_comprehension = {i: i**3 for i in range(1,101) if i % 3 != 0}
    print(dict_comprehension)

    challenge_dict = {i: i**0.5 for i in range(1,1001)}
    print(challenge_dict)

if __name__ == '__main__':
    run()
