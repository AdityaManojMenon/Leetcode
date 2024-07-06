class Solution:
    def calPoints(self, operations: List[str]) -> int:
        new_record = []
        for i in operations:
            if i == "C":
                new_record.pop()
            elif i == "D":
                new_record.append(new_record[-1]*2)
            elif i == "+":
                new_record.append(new_record[-1]+new_record[-2])
            else:
                new_record.append(int(i))
        
        total = 0
        for scores in new_record:
            total+=scores
        return total
        