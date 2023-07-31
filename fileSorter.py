import os
import collections
import shutil

# Add more extensions if needed
imgEx = ['png', 'gif', 'bmp', 'svg', 'jpg', 'jpeg']
audEx = ['mp3', 'wav', 'wma', 'aac', 'm4a', 'flac']
vidEx = ['mp4', 'mov', 'wmv', 'avi', 'm4v', 'h264']
docEx = ['pdf', 'txt', 'doc', 'csv', 'xls', 'xlsx', 'docx']
dmgEx = 'dmg'

# Change these according to personal requirements/preferences
imgDstn = 'Pictures'
audDstn = 'Music'
vidDstn = '/Volumes/2 to the 9/Videos'
docDstn = 'Desktop/Docs'
dmgDstn = os.getcwd()
othDstn = 'Documents'

# Base Setup
basePt = os.path.expanduser('~')
dwnld = os.path.join(basePt, 'Downloads')
fileMap = collections.defaultdict(list)


def createList():
	fileLst = os.listdir(dwnld)

	for fileNam in fileLst:
		if fileNam[0] != ".":
			fileExt = fileNam.split('.')[-1]
			fileMap[fileExt].append(fileNam)


# Moving to dirs based on file types
def moveFiles():
	for fileExt, fLst in fileMap.items():
		if fileExt in vidEx:
			for file in fLst:
				shutil.move(os.path.join(dwnld, file), os.path.join(vidDstn, file))
		elif fileExt in audEx:
			for file in fLst:
				os.rename(os.path.join(dwnld, file), os.path.join(basePt, audDstn, file))
		elif fileExt in imgEx:
			for file in fLst:
				os.rename(os.path.join(dwnld, file), os.path.join(basePt, imgDstn, file))
		elif fileExt in docEx:
			for file in fLst:
				os.rename(os.path.join(dwnld, file), os.path.join(basePt, docDstn, file))
		elif fileExt == dmgEx:
			for file in fLst:
				os.rename(os.path.join(dwnld, file), os.path.join(dmgDstn, file))
		else:
			for file in fLst:
				os.rename(os.path.join(dwnld, file), os.path.join(basePt, othDstn, file))
