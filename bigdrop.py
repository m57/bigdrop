#!/usr/bin/python
###########################################################################
#
# ADD YOUR DigitalOcean TOKEN BELOW
# ---------------------------------
token = ""
#
###########################################################################
###########################################################################
############# DONT EDIT BELOW HERE, UNLESS YOU KNOW OBVIOUSLY :) ##########
###########################################################################
###########################################################################

import sys
import time
import digitalocean
import xml.etree.ElementTree as ET

version = "1.0"
c 	= { "r" : "\033[1;31m", "g" : "\033[1;32m", "y" : "\033[1;33m", "e" : "\033[0m" }
manager = digitalocean.Manager(token=token)

def get_droplets():
	return manager.get_all_droplets()
	
def get_my_token(token):
	return getpass.getpass()

def create_droplet(token, name, region, os, ram, ssh):

	if len(ssh) < 1:
		ssh = ""

	droplet = digitalocean.Droplet(token=token,
                               name=name,
                               region=region,
                               image=os,
                               size_slug=ram,
                               backups=False,
			       ssh_keys=ssh)
				
	x = droplet.create()
	
	print "%s[Droplet]%s '%s' Created." % ( c["g"], c["e"], name )

def interactive_build():

	num = int(raw_input("How many droplets do you want to create: "))

	name = raw_input("VPS name (if # of VPS > 1, name will become %name%-01, %name%-02 etc): ")

	for i in manager.get_all_regions():
		print "%s : '%s'" % (i.name.strip(), i.slug.strip())
	region = raw_input("What region: ")

	for i in manager.get_all_images():
		print "'%s'" % (i.slug)
	os = raw_input("What base image: ")

	ram = raw_input("What size RAM (e.g. 4096): ")
	if "mb" in ram or "MB" in ram:
		ram = ram[:2]

	for n in xrange(num-1):
		x = create_droplet(token, name, region, os, ram)
		print "\033[1;32m[+]\033[0m Droplet '%s' created -> IP address '%s'" % ( str(name + str("-" + n)), x.ip_address)
	

def parse_file(file):

	try:
		f = open(file, "r").close()
	except:
		print "%s[Error]%s Accessing file '%s'" % (c["r"], c["e"], file)
		exit()
		
	d = { "amount" : 1, "name" : "newDroplet", "ram" : "512", "location" : "lon1",  "image" : "fedora-22-x64", "ssh_key" : "" }

	try:
		root = ET.parse(file).getroot()
	except:
		print "%s[Error]%s Invalid XML file '%s', refer to README for schema information." % (c["r"], c["e"], file)
		exit()

	for child in root:
		childd = child.tag.lower()
		if (childd == "amount"):
			d["amount"] = int(child.text)

		elif (childd == "name"):
			d["name"] = child.text.lower()

		elif ( (childd == "ram") and (int(child.text) >= 256) ):
			d["ram"] = int(child.text)

		elif (childd == "location"):
			d["location"] = child.text.lower()

		elif (childd == "image"):
			d["image"] = child.text.lower()

		elif (childd == "ssh_key"):
			d["ssh_key"] = []
			d["ssh_key"].append(child.text.lower())
		else:
			print "%s[Error]%s Invalid XML Schema, tag '%s' is not a valid identifier, see README." % (c["r"], c["e"], childd)
			exit()

	return d


def create_droplets_from_list(drop_dic):

	for num in range(0, drop_dic["amount"]):
	
		name = drop_dic["name"] + "-" + str(num)
		ram = str(drop_dic["ram"]) + "mb"	
		img = drop_dic["image"]
		loc = drop_dic["location"]
		ssh = drop_dic["ssh_key"]
		create_droplet(token, name, loc, img, ram, ssh)

def banner():

	print c["g"]
	print "ICBfICAgICBfICAgICAgICAgICBfICAgICAgICAgICAgICAgICAKIHwgfCAgIChfKSAgICAgICAgIHwgfCAgICAgICAgICAgICAgICAKIHwgfF9fICBfICBfXyBfICBfX3wgfF8gX18gX19fICBfIF9fICAKIHwgJ18gXHwgfC8gX2AgfC8gX2AgfCAnX18vIF8gXHwgJ18gXCAKIHwgfF8pIHwgfCAoX3wgfCAoX3wgfCB8IHwgKF8pIHwgfF8pIHwKIHxfLl9fL3xffFxfXywgfFxfXyxffF98ICBcX19fL3wgLl9fLyAKICAgICAgICAgICBfXy8gfCAgICAgICAgICAgICAgIHwgfCAgICAKICAgICAgICAgIHxfX18vICAgICAgICAgICAgICAgIHxffCAgICB2JXMKCgo=".decode("base64") % (version)
	print c["e"],
	print "       @_x90__, @program_ninja "
	print "  https://github.com/m57/bigdrop.git "
	print ""
	print ""

def usage():

	banner()
	
	print "\n# python %s [options]" % sys.argv[0]
	print ""
	print "Options: "
	print "\t-l\t[arg]\t\t-\tList information about '[arg]' -> droplets, loc, img"
	print "\t-f\t[file.xml]\t-\tCreate droplets from XML schema, see README."
	print "\t-i\t\t\t-\tCreate droplets from interactive menu (Easy)"
	print "\t-rm\t[id]\t\t-\tDelete droplet [id]"
	print ""
	exit(1)

			
if __name__ == "__main__":

	banner()

	if token == "":
		print "%s[Error]%s Please first set your DigitalOcean API token at the top of the script." % (c["r"], c["e"])
		exit()

	if "-rm" in sys.argv:
		
		id = int(sys.argv[sys.argv.index("-rm")+1])

		d = get_droplets()

		try:
			name = d[id].name
		except:
			print "%s[Error]%s Droplet ID out of range, do 'python %s -l droplets' to see how many droplets you have." % (c["r"], c["e"], sys.argv[0])
			exit()
		
		ch = raw_input("%s[Confirm]%s Are you sure you want to delete droplet '%s' [Y/N]: " % (c["r"], c["e"], name ))
		
		if "y" in ch or "Y" in ch:

			try:
				d[id].destroy()
			except:
				print "%s[Error]%s DataReadError from DigitalOcean, retry again later" % ( c["r"], c["e"] )
				exit(1)
		print "%s[Done]%s Droplet '%s' destroyed." % ( c["g"], c["e"], name )
		exit()

	elif "-l" in sys.argv:
		option = sys.argv[sys.argv.index("-l")+1]

		if option.lower() == "img":
			print "%s[Option]%s All valid base images." % (c["y"], c["e"])
			im = manager.get_distro_images()
			for i in im:
				print "%s[Image]%s %s -> '%s'" % (c["g"], c["e"], str(i.distribution + " " + i.name), i.slug)
			exit()

		elif option.lower() == "loc":
			print "%s[Option]%s All regions." % (c["y"], c["e"])
			r = manager.get_all_regions()
			for i in r:
				print "%s[Region]%s %s -> '%s'" % (c["g"], c["e"], i.name, i.slug)
			exit()
		
		elif option.lower() == "droplets":
			print "%s[Option]%s All your Droplets." % (c["y"], c["e"])
			d = get_droplets()
			count = 0
			for i in d:
				print "%s[Droplet id: '%d']%s '%s' -> '%s'" % (c["g"], count, c["e"], i.name, i.ip_address)
				count += 1
			exit()

		else:
			print "%s[Error]%s Option '%s' not recognised, see '%s --help'" % (c["r"], c["e"], option, sys.argv[0])
			exit()

	elif "-i" in sys.argv:
		interactive_build()	
		exit()

	elif "-f" in sys.argv:
		list = parse_file(sys.argv[sys.argv.index("-f")+1])
		create_droplets_from_list(list)
		exit()

	else:
		usage()
