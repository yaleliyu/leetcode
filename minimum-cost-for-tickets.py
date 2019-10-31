class Solution:
    def __init__(self):
        self.minCosts = []

    def nextWindowStart(self, days, start, window_width):
        if start >= len(days):
            return len(days)

        end_day = days[start] + window_width - 1
        next_start_idx = start
        for idx, day in enumerate(days[start:]):
            if day > end_day:
                next_start_idx += idx
                break

        return next_start_idx if next_start_idx > start else len(days)

    def mincostTicketsImpl(self, days, costs, start) -> int:
        if start >= len(days):
            return 0

        if self.minCosts[start] > 0:
            return self.minCosts[start]

        cost_1 = costs[0] + self.mincostTicketsImpl(days, costs, start+1)

        if len(costs) < 2:
            self.minCosts[start] = cost_1
            return self.minCosts[start]

        start_after_7 = self.nextWindowStart(days, start, 7)
        if start_after_7 >= len(days):
            cost_7 = min([costs[1], costs[0]*(len(days)-start)])
        else:
            cost_7 = costs[1] + self.mincostTicketsImpl(days, costs, start_after_7)

        if len(costs) < 3:
            self.minCosts[start] = min(cost_1, cost_7)
            return self.minCosts[start]

        start_after_30 = self.nextWindowStart(days, start, 30)
        if start_after_30 >= len(days):
            cost_30 = min(costs[2], self.mincostTicketsImpl(days, costs[:-1], start))
        else:
            cost_30 = costs[2] + self.mincostTicketsImpl(days, costs, start_after_30)

        self.minCosts[start] = min([cost_1, cost_7, cost_30])
        return self.minCosts[start]


    def mincostTickets(self, days, costs) -> int:
        self.minCosts = [-1] * len(days)

        return self.mincostTicketsImpl(days, costs, 0)



sln = Solution()

print(sln.mincostTickets([1,4,6,7,8,20], [2,7,15]))
print(sln.mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31],[2,7,15]))
