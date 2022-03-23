import boto3

aws_mag_con_root = boto3.session.Session(profile_name="root")
iam_con = aws_mag_con_root.resource("iam")

s3_con = aws_mag_con_root.resource("s3")
for each_buk in s3_con.buckets.all():
    print(each_buk)

# for each_usr in iam_con.users.all():
#     print(each_usr.name)