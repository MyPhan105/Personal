# My Phan
# PSID 2176210
# lab 11.27

num1 = int(input("Enter player 1's jersey number:\n"))
rate1 = int(input("Enter player 1's rating:\n"))
print()
num2 = int(input("Enter player 2's jersey number:\n"))
rate2 = int(input("Enter player 2's rating:\n"))
print()
num3 = int(input("Enter player 3's jersey number:\n"))
rate3 = int(input("Enter player 3's rating:\n"))
print()
num4 = int(input("Enter player 4's jersey number:\n"))
rate4 = int(input("Enter player 4's rating:\n"))
print()
num5 = int(input("Enter player 5's jersey number:\n"))
rate5 = int(input("Enter player 5's rating:\n"))
print()

num_list = []
roster_dict = {num1: rate1, num2: rate2, num3: rate3, num4: rate4, num5: rate5}
for num in roster_dict.keys():
    num_list.append(num)

num_list.sort()

new_dict = {}
for i in num_list:
    new_dict[i] = roster_dict[i]

print('ROSTER')
for num, rating in new_dict.items():
    print(f"Jersey number: {num}, Rating: {rating}")


print()
print('MENU\n'
      'a - Add player\n'
      'd - Remove player\n'
      'u - Update player rating\n'
      'r - Output players above a rating\n'
      'o - Output roster\n'
      'q - Quit\n')

user_option = input('Choose an option:\n')
while user_option != 'q':

    if user_option == 'o':
        print("ROSTER")
        for num, rating in new_dict.items():
            print(f"Jersey number: {num}, Rating: {rating}")
        user_option = input('Choose an option:\n')
        pass

    elif user_option == 'a':
        new_dict[int(input("Enter a new player's jersey number:\n"))] = int(input("Enter the player's rating:\n"))
        print('MENU\n'
              'a - Add player\n'
              'd - Remove player\n'
              'u - Update player rating\n'
              'r - Output players above a rating\n'
              'o - Output roster\n'
              'q - Quit\n')

        user_option = input('Choose an option:\n')

    elif user_option == 'd':
        jersey_to_delete = int(input("Enter a jersey number"))
        if jersey_to_delete in new_dict:
            del new_dict[jersey_to_delete]
        else:
            print("Jersey number not found")
        print('MENU\n'
              'a - Add player\n'
              'd - Remove player\n'
              'u - Update player rating\n'
              'r - Output players above a rating\n'
              'o - Output roster\n'
              'q - Quit\n')

        user_option = input('Choose an option:\n')

    elif user_option == 'u':
        update_num = int(input("Enter a jersey number:\n"))
        update_rate = int(input("Enter a new rating for player:\n"))
        for num in new_dict:
            if update_num == num:
                new_dict[update_num] = update_rate
        print('MENU\n'
              'a - Add player\n'
              'd - Remove player\n'
              'u - Update player rating\n'
              'r - Output players above a rating\n'
              'o - Output roster\n'
              'q - Quit\n')

        user_option = input('Choose an option:\n')

    elif user_option == 'r':
        user_rating = int(input("Enter a rating:\n"))
        print(f"ABOVE {user_rating}")
        for num, rating in new_dict.items():
            if int(new_dict[num]) > user_rating:
                print(f"Jersey number: {num}, Rating: {rating}")
        print()
        print('MENU\n'
              'a - Add player\n'
              'd - Remove player\n'
              'u - Update player rating\n'
              'r - Output players above a rating\n'
              'o - Output roster\n'
              'q - Quit\n')

        user_option = input('Choose an option:\n')
