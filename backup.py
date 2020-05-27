#!/usr/bin/python3
import os
import string
import time
import datetime
import pipes
import configparser
import yaml
import pprint
import glob

pp = pprint.PrettyPrinter(indent=2)

filenames = next(os.walk('.'))

pp.pprint(filenames)   


# with open('backup.yaml') as cnf:
#     data = yaml.load(cnf, Loader=yaml.FullLoader)
#     pp.pprint(data)
#     # print (yaml.dump(data))

# def folderBackup(dirName, backupdir):
#     pritn(dirName)

# Config = configparser.ConfigParser()
# Config.read('backup.cnf')
# dbList = Config.get('config','dbList').split(',')
# BackupDir = os.path.join( os.path.abspath(Config.get('config','backupDir')), time.strftime('%Y%m%d-%H%M%S'))

# folderBackup(dbName, BackupDir)

# def usage():
#   usage = ["mysqlbackup.py [-hkdbups]\n"]
#   usage.append("  [-h | --help] prints this help and usage message\n")
#   usage.append("  [-k | --keep] number of days to keep backups before deleting\n")
#   usage.append("  [-d | --databases] a comma separated list of databases\n")
#   usage.append("  [-t | --store] directory locally to store the backups\n")
#   usage.append("  [-u | --user] the database user\n")
#   usage.append("  [-p | --password] the database password\n")
#   usage.append("  [-s | --host] the database server hostname\n")
#   usage.append("  [-o | --options] the json file to load the options from instead of using command line\n")
#   usage.append("  [-r | --restore] enables restore mode\n")
#   print (''.join(usage))

# usage()
