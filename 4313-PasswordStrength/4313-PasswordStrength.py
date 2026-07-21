# Last updated: 22/07/2026, 04:23:41
class Solution:
    def passwordStrength(self, password: str) -> int:
        stre=0
        seen=set()

        for i in password:
            if i in seen:
                continue
            seen.add(i)
            if i.islower():
                stre+=1
            elif i.isupper():
                stre+=2
            elif i.isdigit():
                stre+=3
            elif i in "!@#$":
                stre+=5

        return stre