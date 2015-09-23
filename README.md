Bigdrop is script which allows you to easily create multiple Droplets. Hopefully it will become more managable, although this isnt what i want from it personally at the moment, so it hasnt been coded in!

The main annoyance is that you need to hardcode your DigitalOcean API key into the script, i could add in a '-t' argument or something but im too lazy. Sorry!

Enjoy anyway!
____________________________________________________________________

**Command Line Arguments:**

![Arguments](http://slimgr.com/images/2015/09/23/9d8cf8b69ea6de7b6db074c3b4760fb8.png)

```# python bigdrop.py -f file.xml```

This allows you to create an XML like so:

```XML
  <droplet>
  <amount>3</amount>
  <name>AutoUbuntu</name>
  <ram>512</ram>
  <location>lon1</location>
  <ssh_key>AA:AA:AA:AA:AA:AA:AA:AA:AA:AA:AA:AA:AA:AA:AA:AA</ssh_key>
  <image>fedora-22-x64</image>
  </droplet>
```
* \<name\> Is only Aa-Zz, -, 0-9
* \<ram\> Should be \> 256
* \<location\> Be retrieved by doing 'python bigdrop.py -l loc'
* \<ssh_key\> Should just be an SSH key fingerprint that is already attached to your DigitalOcean account.
* \<image\> Can be retrieved via 'python bigdrop.py -l img'

The following fields could be omitted:

* \<name\>
* \<ram\>
* \<sshkey\>
* \<location\>
* \<image\>

If they are, their default values are:

```
name    : 'newDroplet'
ram     : '512 MB"'
location: 'London'
image   : 'Fedora 22 x86_64'
sshkey  : 'None'
```

So the following is a perfectly valid XML file:

```XML
  <droplet>
  <amount>10</amount>
  </droplet>
```

This would create 10 default droplets as specified above.

```# python bigdrop.py -i```

This is interactive mode and just goes through step by step to create multiple droplets, easy...

```# python bigdrop.py  -l [option]```

This allows you to list the valid values for the XML data, so you want a different OS to fedora 22 ? See below...

```
-l img		    --->	This lists all the images that you can use in the XML file and supported by DigitalOcean.
-l loc		    --->	This lists all the locations of the servers that are supported by DigitalOcean.
-l droplets 	--->	This lists all the droplets you have in your account.
```
![Image]()
