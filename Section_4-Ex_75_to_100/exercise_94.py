# URL Cleaner

with open("urls.txt", 'r') as file:
    txt = file.readlines()
    #print(txt)

with open("urls.txt", 'w') as file:
    for line in txt:
        for_s = line.strip().replace("s", "", 1)+"\n"
        for_slash = for_s[:6] + "/" + for_s[6:]
        file.write(for_slash)

