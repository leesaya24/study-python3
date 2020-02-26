
# coding: utf-8

# In[10]:


s = input('문자열을 입력하세요: ')
items = []
dic = {'(':')', '{':'}', '[':']'}        
for c in s:
    if c in dic:
        items.append(c)
    elif items==[] or dic[items.pop()] != c:
            print(False)

print(items==[])        


# In[ ]:




# In[ ]:




# In[ ]:



