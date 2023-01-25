from Stack import Stack

def printMaze(maze):
	for row in range(len(maze)):
		for col in range(len(maze[0])):
			print("|{:<2}".format(maze[row][col]), sep='',end='')
		print("|")
	return

def solveMaze(maze, startX, startY):
    """
    The maze parameter will be the 2D List maze as described above.
    startX and startY are the starting coordinates used when traversing
    the maze (maze[startX][startY]).

    The solveMaze function will utilize a Stack and update the maze elements
    with the number of steps at each traversed position. It should return
    True if a path exists and the goal was reached, and return False if no
    path to the goal exists.
    """
    #initializing
    player = Stack()
    count = 1
    player.push([startX, startY])
    maze[player.peek()[0]][player.peek()[1]] = count
    count += 1

    #sequence

    while player.isEmpty() == False:
        try:
            maze[player.peek()[0]][player.peek()[1]]
        except IndexError:
            #print("Maze empty")
            return False
        # if maze[player.peek()[0]][player.peek()[1]] == 'G':
        #     print("wtf it worked")
        #     return True

        try:
            # checking north
            if maze[player.peek()[0] - 1][player.peek()[1]] == 'G':
                #print("wtf it worked")
                return True
            elif maze[player.peek()[0]-1][player.peek()[1]] == ' ':
                maze[player.peek()[0] - 1][player.peek()[1]] = count
                count += 1
                player.push([player.peek()[0]-1, player.peek()[1]])
                #print('north')
            #checking west
            elif maze[player.peek()[0]][player.peek()[1]-1] == 'G':
                #print("wtf it worked")
                return True
            elif maze[player.peek()[0]][player.peek()[1]-1] == ' ':
                maze[player.peek()[0]][player.peek()[1] - 1] = count
                count += 1
                player.push([player.peek()[0], player.peek()[1]-1])
                #print('west')
            #checking south
            elif maze[player.peek()[0]+1][player.peek()[1]] == 'G':
                #print("wtf it worked")
                return True
            elif maze[player.peek()[0]+1][player.peek()[1]] == ' ':
                maze[player.peek()[0]+1][player.peek()[1]] = count
                count += 1
                player.push([player.peek()[0]+1, player.peek()[1]])
                #print('south')
            #checking east
            elif maze[player.peek()[0]][player.peek()[1]+1] == 'G':
                #print("wtf it worked")
                return True
            elif maze[player.peek()[0]][player.peek()[1]+1] == ' ':
                maze[player.peek()[0]][player.peek()[1] + 1] = count
                count += 1
                player.push([player.peek()[0], player.peek()[1]+1])
                #print('east')
            #if nowhere to go, then pop and go back to previous place
            else:
                #maze[player.peek()[0] - 1][player.peek()[1]] = count
                #count += 1
                player.pop()
            # printMaze(maze)
            # print('\n')
        except Exception:
            #print('not valid position')
            continue
    #print('this bitch failed')
    return False






# maze = [[],[],[]]
#
# maze = [
# ['+','+','+','+','G','+'],
# ['+',' ','+',' ',' ','+'],
# ['+',' ',' ',' ','+','+'],
# ['+',' ','+','+',' ','+'],
# ['+',' ',' ',' ',' ','+'],
# ['+','+','+','+','+','+'] ]

# maze = [
#     ['+', '+', '+', '+', '+', '+'],
#     ['+', ' ', ' ', ' ', ' ', '+'],
#     ['+', ' ', ' ', 'G', ' ', '+'],
#     ['+', ' ', ' ', ' ', ' ', '+'],
#     ['+', ' ', ' ', ' ', ' ', '+'],
#     ['+', '+', '+', '+', '+', '+']]

# maze = [
#     ['+', '+', '+', '+', '+', '+', '+'],
#     ['+', ' ', ' ', ' ', ' ', 'G', '+'],
#     ['+', '+', '+', '+', '+', '+', '+']]
#
# print(solveMaze(maze, 0, 1))
#
# print(solveMaze(maze, 4, 4))

# maze = [
#         ['+', '+', '+', '+', '+', '+'],
#         ['+', '+', '+', '+', ' ', '+'],
#         ['+', '+', '+', '+', ' ', '+'],
#         ['+', '+', '+', '+', ' ', '+'],
#         ['+', 'G', ' ', ' ', ' ', '+'],
#         ['+', '+', '+', '+', '+', '+']]
#
# solveMaze(maze, 4, 4)