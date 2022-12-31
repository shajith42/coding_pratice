width = int(input()) #widths is odd and 0 < width < 50
t = width*2
c = "H"
#top arrow
for a in range(1,t,2):
    print((c*a).center(t))
#top pillars
for a in range(width+1):
     print((c*width).center(t)+" ".center(t)+(c*width).center(t))
#center
for a in range((width+1)//2):
     print((c*width*5).center(t*3))
#bottom pillars
for a in range(width+1):
     print((c*width).center(t)+" ".center(t)+(c*width).center(t))
#bottom arrow
for a in reversed(range(1,t,2)):
    print(" ".center(t*2)+(c*a).center(t))