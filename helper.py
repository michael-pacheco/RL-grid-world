import random, datetime, time

random.seed(datetime.datetime.now())
'''
Initializes variable lists including states (s), actions (a), reward (R), state/action pair counter (W), state/value pair value (Q) - and returns them.
'''
def initialize():
	s = []
	for x in range (1,11): #range(1,11) goes from 1-10
		for y in range(1,11):
			s.append([x,y])
	a = ["up", "down", "left", "right"]


	Q = []
	W = []
	R = []
	for state in range(0, len(s)):
		Q.append([])
		W.append([])
		R.append([])
		for action in range(0, len(a)):
			Q[state].append(0)
			W[state].append(0)
			R[state].append(0)
	return s, a, Q, W, R

'''
Creates an arbitrary policy.
'''
def initialize_policy():
	POL = []
	for state in range(0, len(s)):
		POL.append(random.randint(0,3))
	return POL

s, a, Q, W, R = initialize()
'''
Moves the agent in the specified direction and returns the resulting position.
'''
def move(current_position, action):
	if action == 0:
		resulting_position = current_position
		resulting_position[1] +=1
		return resulting_position
	elif action == 1:
		resulting_position = current_position
		resulting_position[1] -=1
		return resulting_position
	elif action == 2:
		resulting_position = current_position
		resulting_position[0] -=1
		return resulting_position
	else:
		resulting_position = current_position
		resulting_position[0] +=1
		return resulting_position

'''
Moves the agent up, and returns the resulting position.
'''
def move_up(current_position):
	resulting_position = current_position[:]
	resulting_position[1] +=1
	return resulting_position[:]

'''
Moves the agent down, and returns the resulting position.
'''
def move_down(current_position):
	resulting_position = current_position[:]
	resulting_position[1] -=1
	return resulting_position[:]

'''
Moves the agent left, and returns the resulting position.
'''
def move_left(current_position):
	resulting_position = current_position[:]
	resulting_position[0] -=1
	return resulting_position[:]

'''
Moves the agent right, and returns the resulting position.
'''
def move_right(current_position):
	resulting_position = current_position[:]
	resulting_position[0] +=1
	return resulting_position[:]

'''
Gets the probability of the agent moving in the direction that it wants to.
Will return the resulting position based on the probabilities.
'''
def probability_getter(current_state, action, p1, p2):
	randomizer = random.random()
	'''
	Below are cases where the agent is in a corner
	'''
	#[1,10] cases
	if current_state == [1, 10] and action == 0:
		if randomizer <= ((1+p1+p2)/2):
			return current_state
		elif randomizer <= ((1-p1-p2)/2):
			return move_right(current_state)

	elif current_state == [1, 10] and action == 2:
		if randomizer <= ((1+p1+p2)/2):
			return current_state
		elif randomizer <= ((1-p1-p2)/2):
			return move_down(current_state)

	#[1,1] cases
	elif current_state == [1, 1] and action == 1:
		if randomizer <= ((1+p1+p2)/2):
			return current_state
		elif randomizer <= ((1-p1-p2)/2):
			return move_right(current_state)

	elif current_state == [1, 1] and action == 2:
		if randomizer <= ((1+p1+p2)/2):
			return current_state
		elif randomizer <= ((1-p1-p2)/2):
			return move_up(current_state)

	elif current_state == [3, 1] and action == 1:
		if randomizer <= ((1+p1+p2)/2):
			return current_state
		elif randomizer <= ((1-p1-p2)/2):
			return move_left(current_state)

	elif current_state == [3, 1] and action == 3:
		if randomizer <= ((1+p1+p2)/2):
			return current_state
		elif randomizer <= ((1-p1-p2)/2):
			return move_up(current_state)

	elif current_state == [4, 1] and action == 2:
		if randomizer <= ((1+p1+p2)/2):
			return current_state
		elif randomizer <= ((1-p1-p2)/2):
			return move_up(current_state)

	elif current_state == [3, 1] and action == 1:
		if randomizer <= ((1+p1+p2)/2):
			return current_state
		elif randomizer <= ((1-p1-p2)/2):
			return move_right(current_state)

	elif current_state == [6, 10] and action == 3:
		if randomizer <= ((1+p1+p2)/2):
			return current_state
		elif randomizer <= ((1-p1-p2)/2):
			return move_down(current_state)

	elif current_state == [6, 10] and action == 0:
		if randomizer <= ((1+p1+p2)/2):
			return current_state
		elif randomizer <= ((1-p1-p2)/2):
			return move_left(current_state)

	elif current_state == [7, 10] and action == 0:
		if randomizer <= ((1+p1+p2)/2):
			return current_state
		elif randomizer <= ((1-p1-p2)/2):
			return move_right(current_state)

	elif current_state == [7, 10] and action == 2:
		if randomizer <= ((1+p1+p2)/2):
			return current_state
		elif randomizer <= ((1-p1-p2)/2):
			return move_down(current_state)

	elif current_state == [10, 1] and action == 3:
		if randomizer <= ((1+p1+p2)/2):
			return current_state
		elif randomizer <= ((1-p1-p2)/2):
			return move_up(current_state)

	elif current_state == [10, 1] and action == 1:
		if randomizer <= ((1+p1+p2)/2):
			return current_state
		elif randomizer <= ((1-p1-p2)/2):
			return move_left(current_state)

	#Cases below are when we bump into a wall.
	#Note that we already accounted for all corner and corner wall cases above, so the above cases will execute first if condition is met.
	elif current_state[0] == 1 and action == 2:
		#with probability p1+p2, we will stay in our current spot
		if randomizer <= (p1+p2):
			return current_state
		else:
			if randomizer <= ((1-p1-p2)/2):
				return move_up(current_state)
			else:
				return move_down(current_state)


	#if we are at most right and trying to go right
	elif current_state[0] == 10 and action == 3:
		if randomizer <= (p1+p2):
			return current_state
		else:
			if randomizer <= ((1-p1-p2)/2):
				return move_up(current_state)
			else:
				return move_down(current_state)


	elif current_state[1] == 10 and action == 0:
		if randomizer <= (p1+p2):
			return current_state
		else:
			if randomizer <= ((1-p1-p2)/2):
				return move_right(current_state)
			else:
				return move_left(current_state)


	elif current_state[1] == 1 and action == 1:
		if randomizer <= (p1+p2):
			return current_state
		else:
			if randomizer <= ((1-p1-p2)/2):
				return move_right(current_state)
			else:
				return move_left(current_state)


	elif current_state[0] == 3 and current_state[1] in range(1,9) and action == 3:
		if randomizer <= (p1+p2):
			return current_state
		else:
			if randomizer <= ((1-p1-p2)/2):
				return move_up(current_state)
			else:
				return move_down(current_state)


	elif current_state[0] == 4 and current_state[1] in range(1,9) and action == 2:
		if randomizer <= (p1+p2):
			return current_state
		else:
			if randomizer <= ((1-p1-p2)/2):
				return move_up(current_state)
			else:
				return move_down(current_state)

	elif current_state[0] == 6 and current_state[1] in range(3,11) and action == 3:
		if randomizer <= (p1+p2):
			return current_state
		else:
			if randomizer <= ((1-p1-p2)/2):
				return move_up(current_state)
			else:
				return move_down(current_state)

	elif current_state[0] == 7 and current_state[1] in range(3,11) and action == 2:
		if randomizer <= (p1+p2):
			return current_state
		else:
			if randomizer <= ((1-p1-p2)/2):
				return move_up(current_state)
			else:
				return move_down(current_state)

	else:
		#print("here")
		if randomizer <= p1:
			return move(current_state, action)
		elif randomizer <= p2:
			return current_state
		else:

			#if randomizer <= (1-p1-p2)/2:
			return move_adjacent(current_state, action)



'''
Will move the agent to an adjacent position.
First checks if the agent is at any wall - as this will restrict the agent's movement to only one adjacent position.
'''
def move_adjacent(current_state, action):
	random_state = random.random()

	if action == 0:
		if current_state[0] == 3 and current_state[1] in range(0,9):
			return move_left(current_state)
		elif current_state[0] == 4 and current_state[1] in range(0,9):
			return move_right(current_state)
		elif current_state[0] == 6 and current_state[1] in range(3,11):
			return move_left(current_state)
		elif current_state[0] == 7 and current_state[1] in range(3,11):
			return move_left(current_state)
		elif current_state[0] == 10:
			return move_left(current_state)
		elif current_state[0] == 1:
			return move_right(current_state)
		else:
			if random_state <= 0.5:
				return move_left(current_state)
			else:
				return move_right(current_state)

	if action == 1:

		if current_state[0] == 3 and current_state[1] in range(0,9):
			return move_left(current_state)
		elif current_state[0] == 4 and current_state[1] in range(0,9):
			return move_right(current_state)
		elif current_state[0] == 6 and current_state[1] in range(3,11):
			return move_left(current_state)
		elif current_state[0] == 7 and current_state[1] in range(3,11):
			return move_left(current_state)
		elif current_state[0] == 10:
			return move_left(current_state)
		elif current_state[0] == 1:
			return move_right(current_state)
		else:
			if random_state <= 0.5:
				return move_left(current_state)
			else:
				return move_right(current_state)


	if action == 2:
		if current_state[1] == 1:
			return move_up(current_state)
		elif current_state[1] == 10:
			return move_down(current_state)
		else:
			if random_state<= 0.5:
				return move_up(current_state)
			else:
				return move_down(current_state)

	if action == 3:
		if current_state[1] == 1:
			return move_up(current_state)
		elif current_state[1] == 10:
			return move_down(current_state)
		else:
			if random_state<= 0.5:
				return move_up(current_state)
			else:
				return move_down(current_state)
'''
Gets the index of the state (which is the parameter)
'''
def state_get_index(current_state):
	for index in range(0, len(s)):
		list1 = [int(current_state[0]), int(current_state[1])]
		list2 = [int(s[index][0]), int(s[index][1])]
		if list1 == list2:
			return index

'''
Gets the optimal action at the specified state index and with the specified state action pair value by returning the action with the maximum value.
'''
def action_get_index(stateIndex, Q):
	optimal_action = None
	optimal_action = max(Q[stateIndex][:])
	for i in range(0, len(Q[stateIndex][:])):
		if optimal_action == Q[stateIndex][:][i]:
			return i
'''
Prints the policy with the specified Q
'''
def q_print_policy(Q):
	to_print = ""
	all_print = ""
	for i in range(10, 0, -1):
		for j in range(1, 11):
			state = state_get_index([j, i])

			action_to_check = action_get_index(state, Q)
			if action_to_check == 0:
				to_print += " ^ "

			elif action_to_check == 1:
				to_print += " v "

			elif action_to_check == 2:
				to_print += " < "

			else:
				to_print += " > "

			if j == 3:
				if i < 9:
					to_print += " | "
				else:
					to_print += "   "

			if j == 6:
				if i > 2:
					to_print += " | "
				else:
					to_print += "   "

			if j % 10 == 0:
				all_print += to_print
				all_print += "\n"

				to_print = ""
	all_print += to_print
	all_print += "\n"
	print(all_print)

'''
Prints the policy with the specified POL (policy)
'''
def mc_print_policy(POL):
	to_print = ""
	all_print = ""
	for i in range(10, 0, -1):
		for j in range(1, 11):
			state = state_get_index([j, i])

			action_to_check = POL[state]
			if action_to_check == 0:
				to_print += " ^ "

			elif action_to_check == 1:
				to_print += " v "

			elif action_to_check == 2:
				to_print += " < "

			else:
				to_print += " > "

			if j == 3:
				if i < 9:
					to_print += " | "
				else:
					to_print += "   "

			if j == 6:
				if i > 2:
					to_print += " | "
				else:
					to_print += "   "


			if j % 10 == 0:
				all_print += to_print
				all_print += "\n"



				to_print = ""
	all_print += to_print
	all_print += "\n"
	print(all_print)
