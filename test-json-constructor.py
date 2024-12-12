def parse(input: str) -> list[str]:
    return input.split("\n")


def convert(lines: list[str], curLine=0, parentLevel=-1):
    n = len(lines)


    def dfs(lines, visited, ans, i):
        if i + 1 == n:
            return
        
        if i in visited:
            return
        
        visited.add(i)

        curLine = lines[i].strip()
        pair = curLine.split(":")
        if pair[1]:
            value = dfs(lines, )
        else:
            value = pair[1]
        
        return {pair[0]: value}


    visited = set()
    ans = {}
    for i in range(n):
        print(i)


    return ans

input = \
"""K1:V1
K2:V2
K3:
  K31:V31
  K32:
    K321:V321
    K322:V322
  K33:V33
K4:
  K41:V41
  K42:V42"""

print(input)
# lines = parse(input)
# record, finalIndex = convert(lines)
# print(record)
# print(finalIndex, len(lines))