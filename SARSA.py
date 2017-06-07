import random, datetime, time
from helper import initialize, move, move_up, move_down, move_left, move_right, probability_getter, state_get_index, action_get_index, initialize_policy, q_print_policy
random.seed(datetime.datetime.now())

EPSILON = float(input("Enter value for epsilon (0.1): ") or 0.1)
ALPHA = float(input("Enter value for alpha (0.1): ") or 0.1)
GAMMA = float(input("Enter value for gamma (0.9): ") or 0.9)
p1 = float(input("Enter value for p1 (1): ") or 1)
p2 = float(input("Enter value for p2 (0): ")or 0)
total_episodes = int(input("Enter a number for max number of episodes (Perhaps under 10000): ") or 100)

s , a , Q, W, R = initialize()
POL = initialize_policy()
first_policy = POL[:]
global total_time_steps
total_time_steps = 0

def play():
	global total_time_steps
	current_position_index = random.randint(0,len(s)-1)
	current_position = s[current_position_index][:]
	optimal_action = action_get_index(current_position_index, Q)
	total_rewards = 0
	while current_position != [10, 10]:
		total_time_steps +=1
		randomizer = random.random()
		if randomizer <= EPSILON:
			next_action = random.randint(0, 3)
			while next_action is optimal_action:
				next_action = random.randint(0, 3)
		else:
			next_action = optimal_action
		next_position = probability_getter(current_position[:], next_action, p1, p2)
		next_position_index = state_get_index(next_position[:])
		if next_position == [10, 10]:
			total_rewards = 500
		else:
			total_rewards = -1
		Q[state_get_index(current_position)][next_action] = Q[state_get_index(current_position)][:][next_action] + ALPHA*(total_rewards + GAMMA*(Q[state_get_index(next_position)][:][action_get_index(next_position_index, Q)]-Q[state_get_index(current_position)][:][next_action]))
		current_position = next_position
		current_position_index = next_position_index
		optimal_action = action_get_index(current_position_index, Q)

start_time = time.time()
iterations = 0
while iterations <= 10000:
	play()
	if EPSILON >= 0.01:
		EPSILON -= 0.01
	iterations+=1

print("Number of episodes inputted: ", total_episodes)
print("Number of overall time steps: ", total_time_steps)
print("Computation time: ", time.time() - start_time)
print("Optimal policy at the end: ")
q_print_policy(Q[:])
