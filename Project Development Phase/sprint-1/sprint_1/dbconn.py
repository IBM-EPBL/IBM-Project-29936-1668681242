import ibm_db
try:
    con = ibm_db.connect("DATABASE=bludb;HOSTNAME=19af6446-6171-4641-8aba-9dcff8e1b6ff.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30699;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=wvb67169;PWD=xkTYBLLgFroQY7Zk;", '', '')
    print("db connection successfully")
except:
    print("db connection failed")
