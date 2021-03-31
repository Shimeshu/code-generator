'''
Code Generator for:

1. Java Projects
2. Python Projects
'''

import os
import sys

from source import java, python

select_type = input("Select The Type of Project [1-4]\n[1]Python\n[2]Java\n?")


if select_type.lower() == "1":
	name = input("Project Name -> ")
	python.createProject(name)

if select_type.lower() == "2":
	name = input("Project Name -> ")
	java.createProject(name)
