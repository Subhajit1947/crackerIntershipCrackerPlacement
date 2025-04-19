class Solution:
    def intToRoman(self, num: int) -> str:
        d={1:"I",2:"V",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",
        90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"
        } 
        ans=''
        if num>=1000:
            a=num//1000
            ans+=d[1000]*a
            num=num%1000
        if num>=900:
            a=num//900
            ans+=d[900]*a
            num=num%900
        if num>=500:
            a=num//500
            ans+=d[500]*a
            num=num%500
        if num>=400:
            a=num//400
            ans+=d[400]*a
            num=num%400
        if num>=100:
            a=num//100
            ans+=d[100]*a
            num=num%100
        if num>=90:
            a=num//90
            ans+=d[90]*a
            num=num%90
        if num>=50:
            a=num//50
            ans+=d[50]*a
            num=num%50
        if num>=40:
            a=num//40
            ans+=d[40]*a
            num=num%40
        if num>=10:
            a=num//10
            ans+=d[10]*a
            num=num%10
        if num>=9:
            a=num//9
            ans+=d[9]*a
            num=num%9
        if num>=5:
            a=num//5
            ans+=d[5]*a
            num=num%5
        if num>=4:
            a=num//4
            ans+=d[4]*a
            num=num%4
        if num>=1:
            a=num//1
            ans+=d[1]*a
            num=num%1
        return ans

