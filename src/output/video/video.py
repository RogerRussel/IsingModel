from ..image.image import Image
import re
import os

class Video(Image):
    """
    Vido Output
    """

    framesPerSecond = "5"

    def __init__(self, model):
        Image.__init__(self, model)

    def makeVideo(self):

        cmd  = "ffmpeg -f image2 -r " + self.framesPerSecond
        cmd += " -i " + self.getFFMPEGNormalizedName()
        cmd += " -vcodec mpeg4"
        cmd += " -y " + self.normalizeName('mp4')

        os.system(cmd)

    def getFFMPEGNormalizedName(self):
        zfil = str(len(str(self.model.iterate)))
        name = self.normalizeName(self.sufix)
        regex = "^(.*?\.i-)\d+(\..*?)$"
        m = re.search(regex,name)
        return m.group(1) + "%0" + zfil + "d" + m.group(2)

    def cleanImages(self):
        cmdDelImages = "rm -f output/*png"
        os.system(cmdDelImages)

    def endOutput(self):
        self.makeVideo()
        self.cleanImages()
