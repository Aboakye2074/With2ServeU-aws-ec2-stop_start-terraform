# Replace the variables with the desired values.
# For best security practices, do not push to GitHub or publish these values. 
# Input these variables into your environment using the export command. 

region         = "us-east-2"
instance_ids   = ["i-0d611f9e5851e22dd", "i-07aca39e0f369983d"]
email = "tonboazz2003@yahoo.com"
start_schedule = "cron(2 5 * * ? *)" # 09:30 AM EST (04:02 AM UTC)
stop_schedule  = "cron(7 5 * * ? *)" # 09:02 AM EST (04:07 AM UTC)
