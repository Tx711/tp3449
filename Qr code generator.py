import qrcode

img = qrcode.make("https://open.spotify.com/playlist/4VAZv6WjPB4yRnMIfiPMht?si=c448e7d3354a4fc1")
img.save("spotify.jpg")

img = qrcode.make("money money money")
img.save("wealth.jpg")

import cv2
d = cv2.QRCodeDetector()
val, points, straight_qrcode = d.detectAndDecode(cv2.imread("wealth.jpg"))
print(val)