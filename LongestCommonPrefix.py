class Solution():
    def longestCommonPrefix(self, strs):
        pattern = ""
        
        shortest = len(min(strs, key=len))
        # print(shortest)
        # print(len(strs))
        # print(strs, strs[2][0:3])

        if len(strs) == 1:
            pattern = strs[0]
        elif len(strs) == 2:
            
            for j in range(shortest):
                if strs[0][j] == strs[1][j]:
                    pattern += strs[0][j]
                else:
                    break
        else:
            
            for j in range(shortest):
                for i in range(len(strs) - 1):
                    if strs[i][j] != strs[i + 1][j]:
                        break  
                else:
                    
                    pattern += strs[0][j]
                    continue
                break

        return pattern

sol = Solution()

if __name__ == "__main__":
    sol = Solution()
