author = 'Liu Lei'
import shutil, os, re

dataPattern = re.compile(r'^(.*?)((19|20)\d\d)-((0|1)?\d)-((0|1|2|3)?d)(.*?)$', re.VERBOSE)
for amerFilename in os.listdir('.'):
    mo = dataPattern.search(amerFilename)
    if mo == None:
        continue

        beforePart = mo.group(1)
        yearPart = mo.group(2)
        monthPart = mo.group(4)
        datePart = mo.group(6)
        afterPart = mo.group(8)
        euorFilename = beforePart + datePart + '-' + monthPart + '-' + yearPart + afterPart
        absWorkingDir = os.path.abspath('.')
        amerFilename = os.path.join(absWorkingDir, amerFilename)
        euorFilename = os.path.join(absWorkingDir, euorFilename)
        print('Renaming "%s" to "%s"...' % (amerFilename, euorFilename))