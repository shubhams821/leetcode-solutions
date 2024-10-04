class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill = sorted(skill)

        l,r =0,len(skill)-1
        chem = 0
        res = skill[l]+skill[r] if skill else 0
        while l<r:
            check = skill[l] + skill[r]
            if res!= check:
                return -1
            chem += skill[l]*skill[r]
            l+=1
            r-=1
        return chem