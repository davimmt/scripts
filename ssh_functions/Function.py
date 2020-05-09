import base64

class Function:
    def b64decode(self, s):
        return base64.b64decode(s).decode("utf-8")
    
    def sudo(self, i):
        return 'echo ' + i + ' | sudo -S '

    def getBaseVariables(self, i):
        password = [
            self.b64decode('QWdhZGVpdGFETw=='), 
            self.b64decode('U29MZW1icm9Eb0pvdGEmNQ=='), 
            self.b64decode('djRuZXNzNDMyMQ=='),
        ]

        cron_header = r'SHELL=/bin/bash\nPATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin\n\n'

        if i == 'password':
            return password
        if i == 'cron_header':
            return cron_header
    

