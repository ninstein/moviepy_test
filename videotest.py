from moviepy.editor import VideoFileClip, concatenate_videoclips
 
clip1 = VideoFileClip("v2.mp4")
clip2 = VideoFileClip("v3.mp4")
#clip3 = VideoFileClip("v3.mp4")
 
finalclip = concatenate_videoclips([clip1, clip2])
finalclip.write_videofile("out2.mp4")
