import glob
from PIL import Image


bgw = Image.new("RGBA",(65, 65),"WHITE") 
bgb = Image.new("RGBA", (65, 65), (120, 170, 238))
bgw.save("w.png")
bgb.save("b.png")