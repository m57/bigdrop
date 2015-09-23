Bigdrop is script which allows you to easily create multiple Droplets. Hopefully it will become more managable, although this 
isnt what i want from it personally at the moment, so it hasnt been coded in!

The main annoyance is that you need to hardcode your DigitalOcean API key into the script, i could add in a '-t' argument or 
something but im too lazy. Sorry!

Enjoy anyway!

____________________________________________________________________

Command Line Arguments:

+-------------+
+ -f file.xml +
+-------------+

This allows you to create an XML like so:

=== XML FILE ===
<droplet>
<amount>3</amount>
<name>AutoUbuntu</name>
<ram>512</ram>
<location>lon1</location>
<sshkey></sshkey>
<image>fedora-22-x64</image>
</droplet>
========== EOF ==============

Name is only Aa-Zz, -, 0-9
RAM should be > 256
Locations can be retrieved by doing 'python bigdrop.py -l loc'
sshkey should just be an SSH key fingerprint that is already attached to your DigitalOcean account.
Images can be retrieved via 'python bigdrop.py -l img'

The following fields could be omitted:

<name>
<ram>
<sshkey>
<location>
<image>

if they are, their default values are:

name     : 'newDroplet'
ram      : '512 MB"'
location : 'London'
image	 : 'Fedora 22 x86_64'
sshkey	 : 'None'

so the following is a perfectyl valid XML file:

---
<droplet>
<amount>10</amount>
</droplet>
---

This would create 10 default droplets as specified above.

+----+
+ -i +
+----+

This is interactive mode and just goes through step by step to create multiple droplets, easy...

+--------------+
+  -l option   +
+--------------+

This allows you to list the valid values for the XML data, so you want a different OS to fedora 22 ? See below...

-l img		--->	This lists all the images that you can use in the XML file and supported by DigitalOcean.
-l loc		--->	This lists all the locations of the servers that are supported by DigitalOcean.
-l droplets 	--->	This lists all the droplets you have in your account.
