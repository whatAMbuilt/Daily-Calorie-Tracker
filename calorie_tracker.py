print("Welcome to your Andy's Daily Calorie Tracker")
goal = int(input("What is your daily calorie goal?: "))
breakfast = int(input("How many calories did you have for breakfast?: "))
lunch = int(input("How many calories did you have for lunch?: "))
dinner = int(input("How many calories did you have for dinner?: "))
snack_count = int(input("How many snacks did you have today?: "))
total_snack_calories = 0
for i in range(snack_count):
    current_snack = int(input("How many calories in the snack?: "))
    total_snack_calories = current_snack + total_snack_calories
total_calories = breakfast + lunch + dinner + total_snack_calories
print(f"You have had a total of {total_calories} today")
remaining_calories = goal - total_calories
if remaining_calories > 0:
    print(f"You have {remaining_calories} calories remaining")
elif remaining_calories < 0:
    print(f"You are over your calorie goal by {abs(remaining_calories)}")
else: 
    print("You are right on target!")




