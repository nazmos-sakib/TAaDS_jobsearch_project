# main.py

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from typing import Optional
from pydantic import BaseModel
import pandas as pd
import your_python_script

df = pd.read_csv("file5.csv", sep=',')


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class SearchInput(BaseModel):
    query: str


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/search/")
async def search(query: SearchInput):
    # Call your Python script with the provided query
    print(query.query)
    #result = your_python_script.process_query(query.query)
    result = getJobList(query.query)
    return {"result": result}


def getJobList(keyword):
  jobs = []
  for index, row in df.iterrows():
    # Access row data using row['column_name']
    #print(row['Keyword'].split("/"))
    for str in row['Keyword'].split("/"):
      if keyword.lower() in str.lower():
        #jobs.append([row['Keyword'],row["Job Title"],row["Job Requirments"]])
        jobs.append(row)

  return jobs