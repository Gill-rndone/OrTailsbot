# OrTailsbot

### REQUIREMENTS:
- Python 3.10+
- pip 
- sqlite3
- basic discord intent setup (read/write messages, etc.) 

### SETUP:
##### In project folder
1. Create a venv file (for linux machines: `python -m venv venv`)
2. Run the venv file with `source venv/bin/activate`
4. Create a .env file and input `DISCORD_TOKEN=<token>`
5. Lastly run `pip install -r requrements.txt` to install the requirements and run with `python3 main.py`

## ***COMMANDS***
- `f!flip` Flips a coin!
- `f!local_history` Returns the last five flips, total flips, and total flip percentages from current server. 
- `f!global_history` Returns the last five flips, total flips, and total flip percentages from all servers. 
