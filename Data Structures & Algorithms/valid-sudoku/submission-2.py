class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowElems = [set() for _ in range(9)]
        colElems = [set() for _ in range(9)]
        boxElems = [set() for _ in range(9)]

        for i, row in enumerate(board): #rows from 0 to 8
            for j, num in enumerate(row):   #elems from 0 to 8 (vertically)
                if num != ".":
                    if(num not in rowElems[i]):
                        rowElems[i].add(num)
                    else:
                        return False

                    if(num not in colElems[j]):
                        colElems[j].add(num)
                    else:
                        return False
                    
                    if(num not in boxElems[(i//3)*3+(j//3)]):
                        boxElems[(i//3)*3+(j//3)].add(num)
                    else:
                        return False
        

        return True