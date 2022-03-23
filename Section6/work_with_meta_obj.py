import boto3
aws_mag_con = boto3.session.Session(profile_name="root")
ec2_con_re = aws_mag_con.resource(service_name="ec2")

# from resource obj -> client obj
ec2_con_cli = ec2_con_re.meta.client
print(ec2_con_cli.describe_regions())