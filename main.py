msg = "    anil             "
print(msg.strip())
# anil
msg_with_dots = "......anil........"
print(msg_with_dots.strip("."))
# anil
print(msg_with_dots.lstrip("."))
# anil........
print(msg_with_dots.rstrip("."))
# ......anil

number = "#4069850485"
number_without_hash = number.strip("#")
print(number_without_hash)
# 4069850485
