from pyspark.sql.functions import concat_ws, col
from pyspark.sql import SparkSession

data = [(1, 'John', None, 'Doe'),
    (2, 'Alice', 'Ann', 'Smith'),
    (3, 'Mike', None, 'Johnson')]
schema = ["id", "first_name", "middle_name", "last_name"]
spark = SparkSession.builder.appName('Pratibha').getOrCreate()

df = spark.createDataFrame(data, schema=schema)
df_with_columns = df.withColumn("full_name",
    concat_ws(" ", col("first_name"), col("middle_name"), col("last_name")))
df_with_columns.show()