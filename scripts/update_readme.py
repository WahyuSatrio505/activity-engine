import random
from datetime import datetime

quotes = [
"Code is like humor. When you have to explain it, it’s bad.",
"Programs must be written for people to read.",
"Simplicity is the soul of efficiency.",
"First, solve the problem. Then, write the code.",
"Experience is the name everyone gives to their mistakes."
]

quote = random.choice(quotes)
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

readme_content = f"""
# Wahyu's GitHub Activity Engine 🚀

Automation project that updates this README every day.

## Last Update
{now}

## Random Dev Quote
"{quote}"

## Daily Log
See data/log.md
"""

with open("README.md", "w") as f:
    f.write(readme_content)

with open("data/log.md", "a") as f:
    f.write(f"\n{now} - Updated README automatically.")
