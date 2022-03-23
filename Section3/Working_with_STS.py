import boto3
aws_mag_con_report = boto3.session.Session(profile_name="root")
sts_con_cli = aws_mag_con_report.client(service_name="sts")
response = sts_con_cli.get_caller_identity()
print(response)

aws_mag_con_report = boto3.session.Session()
sts_con_cli = aws_mag_con_report.client(service_name="sts")
response = sts_con_cli.get_caller_identity()
print(response)