from configparser import ConfigParser

config = ConfigParser()
config.read('config.cfg')
print(config.get('windows', 'bg_colour'))
