class EqualPairs:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = []
        for row in grid:
            rows.append(",".join([str(x) for x in row]))

        cols = []
        for i in range(len(grid)):
            cols.append(",".join([str(row[i]) for row in grid]))

        pairs = 0
        for row in rows:
            for col in cols:
                pairs += (row==col)
        return pairs