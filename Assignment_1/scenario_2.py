import numpy as np
import pandas as pd
from pandas import Series, DataFrame

data = pd.read_excel(r"sgv.xlsx")

climate_january = data.loc[data["January"]==1, ["Year", "Temperature Evening LU", "Precipitation 5 days LU", "Fresh snow 5 days LU"]]
med_temp_jan = climate_january["Temperature Evening LU"].median()
mean_temp_jan = climate_january["Temperature Evening LU"].mean()
med_prec_jan = climate_january["Precipitation 5 days LU"].median()
mean_prec_jan = climate_january["Precipitation 5 days LU"].mean()
med_snow_jan = climate_january["Fresh snow 5 days LU"].median()
mean_snow_jan = climate_january["Fresh snow 5 days LU"].mean()

climate_february = data.loc[data["February"]==1, ["Year", "Temperature Evening LU", "Precipitation 5 days LU", "Fresh snow 5 days LU"]]
med_temp_feb = climate_february["Temperature Evening LU"].median()
mean_temp_feb = climate_february["Temperature Evening LU"].mean()
med_prec_feb = climate_february["Precipitation 5 days LU"].median()
mean_prec_feb = climate_february["Precipitation 5 days LU"].mean()
med_snow_feb = climate_february["Fresh snow 5 days LU"].median()
mean_snow_feb = climate_february["Fresh snow 5 days LU"].mean()

climate_march = data.loc[data["March"]==1, ["Year", "Temperature Evening LU", "Precipitation 5 days LU", "Fresh snow 5 days LU"]]
med_temp_mar = climate_march["Temperature Evening LU"].median()
mean_temp_mar = climate_march["Temperature Evening LU"].mean()
med_prec_mar = climate_march["Precipitation 5 days LU"].median()
mean_prec_mar = climate_march["Precipitation 5 days LU"].mean()
med_snow_mar = climate_march["Fresh snow 5 days LU"].median()
mean_snow_mar = climate_march["Fresh snow 5 days LU"].mean()

climate_april = data.loc[data["April"]==1, ["Year", "Temperature Evening LU", "Precipitation 5 days LU", "Fresh snow 5 days LU"]]
med_temp_apr = climate_april["Temperature Evening LU"].median()
mean_temp_apr = climate_april["Temperature Evening LU"].mean()
med_prec_apr = climate_april["Precipitation 5 days LU"].median()
mean_prec_apr = climate_april["Precipitation 5 days LU"].mean()
med_snow_apr = climate_april["Fresh snow 5 days LU"].median()
mean_snow_apr = climate_april["Fresh snow 5 days LU"].mean()

climate_may = data.loc[data["May"]==1, ["Year", "Temperature Evening LU", "Precipitation 5 days LU", "Fresh snow 5 days LU"]]
med_temp_may = climate_may["Temperature Evening LU"].median()
mean_temp_may = climate_may["Temperature Evening LU"].mean()
med_prec_may = climate_may["Precipitation 5 days LU"].median()
mean_prec_may = climate_may["Precipitation 5 days LU"].mean()
med_snow_may = climate_may["Fresh snow 5 days LU"].median()
mean_snow_may = climate_may["Fresh snow 5 days LU"].mean()

climate_june = data.loc[data["June"]==1, ["Year", "Temperature Evening LU", "Precipitation 5 days LU", "Fresh snow 5 days LU"]]
med_temp_jun = climate_june["Temperature Evening LU"].median()
mean_temp_jun = climate_june["Temperature Evening LU"].mean()
med_prec_jun = climate_june["Precipitation 5 days LU"].median()
mean_prec_jun = climate_june["Precipitation 5 days LU"].mean()
med_snow_jun = climate_june["Fresh snow 5 days LU"].median()
mean_snow_jun = climate_june["Fresh snow 5 days LU"].mean()

climate_july = data.loc[data["July"]==1, ["Year", "Temperature Evening LU", "Precipitation 5 days LU", "Fresh snow 5 days LU"]]
med_temp_jul = climate_july["Temperature Evening LU"].median()
mean_temp_jul = climate_july["Temperature Evening LU"].mean()
med_prec_jul = climate_july["Precipitation 5 days LU"].median()
mean_prec_jul = climate_july["Precipitation 5 days LU"].mean()
med_snow_jul = climate_july["Fresh snow 5 days LU"].median()
mean_snow_jul = climate_july["Fresh snow 5 days LU"].mean()

climate_august = data.loc[data["August"]==1, ["Year", "Temperature Evening LU", "Precipitation 5 days LU", "Fresh snow 5 days LU"]]
med_temp_aug = climate_august["Temperature Evening LU"].median()
mean_temp_aug = climate_august["Temperature Evening LU"].mean()
med_prec_aug = climate_august["Precipitation 5 days LU"].median()
mean_prec_aug = climate_august["Precipitation 5 days LU"].mean()
med_snow_aug = climate_august["Fresh snow 5 days LU"].median()
mean_snow_aug = climate_august["Fresh snow 5 days LU"].mean()

climate_september = data.loc[data["September"]==1, ["Year", "Temperature Evening LU", "Precipitation 5 days LU", "Fresh snow 5 days LU"]]
med_temp_sep = climate_september["Temperature Evening LU"].median()
mean_temp_sep = climate_september["Temperature Evening LU"].mean()
med_prec_sep = climate_september["Precipitation 5 days LU"].median()
mean_prec_sep = climate_september["Precipitation 5 days LU"].mean()
med_snow_sep = climate_september["Fresh snow 5 days LU"].median()
mean_snow_sep = climate_september["Fresh snow 5 days LU"].mean()

climate_october = data.loc[data["October"]==1, ["Year", "Temperature Evening LU", "Precipitation 5 days LU", "Fresh snow 5 days LU"]]
med_temp_oct = climate_october["Temperature Evening LU"].median()
mean_temp_oct = climate_october["Temperature Evening LU"].mean()
med_prec_oct = climate_october["Precipitation 5 days LU"].median()
mean_prec_oct = climate_october["Precipitation 5 days LU"].mean()
med_snow_oct = climate_october["Fresh snow 5 days LU"].median()
mean_snow_oct = climate_october["Fresh snow 5 days LU"].mean()

climate_november = data.loc[data["November"]==1, ["Year", "Temperature Evening LU", "Precipitation 5 days LU", "Fresh snow 5 days LU"]]
med_temp_nov = climate_november["Temperature Evening LU"].median()
mean_temp_nov = climate_november["Temperature Evening LU"].mean()
med_prec_nov = climate_november["Precipitation 5 days LU"].median()
mean_prec_nov = climate_november["Precipitation 5 days LU"].mean()
med_snow_nov = climate_november["Fresh snow 5 days LU"].median()
mean_snow_nov = climate_november["Fresh snow 5 days LU"].mean()

climate_december = data.loc[data["December"]==1, ["Year", "Temperature Evening LU", "Precipitation 5 days LU", "Fresh snow 5 days LU"]]
med_temp_dec = climate_december["Temperature Evening LU"].median()
mean_temp_dec = climate_december["Temperature Evening LU"].mean()
med_prec_dec = climate_december["Precipitation 5 days LU"].median()
mean_prec_dec = climate_december["Precipitation 5 days LU"].mean()
med_snow_dec = climate_december["Fresh snow 5 days LU"].median()
mean_snow_dec = climate_december["Fresh snow 5 days LU"].mean()

climate_overview = DataFrame({
                        "Temp mean" : ([mean_temp_jan, mean_temp_feb, mean_temp_mar, 
                                        mean_temp_apr, mean_temp_may, mean_temp_jun, 
                                        mean_temp_jul, mean_temp_aug, mean_temp_sep, 
                                        mean_temp_oct, mean_temp_nov, mean_temp_dec]),
                        "Temp med" : ([med_temp_jan, med_temp_feb, med_temp_mar, 
                                       med_temp_apr, med_temp_may, med_temp_jun, 
                                       med_temp_jul, med_temp_aug, med_temp_sep, 
                                       med_temp_oct, med_temp_nov, med_temp_dec]),
                        "Prec mean" : ([mean_prec_jan, mean_prec_feb, mean_prec_mar, 
                                        mean_prec_apr, mean_prec_may, mean_prec_jun, 
                                        mean_prec_jul, mean_prec_aug, mean_prec_sep, 
                                        mean_prec_oct, mean_prec_nov, mean_prec_dec]),
                        "Prec med" : ([med_prec_jan, med_prec_feb, med_prec_mar, 
                                       med_prec_apr, med_prec_may, med_prec_jun, 
                                       med_prec_jul, med_prec_aug, med_prec_sep, 
                                       med_prec_oct, med_prec_nov, med_prec_dec]),
                        "Snow mean" : ([mean_snow_jan, mean_snow_feb, mean_snow_mar, 
                                        mean_snow_apr, mean_snow_may, mean_snow_jun, 
                                        mean_snow_jul, mean_snow_aug, mean_snow_sep, 
                                        mean_snow_oct, mean_snow_nov, mean_snow_dec]),
                        "Snow med" : ([med_snow_jan, med_snow_feb, med_snow_mar, 
                                       med_snow_apr, med_snow_may, med_snow_jun, 
                                       med_snow_jul, med_snow_aug, med_snow_sep, 
                                       med_snow_oct, med_snow_nov, med_snow_dec])
                    }, index=["jan","feb","mar","apr","mai","jun","jul", "aug", "sep", 
                                "oct", "nov", "dec"])

print(climate_overview)