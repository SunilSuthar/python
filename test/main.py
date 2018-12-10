import ascii
image = "https://qph.fs.quoracdn.net/main-thumb-145200004-200-mkpyjjwrfttxdmtmglfuendnvnjufipo.jpeg"

art = ascii.loadFromUrl(image, color=False)

print(art)