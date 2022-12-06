import os
from datetime import datetime
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup as Soup

load_dotenv()

def start_puzzle(day=0,year=0,dir='.'):
    print(os.getcwd())
    if day ==0:
        day= datetime.today().day
    if year==0:
        year=datetime.today().year
    if f"day{day}_input" not in os.listdir():
        #print(f"{dir}/day{day}_input")
        with open(f"{dir}/day{day}_input","w") as file:
            ch={"session":os.getenv("ID")}
            #print(ch)
            r=requests.get(f"https://adventofcode.com/{year}/day/{day}/input",cookies=ch)
            file.write(r.text)
    file=open(f"{dir}/day{day}_input","r")
    lines=file.readlines()
    file.close()
    return list(map(lambda x: x.rstrip(),lines))


    
