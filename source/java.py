'''
Generates a Java Project
'''

import os


def createProject(name):
    os.mkdir(name)
    f = open(f"{name}/Main.java", "w+")
    code = '''/*Auto Generated Code*/
import java.util.*;
import java.io.*;

class Main {
	public static void main(String[]args) {
		System.out.println("Hello, World!");
	}
}
	'''
    f.write(code)
    f.close()
    readme = open(f"{name}/Readme.txt", "w+")
    readme.write("Write your Readme Here")
    readme.close()
    license = open(f"{name}/License.txt", "w+")
    lic_text = open("license.txt", "r+")
    text = lic_text.read()
    license.write(text)
    license.close()
    lic_text.close()
