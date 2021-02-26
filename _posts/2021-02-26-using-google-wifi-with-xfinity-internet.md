---
title: 'Using Google Wifi with Xfinity Internet'
author: anjuan
layout: post
date: "2021-02-26"
permalink: /blog/using-google-wifi-with-xfinity-internet/
categories:
  - Tech
excerpt: "I recently had to switch my ISP to Xfinity Internet. Here's how I got it to work with my Google Wifi mesh network."
comments: true
---

{% include image.html url="/images/google-wifi-xfinity.png" alt="Google Wifi Points and Xfinity logo" caption="Google Wifi and Xfinity make a great home internet combination." %}

The power to my home went out during the [snow storm that crippled Texas in mid-February 2021](https://www.cbsnews.com/news/texas-winter-storm-uri-costs/), and my house went without power for 36 hours. After our electricity was restored, I discovered that the internet service provider (ISP) I used at the time wasn't working. After waiting for several days and being regularly reassured that my connectivity would be restored "soon", I finally decided to make the switch. According toe [Nextdoor](https://nextdoor.com/), my neighbors who were using Comcast's Xfinity internet service were back online as soon as the power came back on. I signed up for Xfinity's gigabit service and walked into a store to pick up my [xFi gateway](https://www.theverge.com/2020/1/6/21035595/comcast-wifi-6-new-router-gateway-xfi-advanced-security-ces-2020) (a combination modem and router).

I've use [Google Wifi](https://store.google.com/us/product/google_wifi_2nd_gen) (not to be confused with [Nest Wifi](https://store.google.com/us/product/nest_wifi)) for years to run the mesh network inside of my home. I'm really happy with how the service manages my wireless network, and it's regularly updated with security improvements and features. So, I had configure my Google Wifi setup to work with Xfinity. Here's how I did it.

## **Connect the Xfinity Hardware**

Before doing anything, I unplugged everything in the patch closet in my home. My patch closet is where all of the cables that carry internet, phone, security, and television signals converge. I wanted to start clean so I unplugged (both signal and power) the modem from my previous ISP as well as my primary Google Wifi router. I also went through my house and unplugged the Google Wifi nodes in my house.

I setup the xFi gateway in my patch closet and screwed in the coax cable that carries the internet signal into my home. I also connected the xFi to power and watched the LED lights on top start flashing. I had already downloaded the [Xfinity](https://play.google.com/store/apps/details?id=com.xfinity.digitalhome) app on my phone so I launched it and logged in using my credentials. The app directed me to scan the QR code on the bottom of the Xfi, and I did so. The LED lights flashed until finally settling on a constant white color.

I used the app to configure the wifi network being broadcast by the XFi. I knew I wouldn't permanently use this wireless network since I wanted to eventually use Google Wifi. However, I wanted to confirm that I could get online using the Xfinity service before trying to switch over to the

## **Put the Xfinity Xfi into Bridge Mode**

I wanted Network Address Translation (NAT) to be done by my primary Google Wifi router so I needed to put the xFi into bridge mode. This would disable the NAT capability of the XFi device and avoid double NAT routing with Google Wifi.

Putting the xFi into bridge mode required access the admin panel which isn't possible using the wireless network. You have to physically connect a computer to the device. So, I ran a ethernet cable from the xFi to my MacBook Pro. After doing that, I opened a web browser and navigated to 10.0.0.1 to access the admin panel for the xFi.

{% include image.html url="/images/xFi-admin-panel.png" alt="xFi Admin Panel" caption="The xFi Admin Panel." %}

Since this was the first time I did this, the default username (admin) and password (password) allowed me to login. I immediately changed the default password to a secure version and then used the admin page to enable bridge mode. I toggled bridge mode on.

Keep in mind that a few things happen when you enable bride mode on the xFi gateway. First, the device's wireless network is disabled. Second, you can no longer use the other ethernet ports on the xFi. So, the gateway just becomes a passthrough for internet access to flow to the Google Wifi router.

## **Connect the Google Wifi Primary Access Point**

Google Wifi lets any wireless point act as the router so I picked the one that I used as the router with my previous ISP. I ran an ethernet cable between the Google Wifi router and the xFi which allowed me to setup my permanent wireless network.

I used the Google Home app to inspect my wireless network and verify that I was getting the download and upload speeds I was expecting. I saw that I would get download speeds of about 800 Mbps and upload speeds of about 30 Mbps. My previous ISP was a symmetrical service with fast upload and download speeds, but I felt it was more important to have a stable internet connection rather than a blazingly fast one.

## **Add Ports Via a Switch**

One major reason why I use Google Wifi instead of Google Nest Wifi is the ability to use internet backhaul. The Google Nest nodes don't have any ethernet ports at all so they can only use wireless communication to the router. Every Google Wifi node has two ethernet ports: one for internet into the device and one for internet out of the device. This allows every node to used a wired connection for communicating over the mesh instead of adding overhead to the wireless network.

Since the xFi's ethernet ports in bridge mode are disabled, I had to find another way to add ethernet ports to my setup. So, I purchased a 5-port gigabit ethernet switch which I put between the xFi and the primary Google Wifi router (using port 1 on the switch). I then connected the ethernet cables that led to the other Google Wifi nodes to the other four ports.

{% include image.html url="/images/google-wifi-app.png" alt="Google Wifi App" caption="My beautiful Google Wifi Mesh Network." width=300 %}

The screenshot shows "Nest Wifi" even though I'm using Google Wifi equipment. 

I've been happy with the results of my Google Wifi network powered by Xfinity internet.

{% include image.html url="/images/patch-closet.jpg" alt="Patch Closet" caption="It's not pretty, but it works." %}