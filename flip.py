def flip(section) -> str:
    lines = section.split("\n")

    section = []
    entry = []
    for line in lines:
        if line.startswith("-"):
            section.append("\n".join(entry))
            entry = [line]
        else:
            entry.append(line)
    
    section.reverse()
    return "\n".join(section)


with open("training.txt") as f:
    log = f.read()

log = log.split("\n\n")
log.reverse()

newlog = []
for section in log:
    if section.startswith("-"):
        section = flip(section)

    newlog.append(section)

print("\n\n".join(newlog))
