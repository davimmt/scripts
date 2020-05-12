from Function import Function

class Command:
    def __init__(self, password_index):
        self.f = Function()
        self.password = self.f.getBaseVariables('password')[password_index]
        self.cron_header = self.f.getBaseVariables('cron_header')
        self.sudo = self.f.sudo(self.password)
    
    def ntpdate(self, file_name, cron, user, jobs):
        imploded_jobs = ' && '.join(jobs)

        header = self.cron_header
        bodyFormat = header + cron + user + imploded_jobs

        commands = [
            self.sudo + "install -m 777 /dev/null " + file_name,
            "echo -e '" + bodyFormat + "' > " + file_name,
            self.sudo + "chmod 644 " + file_name
        ]

        return commands

    def getDates(self):
        commands = [
            "echo 'Hardware Clock: '; " + self.sudo + "hwclock", # | cat >> $file_name
            "echo 'System Clock: '; date '+%a %d %b %Y %H:%M:%S'" # | cat >> $file_name
        ]

        return commands