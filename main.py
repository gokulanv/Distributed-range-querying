import partitioning_paper as Partioning
import rangequery_paper as RangeQuery
import datetime

print("Creating Database Name dds")
Partioning.createDB()

print("Getting connection from dds database")
con = Partioning.getOpenConnection()

print("Deleting all Tables")
Partioning.deleteTables('all',con)

print("Creating and Loading the ratings table")
Partioning.loadRatings('ratings','data/ij.dat',con)

print("Doing Range Partitioning")
Partioning.rangePartition('ratings',53,con)

st = datetime.datetime.now()
# print("Performing Range Query")
RangeQuery.FastRangeQuery('ratings','aa','az',10, 53, con)
# RangeQuery.RangeQuery('ratings','aa','az',con)
en = datetime.datetime.now()

print((en-st)*1000)

st = datetime.datetime.now()
# print("Performing Fast Range Query")
RangeQuery.RangeQuery('ratings','aa','az',10, 53, con)
# RangeQuery.RangeQuery('ratings','aa','az',con)
en = datetime.datetime.now()

print((en-st)*1000)

# print("Deleting all Tables")
# Partioning.deleteTables('all',con)
