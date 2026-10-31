bits = int(input("Address size in bits (e.g. 16, 32, 64): "))
addresses = 2 ** bits
print(f"A {bits}-bit address space has {addresses:,} addresses")
print(f"With 1 byte per address that is {addresses / 1024**3:,.4f} GB")

ram_gb = float(input("Installed RAM in GB: "))
if ram_gb * 1024**3 < addresses:
    print("RAM is smaller than the address space -> some addresses do not exist!")
else:
    print("RAM covers the whole address space.")
