import jenkins
import time

# Jenkins server details
jenkins_url = "http://your-jenkins-url"
username = "your-username"
password = "your-password"

# Job details
job_name = "example-job"

try:
    # Connect to Jenkins server
    server = jenkins.Jenkins(jenkins_url, username=username, password=password)
    print("Connected to Jenkins.")

    # Trigger the job
    build_number = server.build_job(job_name)
    print(f"Triggered job '{job_name}', build number: {build_number}")

    # Wait and fetch build status
    time.sleep(5)  # Wait before checking status
    build_info = server.get_build_info(job_name, build_number)

    # Print build details
    print(f"Build #{build_number} Status: {build_info['result']}")

except jenkins.JenkinsException as e:
    print(f"An error occurred: {e}")

