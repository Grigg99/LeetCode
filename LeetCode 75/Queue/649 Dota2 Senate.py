class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        # if len(senate) == (1 or 2):
        #     if senate[0] == "R":
        #         return "Radiant"
        #     else:
        #         return "Dire"

        i = 1
        j = 0
        voters = []
        voters.append(senate[0])

        while len(set(senate)) > 1:

            if len(senate) == (1 or 2):
                if senate[0] == "R":
                    return "Radiant"
                else:
                    return "Dire"

            if j == len(voters):
                if voters[-1] != senate[i]:
                    voters.append(senate[i])
                    # if voters[0] != senate[i]:
                    if i == len(senate)-1:
                        if voters[0] != senate[i]:
                            voters.pop(0)
                        else:
                            voters.pop(voters.index("R" if voters[-1] == "D" else "D"))

                        
                    # j = len(voters) - 1
                else:
                    voters.append(senate[i])

            elif voters[j] != senate[i]:
                # voters.pop(0)
                j += 1
            else:
                voters.append(senate[i])

            # print(voters, i, j)

            i += 1

            if i == len(senate):
                while len(voters) - j > 0:
                    if ("R" if voters[-1] == "D" else "D") in voters:
                        voters.pop(voters.index("R" if voters[-1] == "D" else "D"))
                    else:
                        if voters[-1] == "R":
                            return "Radiant"
                        else:
                            return "Dire"
                    # j += 1
                    # print(voters)
                i = 1
                j = 0
                senate = voters
                voters = []
                voters.append(senate[0])


        # print(voters, j)

        if senate[0] == "R":
            return "Radiant"
        else:
            return "Dire"
        
