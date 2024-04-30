class Solution:
    def intToRoman(self, num: int) -> str:
        num_list = [int(x) for x in str(num)][::-1]
        num_str = ""
        base = ""
        middle = ""
        nextS = ""
        s = ""
        
        for i in range(len(num_list)):
            s = ""
            if i == 0:
                base = "I"
                middle = "V"
                nextS = "X"  
            if i==1:
                base = "X"
                middle = "L"
                nextS = "C"  
            if i==2:
                base = "C"
                middle = "D"
                nextS = "M"  
            if i==3:
                base = "M"
                middle = "V̅"
                nextS = "X̅"  
            if num_list[i] < 4:
                for _ in range(num_list[i]):
                    s += base
            elif num_list[i] == 4:
                s =base+middle
            if num_list[i] == 5:
                s = middle
            if num_list[i] > 5 and num_list[i] < 9:
                s = middle
                for _ in range(num_list[i]-5):
                    s+=base
            elif num_list[i] == 9:
                s = base+nextS
            num_str = s + num_str
        return num_str

        