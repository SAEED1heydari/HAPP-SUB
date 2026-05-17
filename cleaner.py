import base64

good = []

with open("configs.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

for line in lines:

    line = line.strip()

    if line.startswith((
        "vless://",
        "vmess://",
        "trojan://",
        "ss://"
    )):
        good.append(line)

# حذف تکراری‌ها
good = list(dict.fromkeys(good))

# خروجی تمیز
with open("clean.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(good))

# خروجی base64 برای Happ
encoded = base64.b64encode(
    "\n".join(good).encode()
).decode()

with open("sub.txt", "w") as f:
    f.write(encoded)

print("Done")
