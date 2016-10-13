import bubbles
from bubbles import Pipeline, open_store

URL = "https://raw.github.com/Stiivi/cubes/master/examples/hello_world/data.csv"

p = bubbles.Pipeline()

#Set the source dataset
p.source_object("csv_source", resource=URL, encoding="utf8")

p.retype({"Amount (US$, Millions)": "integer"})

#Aggregate population by category code
p.aggregate("Category", "Amount (US$, Millions)")

#Print pretty table
p.pretty_print()

p.run()
