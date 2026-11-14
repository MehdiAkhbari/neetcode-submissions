class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for string in strs:
            l = str(len(string))
            out += l
            out += "#"
            out += string
        print(out)
        return out


    def decode(self, s: str) -> List[str]:
        out = []
        while(s != ""):
            i = 0
            while s[i] != "#":
                i +=1

            l = int(s[0:i])
            word = s[i+1: i+l+1]
            out.append(word)
            s = s[i+l+1: ]
        print(out)
        return out





            
        
