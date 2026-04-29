import csv, json
'''
names1 = ["Ali", "Ahmed", "Sara", "Ayesha", "Usman", "Bilal", "Amna", "Zara"]
with open("names.txt", "w") as names:
    for i in names1[:5:]:     # can also use range for this for i in range(5): write(name[i] + "\n")
        names.write(i + "\n")

with open("names.txt", "r") as reads:
    for i in range(3):
        print(reads.readline().strip())
    reads.seek(0)
    lines = reads.readlines()
    print("number of lines : ", len(lines))

with open("names.txt", "a") as ap:
    for n in names1[5:9:]:
        ap.write(n + "\n")

with open("names.txt", "r") as r:
    l = r.readlines().strip()
    for i in range(len(l)):
        stipeed  = r.strip()
        i.startswith("A")
'''
with open("notes.txt", "r") as f: # line, word, character count
    print(f.read())
    f.seek(0)
    g = f.readlines()
    char_count = 0
    word_count = 0
    # print("line count", len(g))
    # f.seek(0)
    print("line count : ", len(g))
    for i in g:
        word = i.split()
        word_count += len(word)
        for n in word:
            char_count += len(n)

print("word count : ", word_count)                
print("char count : ", char_count)

# with open("notes.txt", "a") as append: # input appended data
    # add = input("enter : ").strip()
    # append.write("\n" + add)

with open("notes.txt", "r") as r:    # copy file content
    print(r.read())
    r.seek(0)
    with open("backup.txt", "w") as backup:
        backup.write(r.read())

with open("notes.txt", "r") as find:   # search for a specific word
    search = find.read().lower().split()
    if "python" in search:
        print("match found")
    else:
        print("not found")

# resume from here
with open("hehe.txt", "r") as mistakes:
    look = mistakes.read().lower().split()
    word_counts = 0
    w = set(look)
    for word in w:
        if word in look:
            word_counts += 1
    print(word, word_count)
    word_counts += 0
    
    print(word_counts)

# with open("hehe.txt", "r") as read:
#     with open("hehe.txt", "a") as replace:
#         reap = read.read().lower()
#         split = reap.split()
#         print(split)
#         if "python" in split:
#             replace.write("java")
with open("hehe.txt", "r") as red:
    r = red.read().lower()
    with open("hehe.txt", "w") as replace:
        new = r.replace("python", "java")
        replace.write(new)
        print(red)