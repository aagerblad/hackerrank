first_input = input().split(" ")
second_input = input().split(" ")

initial_pile = int(first_input[0])
size_of_set = int(first_input[1])

s = []
for i in range(0,size_of_set):
	s.append(int(second_input[i]))

piles = [initial_pile]

current_player_one = True
game_over = False

while !game_over:

	for i in range(0,len(s)):
		for j in range(0,len(piles)):
			if piles[j] % s[i] == 0:
				
