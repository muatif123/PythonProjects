# Importing the required libraries
import boto3
from rds import RDS
from ec2_auto import Ec2Instance

# Defining the function for aws lamda 
def aws_lambda(event, context):
    print("Event " + str(event))
    print("Context " + str(context))
    ec2_reg = boto3.client('ec2')
    regions = ec2_reg.describe_regions()
    for region in region['Regions']:
        region_name = region['RegionName']
        instances = Ec2Instance(region_name)
        deleted_counts = instances.delete_snapshots(1)
        instances.delete_available_volumes()
        print("Deleted counts for region " + str(region_name) + " is " + str(deleted_counts))
        instances.shutdown()
        print("For RDS")
        rds = RDS(region_name)
        rds.cleanup_snapshot()
        rds.cleanup_instances()
    return 'Hello for Lambda'
    