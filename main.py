fullname = "anil beter"
capitalized_fullname = fullname.replace("a", "A").replace("b", "B")
print(capitalized_fullname)
# Anil Beter

experimentel_replace = capitalized_fullname.replace("e", "E")
print(experimentel_replace)
# Anil BEtEr

print("anil beter".replace("e", "E", 1))
# anil bEter
