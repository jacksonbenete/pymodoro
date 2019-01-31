# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 01:12:28 2016
http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=368970&type=card
@author: Muhammad
"""

import sys
from soi_db import Criatura

criatura = Criatura.query.filter_by(cmc=1).first()
sys.exit(criatura.name)


url ="http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=%r&type=card" % criatura.multiverseid

from PIL import Image
import requests
from io import BytesIO

response = requests.get(url)
img = Image.open(BytesIO(response.content))
img.show()