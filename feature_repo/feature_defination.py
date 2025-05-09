from datetime import timedelta
from feast import Entity, FeatureService, FeatureView, Field, FileSource, ValueType
from feast.types import Float64, Int64, String
from feast.value_type import ValueType

# patient = Entity(name = "patient_id",
#                      value_type = ValueType.INT64,
#                  description = "ID of the patient")
patient = Entity(name="customer", join_keys=["ID"])
## Predictors Feature View
file_source = FileSource(path = r"data/predictors_df.parquet",
                         event_timestamp_column = "event_timestamp",)

df1_fv = FeatureView(
    name = "predictors_df_feature_view",
    ttl = timedelta(seconds = 86400*2),
    entities = [patient],
    schema = [
    Field(name = "Age", dtype = Int64),
    Field(name = "Is_Parent", dtype = Int64),
    Field(name = "Total_Kids", dtype = Int64),
    Field(name = "Marital_Status_Simplified", dtype = String),
    Field(name = "Total_Spent", dtype = Int64),
    Field(name = "MntWines_Share", dtype = Float64),
    Field(name = "MntFruits_Share", dtype = Float64),
    Field(name = "MntMeatProducts_Share", dtype = Float64),
    Field(name = "MntFishProducts_Share", dtype = Float64),
    Field(name = "MntSweetProducts_Share", dtype = Float64),
    Field(name = "MntGoldProds_Share", dtype = Float64),
    Field(name = "Total_Purchases", dtype = Int64),
    Field(name = "Avg_Spend_per_Purchase", dtype = Float64),
    Field(name = "Deal_Rate", dtype = Float64),
    Field(name = "Web_Purchase_Share", dtype = Float64),
    Field(name = "Web_Visit_to_Purchase_Ratio", dtype = Float64),
    Field(name = "Is_Online_Buyer", dtype = Int64),
    Field(name = "Customer_Since_Days", dtype = Int64),
    Field(name = "Is_Active", dtype = Int64),
    Field(name = "Lifetime_Spend_per_Day", dtype = Float64),
    Field(name = "Total_Accepted_Campaigns", dtype = Int64),
    Field(name = "Campaign_Response_Rate", dtype = Float64),
    ],
    source = file_source,
    online = True,
    tags= {},
)

## Target FEature View

target_source = FileSource(path = r"data/target_df.parquet", event_timestamp_column = "event_timestamp",)

target_fv = FeatureView(
    name = "target_df_feature_view",
    ttl = timedelta(seconds = 86400*2),
    entities = [patient],
    schema = [
    Field(name = "Response", dtype = Int64),       
    ],
    source = target_source,
    online = True,
    tags= {},
)