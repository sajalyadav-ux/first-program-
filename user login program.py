registered_user={}
print("--- registration process---")
reg_email=input("enter your email:").strip().lower()
reg_name=input("enter your name:").strip()
registered_user[reg_email]=reg_name
print("registration process is completed...")
print("login...")
login_email=input("enter your e-mail:").strip().lower()
if login_email in registered_user:
  name=registered_user[login_email]
  print(f"welcome {name}.login process completed..")
else:
  print("access denied :e-mail is wrong")
