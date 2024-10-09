import pandas
data = pandas.read_csv("Squirrel_Data.csv")
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]

gray_squirrels_count = len(gray_squirrels)
red_squirrels_count = len(red_squirrels)
black_squirrels_count = len(black_squirrels)

print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count": [gray_squirrels_count,red_squirrels_count,black_squirrels_count]
}

print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv("Fur Color Count.csv")
