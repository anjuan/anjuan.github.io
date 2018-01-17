---
title: 'Amplifi: The Dark Fiber Saga'
author: anjuan
layout: post
date: "2018-01-17"
permalink: /blog/amplifi-the-dar-fiber-saga/
categories:
  - Tech
excerpt: "My home network wasn't meeting my needs. I was blowing through my ISP's data cap every month, and I had dead spots in various corners where the WiFi completely died. This is the story of how I fought to revive my home network with AT&T's fiber service and AmpliFi HD."
comments: true
---

{% include image.html url="/images/amplifi-the-dark-fiber-saga-header.jpeg" alt="networking equipment" caption="Resolving my home network issues required new service, new equipment, and a lot of troubleshooting. (Pexels)" width=400 align="right" %}

Like a lot of people who work in tech, my home network is a gateway to the public internet for the various devices used by my family as well as a laboratory where I test out different configurations of the internal network. 

For my family, our home network is a wireless hotspot where my wife can sit on the coach using her work laptop and our kids can roam around the house on their phones and tablets watching YouTube videos, playing online games, and completing school assignments. 

For me, our home network is a place where I can work remotely from my company's central office and also open ports to allow various services to work through the router. It's also a security system when I travel because I can almost feel like I'm still home by checking the various network cameras around the home and even being alerted when someone pushes the button on the Ring doorbell next to our front door.

I improved my home network in 2014, but it was beginning to show its age despite my upgrade to the highest consumer speed offered by Comcast. Here's the second floor of my house where my aged Linksys ac6900 router valiantly tried to cover both floors and all corners of my house with WiFi (2 GHz and 5 GHz bands) from the central patch board and switch in a closet while also providing ethernet connectivity to several rooms:

{% include image.html url="/images/amplifi-the-dark-fiber-saga-mclaren-second-floor.png" alt="mclaren second floor" caption="Second Floor" width=800 align="center" %}

The wireless signal on this image is just a graphical representation of the coverage of the Linksys router so I'll explain how it actually played out. Bedroom 2 is the upstairs guest bedroom, and whoever stayed in that room enjoyed excellent WiFi signal and speed. Bedroom 3 and Bedroom 4 are my kids' rooms, and they usually enjoyed decent signal and speed. The Learning Center is where my kids do their homework and hang out, and, since there are ethernet drops here (which connect to the Linksys router), desktop computers have fast wired connections (i.e., WiFi wasn't an issue). The room labeled Retreat is the game room which has an X-Box that connects via WiFi. Both of these areas had pretty good wireless signal and speed.

So, the second floor, due to the location of the Linksys router, wasn't a bad place to be if you wanted to roam around and use the wireless network. However, the first floor was a different story:

{% include image.html url="/images/amplifi-the-dark-fiber-saga-mclaren-first-floor.png" alt="mclaren second floor" caption="First Floor" width=800 align="center" %}

Again, the wireless image is just a graphical representation of the coverage of the ac6900 as it extended down to the first floor. The coverage in the center of the first floor wasn't too bad. So, guests hanging out in the Family room or eating in the dining room or breakfast area has a nice wireless experience. However, the master bedroom and master bath (hyperbolically called "Owners Retreat" and "Owners Bath" by the builder) had several areas where the WiFi signal from the ac6900 was week or non-existent. Also, the Nest Cameras I had for the backyard ("Covered Porch") and garage experienced random outages due to poor connectivity to the ac6900. 

Furthermore, I had an August lock on my front door (to the right of the Study) as well as a Ring doorbell on my front porch, and they both experienced drops. In fact, I purchased the August connect to control the lock anywhere in the world, but it usually never worked which meant the lock could only be controlled while in Bluetooth range. I also purchased two Ring Chimes (placed outside the Dining room on the first floor and Bathroom 2 upstairs) to improve the connectivity of the Ring doorbell since they bridged the wireless network.

I use the Study as my home office, and it has an ethernet jack so I never had a problem using a wired connection. However, using my phone and iPad on WiFi in my office wasn't a great experience.

Due to the numerous devices used by my kids, my family's frequent use of streaming video services, and my use of Google Cloud to back up my files, I found myself blowing through Comcast's 1 TB monthly cap on a regular basis. So, my bill was slowly increasing every month.

I decided to have another go at improving my home network a few weeks ago. I started by ordering AT&T's Internet 1000 speed which promised up to 1000 Mbps download and no caps. A technician spent four hours trenching outside my house and drilling a hole into my garage. The last step was installing and configuring a 2Wire 5268AC ("5268AC"). I did a quick speedtest with my laptop connected directly to one of the ethernet ports on the 5268AC and, unsurprisingly, I was getting a really fast connection:

{% include image.html url="/images/amplifi-the-dark-fiber-saga-speedtest-1.png" alt="speed test 1" caption="Speed test using wired connection to Linksys router" width=300 align="center" %}

While adding fiber generally improved the speed of wired connections from about 130 Mbps to consistent speeds above 900 Mbps, I still had dead spots in my home. I was like someone who ratched up the water pressure coming into a sprinkler system but still had dead grass in the yard that were too far from a sprinkler head. I realized I needed to expand my WiFi coverage which was impossible to do with the ac6900. So, as we do, I took to Twitter to complain.

## The Coming of AmpliFi HD

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">I&#39;m due for a new home router, and Google WiFi looks promising. But, the need for a constant connection to Google is odd. And, with CES around the corner, I can wait a few more weeks.</p>&mdash; Anjuan (@anjuan) <a href="https://twitter.com/anjuan/status/949854225978228736?ref_src=twsrc%5Etfw">January 7, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

As I suggested in this tweet, one of the mesh routers that came up again and again in my research was Google WiFi. However, I never buy new equipment when CES is so close, and I decided to wait. This tweet generated a bit of discussion leading to this comment by Dan North:

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">You should check out <a href="https://twitter.com/troyhunt?ref_src=twsrc%5Etfw">@troyhunt</a>’s home WiFi setup. Not the cheapest but he’s super stoked about it. He’s blogged about it at length.</p>&mdash; Dan North (@tastapod) <a href="https://twitter.com/tastapod/status/949864996305031168?ref_src=twsrc%5Etfw">January 7, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Troy himself replied shortly thereafter:

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Here’s what you want: <a href="https://t.co/yOLA3vFymL">https://t.co/yOLA3vFymL</a></p>&mdash; Troy Hunt (@troyhunt) <a href="https://twitter.com/troyhunt/status/949875350485348352?ref_src=twsrc%5Etfw">January 7, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

I had never heard of Ubiquiti, but Troy's posts are **thorough**. You really should follow the [link Troy posted above](https://www.troyhunt.com/tag/ubiquiti/) because he's a great writer and a technical expert.

I spent a day reading Troy's posts and began researching Ubiquiti's products when I was contacted by the company with an offer to try AmpliFi HD. They also offered to send me UniFi, but, based on my research, AmpliFi HD would be a better choice for my home. I provided my mailing address, and the AmpliFi HD box showed up a few days later. I was excited to receive the equipment, and I hurried upstairs to set it up.

{% include image.html url="/images/amplifi-the-dark-fiber-saga-as-is-patch-box.jpg" alt="patch box before" caption="The patch box and switch before the AmpliFi HD" width=800 align="center" %}

This is the patch box and switch in the upstairs guest bedroom closet with (going from right to left in the picture) the AT&T fiber modem, the Linksys router I was replacing, and an old Linksys switch. Most of the blue cables run to phone drops around the house, but the ones that go into the AT&T fiber modem connect to rooms with Ethernet ports. I also hung the Linksys router off the AT&T fiber modem so that it had a fast connection to broadcast over WiFi.  By the way, the AT&T fiber modem can broadcast WiFi, but it's not very good at it. So, I disabled the wireless capability of the AT&T fiber modem and just used it for getting the fast connection into my patch box. I used the Linksys router for WiFi, but I know could replace it with the AmplFi HD.

{% include image.html url="/images/amplifi-the-dark-fiber-saga-amplifi-hd-in-the-patch-box.jpg" alt="amplifi hd in the patch box" caption="Amplifi HD in the Patch Box!" width=800 align="center" %}

I opened the AmpliFi HD and found that the packaging was very clean and minimal. You can see the square router and the two mesh antennas that extend the ranger of the router.

I prepared to disconnect the Linksys router and immediately saw a benefit to using the AmpliFi HD.

{% include image.html url="/images/amplifi-the-dark-fiber-saga-freeing-an-ethernet-port.jpg" alt="freeing an Ethernet port" caption="Getting an Ethernet port back" width=800 align="center" %}

Going from top to bottom on the back of the AT&T fiber modem, you can see the orange port is for connecting the device to the line that comes from my garage, and four Ethernet ports. Using that AT&T fiber router with my Linksys router meant that one of them (the one with the gray cable) had to be used for it. The other three ports went to my office, the Learning Center, and the Master Bedroom.

{% include image.html url="/images/amplifi-the-dark-fiber-saga-amplifi-plugging-in-the-amplifi-hd.jpg" alt="amplifi hd plugged in" caption="Hooking up the AmpliFi HD" width=800 align="center" %}

Since the AmpliFi HD had a WAN port for the AT&T modem and four Ethernet LAN ports, I could now connect to another of the pre-wired Ethernet ports in my house. I chose to send it to the Game Room to use with the X-Box.

## Turn On and . . . Turn Down?

I connected the USB C power cable to the AmpliFi HD router and then plugged the other end of it into the wall outlet. This started the boot up process.

{% include image.html url="/images/amplifi-the-dark-fiber-saga-amplifi-hd-plugged-in.jpg" alt="amplifi hd powered on" caption="Booting up the AmpliFi HD" width=800 align="center" %}

I immediately noticed a soft glow beneath the router. I've installed my fair share of routers, but this was the first one I've seen with mood lighting!

I downloaded and installed Android version of the [AmpliFi WiFi app](https://play.google.com/store/apps/details?id=com.ubnt.unifihome&hl=en) on my Pixel 2 XL. 

{% include image.html url="/images/amplifi-the-dark-fiber-saga-amplifi-wifi-app.png" alt="amplifi wifi app" caption="Success!" width=400 align="center" %}

After a few short taps the app let me know that my AmpliFi HD router was good to go.

During my research, I learned that it's best to position the mesh antennas on the opposite ends of a building with the router in between. This helps the mesh network to go through the router instead of trying to jump between meshes. I knew exactly where I wanted to put the AmpliFi HD antennas.

{% include image.html url="/images/amplifi-the-dark-fiber-saga-back-door-amplifi-antenna.jpg" alt="back door antenna" caption="The AmpliFi HD back door antenna" width=800 align="center" %}

I took one antenna out of the box and plugged it into an outlet near my back door.

{% include image.html url="/images/amplifi-the-dark-fiber-saga-front-door-amplifi-antenna.jpg" alt="front door antenna" caption="The AmpliFi HD front door antenna" width=800 align="center" %}

I took the other antenna and plugged it into an outlet between my office and the front door. My home network now looked like this.

{% include image.html url="/images/amplifi-the-dark-fiber-saga-mclaren-second-floor-amplifi.png" alt="amplifi on the second floor" caption="The AmpliFi'ed second floor" width=800 align="center" %}

The AmpliFi HD router took the place of the Linksys router upstairs.

{% include image.html url="/images/amplifi-the-dark-fiber-saga-mclaren-first-floor-amplifi.png" alt="amplifi on the first floor" caption="The AmpliFi'ed first floor" width=800 align="center" %}

The ground floor now had two mesh antennas near the front and back doors. This isn't immediately obvious from the picture, but the mesh antennas are opposite sides of the main living areas of the house with the router between them.

I went into my office to test the connection using my laptop connected via Ethernet to the AmpliFi HD router. This is when I discovered my first problem with the equipment.

{% include image.html url="/images/amplifi-the-dark-fiber-saga-speedtest-2.png" alt="speed test 2" caption="Speed test using wired connection to the AmpliFi HD router" width=300 align="center" %}

I ran wired speed tests that now consistently showed download and upload speeds around 500 Mbps over a wired connection to the AmpliFi HD router. This was approximately half of what I was getting with the Linksys router. I used my phone to check the wireless performance, and, while the overall WiFi speeds are faster and the dead spots were eliminated, I didn't want to get half the performance I was paying for just to use the AmpliFi HD router.

## The Fiber Darkens

I spent several minutes doing research while standing in the upstairs closet with the patch box, and a few articles suggested that the AmpliFi HD has to be in bridge mode to use fiber. In fact, [this support article by AmpliFi](https://help.amplifi.com/hc/en-us/articles/220771768-Does-AmpliFi-support-fiber-services-such-as-Google-Fiber-or-Fios-) stated:

{% include image.html url="/images/amplifi-the-dark-fiber-saga-amplifi-support-bridge-mode.png" alt="amplifi bridge mode" caption="Statement from AmpliFI about bridge mode" width=600 align="center" %}

I read the last sentence to mean that I had to call AT&T to have them turn the fiber modem into bridge mode. So, while still standing in the closet, I called AT&T support and, after a short hold period, walked the support representative through my problem. The representative first tried to send a "strong signal" to the router which, in my opinion, wouldn't solve the problem. However, I waited the ten minutes I was told it would take for the signal to finish, went downstairs, and did a speed test. I received the same diminished performance. I communicated this to the representative who put me on hold. I then noticed that the AmpliFi HD now presented the second problem with the equipment.

{% include image.html url="/images/amplifi-the-dark-fiber-saga-amplifi-hd-outage.jpg" alt="amplifi outage" caption="AmpliFi HD outage" width=800 align="center" %}

I noticed that my connection to the AmpliFi HD's WiFi access point disappeared so I switched to my phone's cellular connection. I was still on hold with the AT&T representative when I saw my phone automatically reconnect to the AmpliFi HD's WiFi access point. I opened the AmplFi HD app and decided to use the built-in chat support.

So, I was on the phone with AT&T support and live chatting with AmpliFi support. The AmpliFi support representative was very cordial and walked me through several troubleshooting steps, but none of them worked. I went downstairs and noticed that, despite the "No Internet connection" error on the AmpliFi HD router's display, my wired laptop still worked (but, still with ~500 Mbps speeds). However, after connecting to the AmpliFi HD's SSID, I couldn't browse anywhere online. So, the AmpliFI HD wireless connection was dark all over my house. 

The AT&T representative let me know he would install an update to the modem that would take several minutes. I hung up the phone and continued to troubleshoot with AmpliFi support, but, after several minutes, I had to leave my house for an appointment. I couldn't get back to the issue until later the next morning, and my family was not pleased that the entire wireless network was down and the only way to get online was the laptop in my office.

## A Bridge to Success

I returned to troubleshoot the issue the next day and soon saw this error when I connected to the AmpliFi HD access point:

{% include image.html url="/images/amplifi-the-dark-fiber-saga-att-router-behind-router-1.png" alt="att router error 1" caption="AT&T router behind router" width=600 align="center" %}

I clicked on the "Router / Router Information" link and went to this page:

{% include image.html url="/images/amplifi-the-dark-fiber-saga-att-router-behind-router-2.png" alt="att router error 1" caption="AT&T router behind router" width=600 align="center" %}

I surmised from this router that the AmpliFI HD was fighting with the AT&T modem to serve as a NAT router and assign IP addresses on the internal network. I went back to the initial page and typed in the router's password. After a couple of minutes, the AmpliFI HD returned to normal! Devices could connect to the AmpliFI HD's wireless network again.

However, I was still seeing reduced performance on my wired connection. I decided to use the AmpliFI WiFI app to put the router into bridge mode. After a brief delay, I found that wired connections to the AmpliFI HD finally returned to the 900 Mbps range.

## Drawbacks and Workarounds

So, after some troubleshooting, I was finally able to use the full capability of the AmpliFi HD's mesh network to cover my house while also receiving the speeds I expected from AT&t's Internet 1000 service. I felt this was a good outcome, but there were some drawbacks.

When the AmpliFi HD router operates in bridge mode, then that means you can't use a lot of the cool features of the device. You can't set up a guest network or group devices into user profiles (so, for example I can disconnect my son's phone and tablet from the network while allowing my daughter to use her phone and laptop). This is a serious drawback to bridge mode on the AmpliFi HD, but, until they issue a fix, you have to live without these features if you want to use a fiber service.

My wife and I like to entertain guests, and the lack of a guest mode really bugged me. However, I found a workaround. I took my old Linksys router and connected it to a switch which was downstream of the AmpliFi HD router. 

{% include image.html url="/images/amplifi-the-dark-fiber-saga-linksys-rebirth.jpg" alt="linksys reborn" caption="The Linksys router reborn" width=800 align="center" %}

I placed it on the stair case between the Game Room and Learning center in this configuration. However, I soon saw the same AT&T message indicating that the Linksys router was fighting with the upstream AT&T modem. So, I had to put it into bridge mode, too.

Bridge mode on the Linksys router also removed a lot of its capabilities. It could not longer create an explicit guest network or be configured to do things like port forwarding or create MAC filers. I also had to turn off DHCP on the Linksys router so that it could get an IP address from the upstream AT&T modem. However, it was important to leave DNS on so that it could assign IP addresses to the users who connected to it as it performed guest network duties. There are good instruction on putting Linksys routers into bridge mode [here](https://www.linksys.com/fi/support-article?articleNum=137888).

I also made the following modifications to have the Linksys router perform as a guest network:
  * I configured the router to obtain an IPv4 address automatically so that it gets an IP address from the AT&T fiber modem.
  * I turned off the 5 GHz band because I didn't want to provide a high speed guest pipe that would degrade the bandwidth of my house
  * So, I only kept the 2.4 GHz band which would provide better coverage.
  * I created password so that random people can't connect to the guest network.

## Final Thoughts

Before I share my final thoughts about the AmpliFi HD, remember that this is based on the specific needs I was trying to solve. I had a two story home with several wireless dead zones, and I needed to preserve the speed of the fiber service I had purchased.

Pros

* Erasure of dead zones
* August Smart Lock could be remotely accessed because it was near a mesh router. 
* Router has four Ethernet ports 
* Recent ability to use the mobile app anywhere to administer the router
* Lays the groundwork for other Ubiquiti solutions like the Teleport which is essentially their VPN solution

Cons
* Must use bridge mode if you have fiber service which takes away a lot of the features of the AmpliFi router

If you have a home the size of mine or smaller and don't use a fiber service, then I think the AmpliFi HD is a solid solution. It's easy to use and will expand your wireless coverage.

If you're trying to cover a structure with a larger footprint than my house and use a fiber service, then know that you'll have to make some pretty significant tradeoffs to use the AmpliFi HD. I was able to workaround what was, in my opinion, the main tradeoff (the loss of a guest network hosted by the AmpliFi HD router), and the system works to my satisfaction.