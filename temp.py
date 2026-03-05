from pathlib import Path
lines=Path('sections/main-page.liquid').read_text().splitlines()
for idx,line in enumerate(lines,1):
    if idx>=1465 and idx<=1495:
        print(f"{idx}: {line}")
