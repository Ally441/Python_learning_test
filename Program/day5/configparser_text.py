Author = 'Liu Lei'
import configparser

config=configparser.ConfigParser()
config['DEFAULT']={'ServerAliveInterval':'45','sex':'girl'}
config['f']={'aslkd':'wew'}
config['topsecret.server.com']={}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'  # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
with open('example.ini', 'w') as configfile:
    config.write(configfile)