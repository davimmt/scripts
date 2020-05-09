from Function import Function

class Command:
    def __init__(self):
        self.f = Function()
        self.password = self.f.getBaseVariables('password')[2]
        self.cron_header = self.f.getBaseVariables('cron_header')
        self.sudo = self.f.sudo(self.password)
    
    def ntpdate(self, file_name, cron, user, jobs):
        header = self.cron_header
        bodyFormat = header + cron + user + jobs[0] + "; " + jobs[2]

        commands = [
            self.sudo + "install -m 777 /dev/null " + file_name,
            "echo -e '" + bodyFormat + "' > " + file_name,
            self.sudo + "chmod 644 " + file_name
        ]

        return commands