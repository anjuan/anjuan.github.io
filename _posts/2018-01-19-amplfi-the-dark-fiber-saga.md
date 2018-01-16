---
title: 'Amplifi: The Dark Fiber Saga'
author: anjuan
layout: post
date: "2018-01-19"
permalink: /blog/amplifi-the-dar-fiber-saga/
categories:
  - Tech
excerpt: "My home network wasn't meeting my needs. I was blowing through my ISP's data cap every month and I had dead spots in various corners where the WiFi completely died. This is the story of how I fought to revive my home network with AT&T's fiber service and AmpliFi HD."
comments: true
---

{% include image.html url="/images/amplifi-the-dark-fiber-saga-header.jpeg" alt="networking equipment" caption="Resolving my home network issues required new service, new equipment, and a lot of troubleshooting. (Pexels)" width=400 align="right" %}

Like a lot of people who work in tech, my home network is a gateway to the public internet for the various devices used by my family as well as a laboratory where I test out different configurations of the internal network. 

For my family, our home network is a wireless hotspot where my wife can sit on the coach using her work laptop and our kids can roam around the house on their phones and tablets watching YouTube videos, playing online games, and completing school assignments. 

For me, our home network is a place where I can work remotely from my company's central office and also open ports to allow various services to work through the router. It's also a security system when I travel because I can almost feel like I'm still home by checking the various network cameras around the home and even being alerted when someone pushes the button on the Ring doorbell next to our front door.

I upgraded my home network in 2014, but it was beginning to show its age. Here is the second floor of my house where the Linksys router valiantly tried to cover both floors and all corners of my house:





## Medieval Times

TBD

## Fiber

Blazing Speed

But, only to a few ethernet ports

## Meshing

Google WiFi or Amplifi HD?

Twitter guy's great Amplifi blog posts

An AmpliFi HD soon appeared on my doorstep.

## Amplifi Setup

While the AmplFi router is very nice looking, I had to stick it in the bedroom closet where my Ethernet drops terminate. This made it very easy to hardwire the Ethernet ports in rooms around my house.

Immediate benefit of an additional Ethernet port

## Speed Bumps

TBD

## Dark Fiber

TBD

## Support Purgatory

AmpliFi and AT&T

## Success!

TBD

## Modernity

Bridge mode on the AmplFi HD means no Guest network, port forwarding, etc.

Used old Linksys router downstream of the AmpliFi to create a guest network (had to turn off dhcp because I got the same router behind router error message, but I left DNS on so it could assign IP addresses to guest users)
  * Good instructions here: https://www.linksys.com/fi/support-article?articleNum=137888, but I had to hard reset the router first while it was downstream from the Amplifi
  * It's very important that you set the router to obtain an IPv4 address automatically so that it gets an IP address from the modem (in this case, the AT&T fiber modem)
  * I turned off the 5 GHz band because I didn't want to provide a high speed guest pipe that would degrade the bandwidth of my house
  * So, I only kept the 2.4 GHz band
  * I put a password on it, but I'm ok if it gets out.
  * In bridge mode you cannot:
   * Provide a guest WiFi access point (fine, because I intended to use it as an guest network)
   * Create MAC filters
   * Change port settings
   * Set Parental Controls
   * Set Device Prioritization
   * Create Profiles to group devices (ouch!)
   * Pause internet on individual groups or devices (ouch!)
   * I was (mostly) fine because this was only for guest users who just needed internet access
   * I can administer the Linksys router on the AmpliFi HD by seeing how much data is going across it and restricting internet access on it altogether.
   * I did miss the ability to filter MAC addresses and administer ports on the AmpliFi HD, but I only needed to do that in a small number of edge cases.



## Benefits

* Erasure of dead zones
* August Smart Lock could be remotely accessed because it was near a mesh router. 
* TBD

## Verdict

Pros

Cons




## Future Plans

   * Keep using the Amplifi HD
   * Purchase the Ubiquiti Teleport which is a VPN solution