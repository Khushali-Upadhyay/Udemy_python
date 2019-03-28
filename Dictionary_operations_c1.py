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
