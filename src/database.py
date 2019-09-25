import config
import requests
import re
import pandas as pd


request_result = requests.get("http://messier.obspm.fr/data1.html")
pattern  = r">([0-9\?\.]+)\s+(Win4|[&gt;I\-0-9\.\s]+)\s([a-zA-Z]+)\s+([0-9ABC]+)\s+([0-9\.]+)\s([0-9\.]+)\s([\+\-0-9\.]+)\s([0-9]+)\s+([0-9\.]+)\s+([0-9\.x]+)\s+([0-9\.]+)\s"
re_result = re.findall(pattern, request_result.content.decode('utf-8'))

data = pd.DataFrame(data=re_result, columns=["M#", "NGC#", "Constellation", "Type",
                                            "Right_Ascention_h", "Right_Ascention_min",
                                            "Declination_deg", "Declination_min",
                                            "Aparent_Magnitude", "Aparant_Diameter", "distance_kLightYear"])
data.drop("NGC#", axis=1, inplace=True)

data.loc[data["M#"] == "102?", "M#"] = "102"

data["M#"] = data["M#"].apply(lambda x: "M"+str(int(x)))

categories = {"1":"Open Cluster",
            "2":"Globular Cluster",
            "3":"Planetary Nebula",
            "4":"Starforming Nebula (with open cluster)",
            "5":"Spiral Galaxy",
            "6":"Elliptical Galaxy",
            "7":"Irregular Galaxy",
            "8":"Lenticular (S0) Galaxy",
            "9":"Supernova Remnant",
            "A":"System of 4 stars or Asterism",
            "B":"Milky Way Patch",
            "C":"Binary star"}

data['Type'] = data['Type'].map(categories).astype('category')


coordinates = ["Right_Ascention_h", "Right_Ascention_min","Declination_deg", "Declination_min"]
for col in coordinates:
    data[col] = data[col].astype('float')
data['RA_h'] = data['Right_Ascention_h'] + data['Right_Ascention_min']/60
data['DEC_deg'] = data['Declination_deg'] + data['Declination_min']/60
data.drop(coordinates, axis=1, inplace=True)


data.to_pickle(config.PIKLE_FILE)
