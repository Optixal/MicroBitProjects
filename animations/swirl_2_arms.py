from microbit import *

imgs = [
	Image('09000:90090:90909:09009:00090:'),
	Image('00090:90909:90909:90909:09000:'),
	Image('00990:09009:00900:90090:09900:'),
	Image('09990:90000:09990:00009:09990:')
]
display.show(imgs, delay=75, loop=True)