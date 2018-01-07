# /usr/bin/env python3
#  Filename :Integral.py
#  author_by hao yi


#输入要积分的函数
print("Please input the equation that you want to integrate   ")
equation = input("equation:")

class Integral:
    '''usage:
             In[1]:Integral ("math.sin(x)+x ** 2",0,10)()
             Out[1]4999.99xx
    '''
    def _init_(self,start,end,default_step,result,x):
        start=0
        end=10
        default_step=0.0000000001
        return result

        self.equation=equation
        self.start=start
        self.end=end
        self.default_step=default_step                      
        self,result=result
        self.x=x
    try:
        eval(equation.replace('x','123'))
    except SyntaxError:#equation not valid
        print ("Unsupported expression!")

ch = 0.00000001
default_step = 0.0000000001
n=1
result = 0
for n in range(10000000000):#分成10000000000份
    result+=eval(equation.replace('x','ch'))* default_step
    ch = ch * n
print(result)





