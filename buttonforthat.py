import subprocess
import json
import web

f = open('commands.json')
commands = json.load(f)

urls = (
    '/(.*)', 'button'
)
app = web.application(urls, globals())

class button:

    def GET(self, action=None):

        if not action: 
            return self.list()

        return self.run(self.get_commands()[action])

    def list(self):

        output = '<!doctype html>\n<html><head></head><body>'
        
        commands = self.get_commands()        

        for x in commands:
            output += '<div><code>' +  commands[x] + '</code><p><a href="/' + x + '">' + x + '</a></p></div><hr>'

        return output + '</body></html>'

    def get_commands(self):
        f = open('commands.json')
        return json.load(f)


    def run(self, cmd):
        p = subprocess.Popen(cmd.split(' '), stdout=subprocess.PIPE)
        out, err = p.communicate()

        if out is None:
            out = ''

        if err is None:
            err = ''

        output = '<!doctype html>\n<html><head></head><body><pre>' + out  + err + '</pre><a href="/">Back...</a></body></html>'

        return output

if __name__ == "__main__":
    app.run()

