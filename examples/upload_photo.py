#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI

InstagramAPI = InstagramAPI("nari_bot_maker", "Wldbs0506!@")
InstagramAPI.login()  # login

photo_path = '../../file.jpg'
caption = "Sample photo instagram"
InstagramAPI.uploadPhoto(photo_path, caption=caption)
