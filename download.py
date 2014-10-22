from HTMLParser import HTMLParser
import urllib, os, sys, time

images = []
directory = 'images'
download_progress = 0
path = 'http://sebastiandieser.com/dev/beegees/backgrounds/'

class AnchorParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for key, value in attrs:
                if key == 'href':
                    file_type = value.split('.')
                    ext = os.path.splitext(value)[1]
                    if ext == '.jpg' or ext == '.png':
                        images.append(value)

parser = AnchorParser()
data = urllib.urlopen(path).read()
parser.feed(data)

print images

# Create directory if it doesn't exist
if not os.path.exists(directory):
    print 'Directory "%s" does not exist.' % directory
    os.makedirs(directory)
    print 'Created directory: %s' % directory

# Progress hook
def report_hook(count, blockSize, totalSize):
    global download_progress
    download_progress += blockSize

    percent = float(download_progress)/totalSize
    percent = round(percent*100, 2)
    result = '%d%%' % percent

    sys.stdout.write(result)
    sys.stdout.flush()
    sys.stdout.write('\b\b\b\b')

# Download images
for image in images:
    print 'Downloading: %s%s' % (path, image)
    urllib.urlretrieve('%s%s' % (path, image), '%s/%s' % (directory, image), reporthook=report_hook)
    download_progress = 0
    print 'Done.\n'
