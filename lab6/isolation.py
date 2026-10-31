
print("=== Without virtual memory ===")

ram = {}

# Program 1 stores bank balance at address 1024
ram[1024] = 4700
print("Program 1 saved balance:", ram[1024])

# Program 2 also uses address 1024
ram[1024] = 80210000
print("Program 1 reads again :", ram[1024], " <-- data corrupted!")


print()


# ==========================================
# WITH VIRTUAL MEMORY
# ==========================================

print("=== With virtual memory ===")

ram = {}

# Virtual address -> Physical RAM address
map1 = {1024: 1}  # Program 1: virtual 1024 -> RAM address 1
map2 = {1024: 5}  # Program 2: virtual 1024 -> RAM address 5


def write(mapping, va, value):
    ram[mapping[va]] = value


def read(mapping, va):
    return ram[mapping[va]]


# Each program writes to its own physical location
write(map1, 1024, 4700)
write(map2, 1024, 80210000)

print("Program 1 reads address 1024:", read(map1, 1024))
print("Program 2 reads address 1024:", read(map2, 1024))
print("Real RAM content :", ram)


print()


# ==========================================
# SHARING ON PURPOSE
# ==========================================

print("=== Sharing on purpose ===")

# Both programs map their virtual addresses to RAM address 9
map1[2048] = 9
map2[3000] = 9

write(map1, 2048, "hello from program 1")

print("Program 2 reads shared data :", read(map2, 3000))
