


maze = []
row, col = input().split()
row = int(row); col = int(col)
for i in range(row):
    maze.append(input())
    if maze[-1].find("R"):
        R = i, maze[-1].find("R")
    if maze[-1].find("B"):
        B = i, maze[-1].find("B")

global count
count = 0

def solution(row, col, direction): #1: east, 2: west, 3: south, 4: north
    #red
    