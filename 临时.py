from random import randint, sample
red_balls = [x for x in range(1, 34)]
print(red_balls)
selected_balls = sample(red_balls, 6)
print(selected_balls)
selected_balls.sort()
print(selected_balls)
