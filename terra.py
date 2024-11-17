import subprocess

def terraform_init(command):
    process = subprocess.run(command,shell=True,check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    print(process.stdout.decode())

directory = "D:/terraform/EC2-With-Python"
#command = f"terraform -chdir={directory} init"
#command = f"terraform -chdir={directory} plan"
command = f"terraform -chdir={directory} destroy -auto-approve"
#print(command)
terraform_init(command)
