import qrcode

# Get link to redirect to
link = input("Insert link for QR Code or type text: ")

# Create QR Code
code = qrcode.make(link)

# Save Code
name = input("Type the save file name: ")
code.save(name)
