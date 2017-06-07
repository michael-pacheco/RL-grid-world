import random, datetime, time
from helper import initialize, move, move_up, move_down, move_left, move_right, probability_getter, state_get_index, action_get_index, q_print_policy


random.seed(datetime.datetime.now())

EPSILON = float(input("Enter value for epsilon (0.1): ") or 0.1)
ALPHA = float(input("Enter value for alpha (0.1): ") or 0.1)
GAMMA = float(input("Enter value for gamma (0.9): ") or 0.9)
p1 = float(input("Enter value for p1 (1): ") or 1)
p2 = float(input("Enter value for p2 (0): ")or 0)
total_episodes = int(input("Enter a number for max number of episodes (Perhaps under 10000): ") or 100)

s , a , Q, W, R = initialize()
total_time_steps = 0
Q_2 = []
for state in range(0, len(s)):
	Q_2.append([])
	for action in range(0, len(a)):
		Q_2[state].append(0)


def play():
    current_position_index = random.randint(0,len(s)-1)
    current_position = s[current_position_index][:]

    global Q
    global Q_2
    global total_time_steps
    total_rewards = 0
    while current_position != [10, 10]:
        total_time_steps += 1
        current_position_index = state_get_index(current_position[:])

        optimal_action_q1 = action_get_index(current_position_index, Q[:])
        optimal_action_q2 = action_get_index(current_position_index, Q_2[:])

        optimal_action = max(optimal_action_q1, optimal_action_q2)

        next_action = optimal_action

        next_position = probability_getter(current_position[:], next_action, p1, p2)

        randomizer = random.random()

        next_position_index = state_get_index(next_position[:])
        if next_position == [10, 10]:
            total_rewards = 500
        else:
            total_rewards = -1

        if randomizer <= 0.50:
            Q[state_get_index(current_position)][next_action] = Q[state_get_index(current_position)][:][next_action] + ALPHA*(total_rewards + GAMMA*(Q_2[state_get_index(next_position)][:][action_get_index(next_position_index, Q)]-Q[state_get_index(current_position)][:][next_action]))
        else:
            Q_2[state_get_index(current_position)][next_action] = Q_2[state_get_index(current_position)][:][next_action] + ALPHA*(total_rewards + GAMMA*(Q[state_get_index(next_position)][:][action_get_index(next_position_index, Q_2)]-Q_2[state_get_index(current_position)][:][next_action]))
        current_position = next_position

        if current_position == [10, 10]:
            break

iterations = 0
start_time = time.time()
while iterations <= total_episodes:
    play()
    if EPSILON >= 0.01:
         EPSILON -= 0.01
    iterations+=1


print("Number of episodes inputted: ", total_episodes)
print("Number of overall time steps: ", total_time_steps)
print("Computation time: ", time.time() - start_time)
print("Optimal policy at the end (Q1): ")
q_print_policy(Q[:])
print("Optimal policy at the end (Q2): ")
q_print_policy(Q_2[:])
