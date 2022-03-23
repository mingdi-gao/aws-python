import boto3

aws_mag_con = boto3.session.Session(profile_name="root")
iam_con_re = aws_mag_con.resource(service_name="iam", region_name="us-west-2")
ec2_con_re = aws_mag_con.resource(service_name="ec2", region_name="us-west-2")
s3_con_re = aws_mag_con.resource(service_name="s3", region_name="us-west-2")

# List all IAM users

for each_item in iam_con_re.users.all():
    print(each_item.user_name)
