import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count = data[data["Primary Fur Color"] == "Gray"].count()["Unique Squirrel ID"]
red_count = data[data["Primary Fur Color"] == "Cinnamon"].count()["Unique Squirrel ID"]
black_count = data[data["Primary Fur Color"] == "Black"].count()["Unique Squirrel ID"]

# Also can be written as
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_count, red_count, black_count],
}

squirrel_count = pandas.DataFrame(data_dict)
squirrel_count.to_csv("squirrels_count.csv")
