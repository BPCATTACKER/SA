"""
Copyright [2019] [S.A TOOL ATTACK BY MR.SPOON VERSION 5]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# This is an example of a distutils 'MySetup' script for the example_nt
# sample.  This provides a simpler way of building your extension
# and means you can avoid keeping MSVC solution files etc in source-control.
# It also means it should magically build with all compilers supported by
# python.

# USAGE: you probably want 'MySetup.py' - but execute 'MySetup.py --help'
# for all the details.

# NOTE: This is *not* a sample for distutils - it is just the smallest
# script that can build this.  See distutils docs for more info.
# reading Project
global data
headers = open("Project.txt", "r")
data = headers.read()
headers.close()

		
def usage():
	print (''' sh sa5.sh =command untuk jalankan tool
		-h =untuk bantuan''')
	sys.exit()


print("""\033[32;1m
Coding : python 3,bash
League :IND,ENG
Athour :MR.SPOON
TeAm   : BLACK PHANTOM CYBER
Licence Version : Apache.The Mit Licence (Mit)
Made In Indonesia --> Bundah Street 42 KBT SM KC SRH MADURA ISLAND
Zone time :GMT+07.00,WIB
 

        -|DI BUAT 26-05-2019|-

TTD MR.SPOON

YG COPYRIGHT GW DOAIN GK BERKAH""")
print
print("\033[31;1m[A]LiNet [D]eNial [O]f [S]ervice || [S]Imulation [A]rmagedon")
print("\033[31;1mPENGEMBANG=MR.SPOON")
print("-------------------------------------------------")
print("\033[31;1mBantuan? python MySetup.py -h")
print("--------")
print("UNTUK MEMULAI GUNAKAN COMMAND sh sa5.sh")



