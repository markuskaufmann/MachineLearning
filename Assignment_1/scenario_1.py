import numpy as np
import pandas as pd
from pandas import Series, DataFrame

data = pd.read_excel(r"sgv.xlsx")

passengers_january = data.loc[(data["January"]==1) & (data["Revisions (no ships in use)"]==0), ["Passengers", "Year"]]
med_jan = passengers_january["Passengers"].median()
mean_jan = passengers_january["Passengers"].mean()

passengers_february = data.loc[(data["February"]==1) & (data["Revisions (no ships in use)"]==0), ["Passengers", "Year"]]
med_feb = passengers_february["Passengers"].median()
mean_feb = passengers_february["Passengers"].mean()

passengers_march = data.loc[(data["March"]==1) & (data["Revisions (no ships in use)"]==0), ["Passengers", "Year"]]
med_mar = passengers_march["Passengers"].median()
mean_mar = passengers_march["Passengers"].mean()

passengers_april = data.loc[(data["April"]==1) & (data["Revisions (no ships in use)"]==0), ["Passengers", "Year"]]
med_apr = passengers_april["Passengers"].median()
mean_apr = passengers_april["Passengers"].mean()

passengers_may = data.loc[(data["May"]==1) & (data["Revisions (no ships in use)"]==0), ["Passengers", "Year"]]
med_may = passengers_may["Passengers"].median()
mean_may = passengers_may["Passengers"].mean()

passengers_june = data.loc[(data["June"]==1) & (data["Revisions (no ships in use)"]==0), ["Passengers", "Year"]]
med_june = passengers_june["Passengers"].median()
mean_june = passengers_june["Passengers"].mean()

passengers_july = data.loc[(data["July"]==1) & (data["Revisions (no ships in use)"]==0), ["Passengers", "Year"]]
med_july = passengers_july["Passengers"].median()
mean_july = passengers_july["Passengers"].mean()

passengers_august = data.loc[(data["August"]==1) & (data["Revisions (no ships in use)"]==0), ["Passengers", "Year"]]
med_august = passengers_august["Passengers"].median()
mean_august = passengers_august["Passengers"].mean()

passengers_september = data.loc[(data["September"]==1) & (data["Revisions (no ships in use)"]==0), ["Passengers", "Year"]]
med_september = passengers_september["Passengers"].median()
mean_september = passengers_september["Passengers"].mean()

passengers_october = data.loc[(data["October"]==1) & (data["Revisions (no ships in use)"]==0), ["Passengers", "Year"]]
med_october = passengers_october["Passengers"].median()
mean_october = passengers_october["Passengers"].mean()

passengers_november = data.loc[(data["November"]==1) & (data["Revisions (no ships in use)"]==0), ["Passengers", "Year"]]
med_november = passengers_november["Passengers"].median()
mean_november = passengers_november["Passengers"].mean()

passengers_december = data.loc[(data["December"]==1) & (data["Revisions (no ships in use)"]==0), ["Passengers", "Year"]]
med_december = passengers_december["Passengers"].median()
mean_december = passengers_december["Passengers"].mean()

array_mean = Series([mean_jan, mean_feb, mean_mar, mean_apr, mean_may, mean_june, 
                    mean_july, mean_august, mean_september, mean_october, 
                    mean_november, mean_december],
                    index=["jan","feb","mar","apr","mai","jun","jul", "aug", "sep", "oct", 
                           "nov", "dec"])
array_med = Series([med_jan, med_feb, med_mar, med_apr, med_may, med_june, 
                    med_july, med_august, med_september, med_october, 
                    med_november, med_december],
                    index=["jan","feb","mar","apr","mai","jun","jul", "aug", "sep", "oct", 
                           "nov", "dec"])

print("\nDurchschnitt pro Monat:")
print(array_mean)
print("\nMedian pro Monat:")
print(array_med)
print("\nMinimaler Durchschnitt:")
print(array_mean.loc[array_mean == array_mean.min()])
print("\nMinimaler Median:")
print(array_med.loc[array_med == array_med.min()])
