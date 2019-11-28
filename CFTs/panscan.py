#!/usr/local/bin/python3

import subprocess
import json
import os
from tkinter import *
from tkinter import ttk
import tkinter.filedialog as filedialog
from tkinter.scrolledtext import ScrolledText



temp_file = "redshift_cluster.cft"
temp_dir = "/Users/jbuhr/scan_examples/CFTs"

def run_command(cmd):
   from subprocess import Popen, PIPE
   p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE, close_fds=True, universal_newlines=True)
   stdout, stderr = p.communicate()
   return(stdout)

def temp_scan(template):
   curl = '/usr/bin/curl'
   command = curl + " " + "-d @" + template + " -X POST https://scanapi.redlock.io/v1/iac"
   return(run_command(command))

def json_format(jsondata):
   parsed = json.loads(jsondata)
   return(json.dumps(parsed, indent=3, sort_keys=True))

def get_absfiles(directory):
   # takes a directory path and returns all files with absolute paths
   files_path = [os.path.abspath(x) for x in os.listdir(directory)]
   print(files_path)
   return("true")

def get_scanfile():
   ftypes = [
      ('Cloud Formation Templates', '*.cft'),
      ('Terraform Configuration File', '*.tf;*.tf.json'),
      ('Kubernetes YAML Config File', '*.yaml'),
   ]

   fpath = filedialog.askopenfilename(filetypes=ftypes)
   if fpath:
      return(fpath)
   else:
      return('cancelled')

#print(get_scanfile())


root = Tk()

content = ttk.Frame(root, padding=(3,3,12,12))
frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100)
iaclbl = ttk.Label(content, text="Selected IaC File")
name = ttk.Entry(content)

scan = ttk.Button(content, text="Scan")
quit = ttk.Button(content, text="Quit")

content.grid(column=0, row=0, sticky=(N, S, E, W))
frame.grid(column=3, row=1, columnspan=3, rowspan=2, sticky=(N, S, E, W))
iaclbl.grid(column=0, row=0, columnspan=2, sticky=(N, W), padx=5)
name.grid(column=0, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
scan.grid(column=0, row=3)
quit.grid(column=0, row=4)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)


root.mainloop()

#get_absfiles("/Users/jbuhr/scan_examples/CFTs")
#print(json_format(temp_scan(temp_file)))

