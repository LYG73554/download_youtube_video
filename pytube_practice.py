from pytube import YouTube

#建立物件辨識
#物件變數.streams.first().download()

yt = YouTube('https://www.youtube.com/watch?v=nb2qyZCFNU0')

#列印出影片擁有的格式
#print(yt.streams)
print('影片名稱:' + yt.title)
print('影片格式共有'+ str(len(yt.streams))+'種')
print('影片型態為 mp4 且影像及聲音皆有的影片：')
print(yt.streams.filter(subtype='mp4', progressive=True))
print('開始下載 mp4 的影片：')

#儲存位置，若沒有該資料夾則會新建立
pathdir = '/Users/hotingshao/Documents/pytube_downloads'
#download()一定要在first() or last() 後面
#yt.streams.filter(subtype='mp4', res='360p').last().download(pathdir)

yt.streams.filter(subtype='mp4',res='720p', progressive=True).first().download(pathdir)

print(  yt.title + "影片下載完成！ 影片儲存位置於：" + pathdir + "資料夾" )