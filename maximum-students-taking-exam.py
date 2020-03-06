# https://leetcode.com/problems/maximum-students-taking-exam/

# If a seat is broken, it is denoted by '#' character otherwise it is denoted by a '.' character.
# Input: seats = [["#",".","#","#",".","#"],
#                [".","#","#","#","#","."],
#                ["#",".","#","#",".","#"]]
# Output: 4
# Explanation: Teacher can place 4 students in available seats so they don't cheat on the exam.

class Solution:
    def __init__(self):
        self.student = 'H'
        self.max = 0
        self.available_seats = []
        self.width = 0
        self.depth = 0

    def is_available(self, seats, row, col):
        available = True

        if seats[row][col] != '#':
            right_fulfilled = col<self.width-1 and seats[row][col+1] == self.student
            left_fulfilled = col > 0 and seats[row][col-1] == self.student

            left_behind = row>0 and col>0 and seats[row-1][col-1] == self.student
            left_ahead = row<self.depth-1 and col>0 and seats[row+1][col-1]==self.student
            right_ahead = row<self.depth-1 and col<self.width-1 and seats[row+1][col+1]==self.student
            right_behind = row>0 and col<self.width-1 and seats[row-1][col+1]==self.student

            if right_fulfilled or left_fulfilled or left_behind or left_ahead or right_ahead or right_behind:
                available = False
        else:
            available = False

        return available

    def calculate(self, seats):
        _buf_ = [[1 if c==self.student else 0 for c in r] for r in seats]
        count = sum([sum(r) for r in _buf_])

        return count

    def maxSudentsImpl(self, seats, idx):
        if idx >= len(self.available_seats):
            count = self.calculate(seats)
            self.max = self.max if self.max > count else count
            return count

        empty_count = self.maxSudentsImpl(seats, idx+1)
        fulfill_count = 0

        row = self.available_seats[idx][0]
        col = self.available_seats[idx][1]
        if self.is_available(seats, row, col):
            seats[row][col] = self.student
            fulfill_count = self.maxSudentsImpl(seats, idx+1)
            seats[row][col] = '.'

        return max(empty_count, fulfill_count)


    def maxStudents(self, seats) -> int:
        self.width = len(seats[0])
        self.depth = len(seats)

        for idx_x, row in enumerate(seats):
            for idx_y, col in enumerate(row):
                if seats[idx_x][idx_y] == '.':
                    self.available_seats.append([idx_x, idx_y])

        return self.maxSudentsImpl(seats, 0)

seats = [["#",".","#","#",".","#"], [".","#","#","#","#","."], ["#",".","#","#",".","#"]]
seats = [[".","#"],["#","#"], ["#","."], ["#","#"], [".","#"]]
seats = [["#",".",".",".","#"], [".","#",".","#","."],[".",".","#",".","."],[".","#",".","#","."],["#",".",".",".","#"]]
seats = [[".",".",".",".","#",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".","#","."],[".",".",".",".",".",".",".","."],[".",".","#",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","#",".",".","#","."]]
sln = Solution()

print(sln.maxStudents(seats))
