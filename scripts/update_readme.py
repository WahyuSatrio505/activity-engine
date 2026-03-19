import random
import os
from datetime import datetime

now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

quotes = [
    "Consisten Diatas segalanyaa...",
    "Sedikit push,.",
    "Debugging adalah berpikir, bukan menebak..",
    "Pengalaman di atas segalanyaa"
]

status_list = ["building", "testing", "improving", "refactoring"]

quote = random.choice(quotes)
status = random.choice(status_list)
unique_id = random.randint(1000, 999999)


readme_content = f"""
# 🚀 Wahyu Dev Activity

## Last Update
{now}

## Status
{status}

## Dev Quote
{quote}

## Update ID
{unique_id}
"""

with open("README.md", "w") as f:
    f.write(readme_content)


os.makedirs("data", exist_ok=True)

with open("data/log.md", "a") as f:
    f.write(f"\n{now} - Status: {status} - ID: {unique_id}")


chance = random.randint(1, 3)

if chance == 1:
    filename = f"data/dev_note_{unique_id}.md"
    
    content = f"""
## Dev Note

Time: {now}
Status: {status}

Thought:
Today I explored automation and system behavior.
"""
    with open(filename, "w") as f:
        f.write(content)
