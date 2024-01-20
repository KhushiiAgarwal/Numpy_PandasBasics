import numpy as np
import pandas as pd
s1=pd.Series(7, index=['a','b','c','d','e'])
x=[10,20,5,19,4]
s2=pd.Series(x, index=['a','b','c','d','e'])
print(s1,s2)
print('Boolean expression')
print('s1>s2')
print(s1>s2)
print('s1<s2')
print(s1<s2)
print('s1=s2')
print(s1==s2)
