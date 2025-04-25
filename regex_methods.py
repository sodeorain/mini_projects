#%%
import re
quote = "The definition of madness. is doing the same thing over and over. and expecting a different. result"
re.search("over", quote)

#%%
re.findall("over", quote)
# %%
len(re.findall("over", quote))
# %%
re.split("\.", quote) # "." alone is a metacharacter
# %%
twisted_quote = re.sub("madness", "lunacy", quote) # can add a count = parameter to re.sub()
print(twisted_quote)
# %%
