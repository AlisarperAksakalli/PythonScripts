import random
while True:
    number_list = ["1", "2", "3", "4", "5", "6",]


    alici = random.choice(number_list)

    number_list.append(alici)



    a = input("Find Odd One between 1 and 6 (hard)")

    for item in range(6):
        if number_list[item] == alici:
            print(number_list[item], "is odd one.")
            if a == number_list[item]:
                print("means that you won!")
            else:
                print("means that you lost!")    

