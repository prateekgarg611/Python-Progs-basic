test_li=['Gfg','is','best','platform','for','Geeks']
print(test_li)
res=[sub.replace('G','-').replace('e','G').replace('-','e') for sub in test_li]
print(str(res))

string=''
for i in test_li:
    string+=str(i)+" "
print(string)
    
    
    

