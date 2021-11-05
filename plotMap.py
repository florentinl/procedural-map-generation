from matplotlib import pyplot as plt
from PixelMap import PixelMap
from MapBuffer import MapBuffer

world = PixelMap(3000, 1000)
view = MapBuffer(world, 0, 0)
plt.imshow(view.get_view(0,0), cmap = 'terrain')
plt.show()
