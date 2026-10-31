RAM = [None] * 4  # 4 slots, each slot = 1 GB


def show(title):
    print(f"{title:<28}", [s if s else "free" for s in RAM])


def alloc_contiguous(name, size):
    """The program needs ONE continuous block."""

    for start in range(len(RAM) - size + 1):
        if all(RAM[i] is None for i in range(start, start + size)):
            for i in range(start, start + size):
                RAM[i] = name
            return True

    return False


def alloc_paged(name, size):
    """Use ANY free slots; a map remembers where they are."""

    free_slots = [i for i, s in enumerate(RAM) if s is None]

    if len(free_slots) < size:
        return False

    for i in free_slots[:size]:
        RAM[i] = name

    return True


def quit_program(name):
    for i, s in enumerate(RAM):
        if s == name:
            RAM[i] = None


# ==========================================
# PART A: CONTIGUOUS ALLOCATION
# ==========================================

print("--- Part A: contiguous allocation (no virtual memory) ---")

alloc_contiguous("P1", 1)
alloc_contiguous("P2", 2)

show("P1 (1GB) and P2 (2GB) run:")

quit_program("P1")
show("P1 quits:")

ok = alloc_contiguous("P3", 2)

print("Can P3 (2GB) start?", ok)
show("RAM now:")

print()


# ==========================================
# PART B: PAGING (VIRTUAL MEMORY)
# ==========================================

print("--- Part B: paging (virtual memory) ---")

RAM = [None] * 4

alloc_paged("P1", 1)
alloc_paged("P2", 2)

quit_program("P1")
show("P1 quits:")

ok = alloc_paged("P3", 2)

print("Can P3 (2GB) start?", ok)
show("RAM now:")