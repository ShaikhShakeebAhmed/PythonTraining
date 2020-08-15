import pandas
import os
# do pip3 install pandas

def usePandas():
  if os.path.exists("Additionalfiles/temps_today.csv") :
    data = pandas.read_csv("Additionalfiles/temps_today.csv")
    print(data.mean())

usePandas()