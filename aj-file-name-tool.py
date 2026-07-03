#audiojungle file name editor

username = "celestialnostalgia"
wm = "watermark"
title = input("what is the title of this asset? ")
clean_title = "-".join(title.lower().split())

variations = int(input("how many variations do you want to create? "))

for number in range (1, variations +1):
    suffix = f"main-{number:02}_full"
    print(f"{username}_{clean_title}_{suffix}")

print(f"{username}_{clean_title}_{wm}")