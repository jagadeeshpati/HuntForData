import boto3
import psycopg2

def lambda_handler(event, context):
    if event:
        s3 = boto3.client("s3")
        conn = psycopg2.connect(database="mypostgresdb", user = "mypostgresusername", password = "mypostgresusername", host = "***.us-east-1.rds.amazonaws.com", port = "5432")
        print("Opened database successfully")
        cur = conn.cursor()
        content_list=[]
        var=[]

        file_obj = event["Records"][0]
        filename = str(file_obj['s3']['object']['key'])
        bucket_name = str(file_obj['s3']['bucket']['name'])
        fileObj = s3.get_object(Bucket =bucket_name, Key=filename)
        file_content = fileObj["Body"].read().decode('utf-8')
        content_list.append(file_content)
        for i in content_list:
             var=i.split('\r\n')
        var.pop(0)
        var.pop(-1)
        for j in range(len(var)):
            print(var[j])
        print ("Count of Lines :", file_content.count('\n'))
        for j in range(len(var)):
            for row in var:
                st = row.split(',')
                person=st[0]
                year=st[1]
                company=st[2]
                cur.execute("INSERT INTO sample_data (person,year,company) VALUES (%s, %s, %s)", (person,year,company))
        conn.commit()
        print("Records created successfully")
        conn.close()
