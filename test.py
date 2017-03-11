import youtube_dl
import cv2

#with youtube_dl.YoutubeDL({}) as ydl:
#    ydl.download(['https://www.youtube.com/watch?v=Mh4f9AYRCZY'])

vidcap = cv2.VideoCapture('video.mp4')
success,image = vidcap.read()
count = 0
success = True
while success:
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  cv2.imwrite("frames/frame%d.jpg" % count, image)
  count += 1