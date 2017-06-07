import random, datetime, time
from helper import initialize, move, move_up, move_down, move_left, move_right, probability_getter, state_get_index, action_get_index, initialize_policy, mc_print_policy


random.seed(datetime.datetime.now())

EPSILON = float(input("Enter value for epsilon (0.1): ") or 0.1)
ALPHA = float(input("Enter value for alpha (0.1): ") or 0.1)
GAMMA = float(input("Enter value for gamma (0.9): ") or 0.9)
p1 = float(input("Enter value for p1 (1): ") or 1)
p2 = float(input("Enter value for p2 (0): ")or 0)
total_episodes = int(input("Enter a number for max number of episodes (Warning: MC takes an extremely long time - 50 and under is appropriate!): ") or 25)

s , a , Q, W, R = initialize()
POL = initialize_policy()


global total_time_steps
total_time_steps = 0
'''
Agent can randomly start anywhere in the grid world
'''
current_position_index = random.randint(0,len(s)-1)
current_position = s[current_position_index][:]
action_according_to_policy = POL[current_position_index]


def play(current_position, action_according_to_policy, set_of_states, set_of_actions):

	global total_time_steps
	set_of_states = []
	set_of_actions = []
	set_of_states.append(current_position[:])
	set_of_actions.append(action_according_to_policy)

	while current_position != [10, 10]:
		total_time_steps +=1

		current_position = probability_getter(current_position, action_according_to_policy, p1, p2)

		current_position_index = state_get_index(current_position[:])

		set_of_states.append(current_position[:])

		randomize_action = random.random()

		if randomize_action <= (1-EPSILON+(EPSILON/4)):
			next_action = POL[current_position_index]
		else:
			next_action = random.randint(0, 3)
			while next_action is POL[current_position_index]:
				next_action = random.randint(0, 3)

		POL[current_position_index] = next_action

		action_according_to_policy = POL[current_position_index]

		set_of_actions.append(action_according_to_policy)

	update_values(set_of_states, set_of_actions)





def update_values(set_of_states, set_of_actions):
	G = 0
	i = 0
	for state in set_of_states:
		if set_of_states[i][:] == [10, 10]:
			break
		if set_of_states[i+1][:] == [10, 10]:
			G += 500
		else:
			G += (-1)

		state_index = state_get_index(state)
		actionIndex = set_of_actions[i]

		W[state_index][actionIndex] += 1

		Q[state_index][actionIndex] = Q[state_index][actionIndex] + (G 	- (Q[state_index][actionIndex]/W[state_index][actionIndex]))
		i+=1

	update_policy(set_of_states)

def update_policy(set_of_states):
	old_policy = POL[:]
	for state in set_of_states:

		state_index = state_get_index(state)

		best_action_index = action_get_index(state_index, Q)

		optimal_action = best_action_index

		randomize_action = random.random()

		if randomize_action <= (1-EPSILON+(EPSILON/4)):
			next_action = optimal_action
		else:
			next_action = random.randint(0, 3)
			while next_action is optimal_action:
				next_action = random.randint(0, 3)

		POL[state_index] = next_action

start_time = time.time()
iterations = 0
while iterations <= total_episodes:
	play(current_position, action_according_to_policy, [], [])
	current_position_index = random.randint(0,len(s)-1)
	current_position = s[current_position_index][:]
	action_according_to_policy = POL[current_position_index]

	print(iterations)
	iterations+=1

print("Number of episodes inputted: ", total_episodes)
print("Number of overall time steps: ", total_time_steps)
print("Computation time: ", time.time() - start_time)
print("Optimal policy at the end: ")
mc_print_policy(POL[:])
