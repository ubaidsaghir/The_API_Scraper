import pandas as pd
import requests
from datetime import datetime

url = "https://disease.sh/v3/covid-19/countries"

params = {
    "yesterday": "false",  
    "sort": "cases"         
}


response = requests.get(url, params=params)
data = response.json()


df = pd.DataFrame(data)

df = df[
    [
        "country",
        "cases",
        "todayCases",
        "deaths",
        "todayDeaths",
        "recovered",
        "active"
    ]
]

df_top20 = df.sort_values(by="cases", ascending=False).head(20)

df_top20.rename(
    columns={
        "country": "country_name",
        "cases": "total_cases",
        "todayCases": "new_cases",
        "deaths": "total_deaths",
        "todayDeaths": "new_deaths",
        "recovered": "total_recovered",
        "active": "active_cases"
    },
    inplace=True
)

df_top20["timestamp"] = datetime.now()

df_top20.fillna("NA", inplace=True)


filename = "api_scrper2.csv"
df_top20.to_csv(filename, index=False)

print(df_top20)
print("File saved:", filename)
