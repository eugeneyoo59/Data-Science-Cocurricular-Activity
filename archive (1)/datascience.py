import pandas # for loading csv
import matplotlib.pyplot as plt # for graph
import plotly.express as px # for better looking graph


data1 = pandas.read_csv("russia_losses_personnel.csv")
data2 = pandas.read_csv("russia_losses_equipment.csv")


print (data1.info())
print (data2.info())


#fig = px.line(data2, x = "date", y = ["aircraft", "tank", "drone", "helicopter", "naval ship", "fuel tank"])
#fig.write_image("figure1_line.png")

names = ["aircraft", "tank", "drone", "helicopter", "naval ship", "fuel tank"]
values = [data2["aircraft"].max(),data2["tank"].max(),data2["drone"].max(),data2["helicopter"].max(),data2["naval ship"].max(),data2["fuel tank"].max(),]
fig = px.pie(names = names, values = values, hole = 0.5, color_discrete_sequence=px.colors.sequential.ice)
fig.show()
