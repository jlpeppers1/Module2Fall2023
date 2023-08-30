# ask user their name

first_name = input("Please enter a first name:")


# ask them for rent 4 times
month_one = input("Please enter rent for month one:")
month_one_int = int(month_one)

month_two_int = int(input("Please enter rent for month two:"))

month_three_int = int(input("Please enter rent for month three:"))

month_four_int = int(input("Please enter rent for month four:"))


#do some math (calculate the max, add 3%)
max_rent = max(month_one_int, month_two_int, month_four_int, month_three_int)

#three_percent = max_rent * 0.03
#max_with_inflation = max_rent + three_percent
max_with_inflation = max_rent * 1.03


# print/output results
print(f"{first_name}, your max rent with inflation for next year is ${max_with_inflation}")
