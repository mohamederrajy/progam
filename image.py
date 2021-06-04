import cv2
import matplotlib.pyplot as plt
 
img_path = r"test.png"
#img_path = r"C:\Users\kashz\AI Life\AI Projects - IAIP, PTs (Web + Channel)\02 OpenCV\000 opencv tutorial\green.jpg"
img = cv2.imread(img_path)
img = cv2.resize(img, (1280, 720))
 
# ## Histogram of Image 
# In[7]:
plt.hist(img.ravel(), bins=256, range = [0,255])
plt.show()

# ## Plot of all Channel using cv2.calcHist() Function
# In[10]:
colors = ('b', 'g', 'r')      
plt.figure(figsize=(16, 9))
for i, color in enumerate(colors):
    histogram = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histogram, color=color)
plt.show()
 
# In[11]:

colors = ('b', 'g', 'r')
img_ravel = [img[:, :, 0].ravel(), img[:, :, 1].ravel(), img[:,:, 2].ravel()] 
plt.hist(img_ravel, color=colors, label=colors, bins=256, range=[0,256])
plt.legend()
plt.show()