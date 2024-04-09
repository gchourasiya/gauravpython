import psycopg2
from sshtunnel import SSHTunnelForwarder
import pandas as pd
#Create an SSH tunnel

tunnel = SSHTunnelForwarder(
    ('10.252.38.10', 22),

    ssh_username='redshift-bastion-sa',
    ssh_private_key='bastion.pem',

    #ssh_private_key_password=*,
    remote_bind_address = ('10.252.52.194', 5439),
    local_bind_address=("local ost 6543"), #could be any available port

)

#Start the tunnel

tunnel.start()

tunnel.daemon_forward_servers = True#Create a database connection



conn = psycopg2.connect( database='truevuedb",

user='inbanrensolauto",

host-tunnel. Local_bind_host,

port-tunnel.Local_bind_port, password=INBANRENSOLAUTO test123'

password=INBANRENSOLAUTO_test123

25

26

27

#Get a database cursor

29

cur conn.cursor()

30

33

#Execute SQL

cur.execute("select from test 101 prismax.device events alarms order by airs event ti

32

34

35

36

#Get the result

result cur.fetchall() df pd.DataFrane (result)

I

print(df) df.to_csv("plk redshift_data.csv" encoding='utf-8')

37

38

39

40

#Close connections

41 42

conn.close()

43

#Stop the tunnel tunnel.stop()

44

45

walid AWS Connection: Failed to validate your AWS