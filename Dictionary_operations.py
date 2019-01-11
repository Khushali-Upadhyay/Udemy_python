Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Dictionary to map price of a camera to its brand
>>> priceOfCameras = {"sony":500, "nikon":600, "canon":700}
>>> priceOfCameras
{'sony': 500, 'nikon': 600, 'canon': 700}
>>> # dictionary.keys()
>>> priceOfCameras.keys()
dict_keys(['sony', 'nikon', 'canon'])
>>> # dictionary.values()
>>> priceOfCameras.values()
dict_values([500, 600, 700])
>>> # dictionary.copy()
>>> copyOfPriceOfCameras = priceOfCameras.copy()
>>> copyOfPriceOfCameras
{'sony': 500, 'nikon': 600, 'canon': 700}
>>># Deleting dictionary
>>> del priceOfCameras["sony"]
>>> priceOfCameras
{'nikon': 600, 'canon': 700}
>>> # dictionary.clear()
>>> priceOfCameras.clear()
>>> priceOfCameras
{}
>>> 
