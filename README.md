
# City DNA - GSS 2021

# to run the Python script

## Requirements
- [Python 3](https://www.python.org/downloads/)(ideally 3.6 or 3.7)
- [git](https://www.atlassian.com/git/tutorials/install-git)


## Installation
1. **[clone the repository](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)**
  - download the repository and unzip
  - open a Terminal (mac) or run PowerShell (win)
  - change directory to access the repository `example: cd /Users/xxx/Desktop/city-dna`
2. **[virtual environment](https://docs.python.org/3/tutorial/venv.html)**
  - with only Python3 installed `python -m venv env`
  - if Python2 and Python3 installed `python3 -m venv env`
  -  mac: `source /env/bin/activate`
  -  win: `.\env\Scripts\activate`
3. **install dependencies**
  - `pip install -r requirements.txt`

## Usage
- Change directory in the Terminal/PowerShell to repository folder
- Activate your virtual environment (as explained above)

## Troubleshooting
- if `.\env\Scripts\activate` fails to run in Windows
  - make sure you run Powershell as Administrator 
  - `Set-ExecutionPolicy RemoteSigned`
  - `y`
  - `.\env\Scripts\activate`
