import ascii

image = "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"

art = ascii.loadFromUrl(image=image, color=False)

print(art)
