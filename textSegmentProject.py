import textSegmentionModule as ts

class Text :
  def __init__(self , textID, textLength, textBody, textTitle, listOfSegments):
    self.textTD = textID
    self.textLength = textLength
    self.textBody = textBody
    self.textTitle = textTitle
    self.listOfSegments=listOfSegments


class Segment :
  def __init__(self , segmentID, segmentText, segmentLength, positionStart, positionEnd):
    self.segmentID = segmentID
    self.segmentText = segmentText
    self.segmentLength = segmentLength
    self.positionStart = positionStart
    self.positionEnd = positionEnd

def textSegmentionWork(listOfSegments):
    textID = id(listOfSegments)
    textTitle = "".join(ts.findTextTitle(listOfSegments))
    textBody = " ".join(ts.findTextBody(listOfSegments))
    textLength = ts.findTextLength(fileText)
    Text(textID, textLength, textBody, textTitle, listOfSegments)

    green = '\033[32m'
    bold = '\033[1m'
    end = '\033[m'

    #print text info
    print(green+bold+"Text info:"+end)
    print(green+bold+"Full text:"+end)
    start = 0
    for line_number, sentence in enumerate(listOfSegments, start=start + 1):
        sentence = sentence.strip("\n")
        print(f"{line_number:2}: {sentence}")
    print()
    print(green+bold+"Text id: "+end, textID)
    print(green+bold+"Text length: "+end, textLength)
    print(green+bold+"List of segments: "+end, listOfSegments)
    print(green+bold+"Text title: "+end, textTitle)
    print(green+bold+"Text body: "+end, textBody)

    num = 0
    for segment in listOfSegments:
        num += 1
        segmentID = id(segment)
        segmentText = segment
        segmentLength = ts.findTextLength(segment)
        positionStart = ts.findPositionStart(segment, listOfSegments)
        positionEnd = ts.findPositionEnd(segment, listOfSegments)
        Segment(segmentID, segmentText, segmentLength, positionStart, positionEnd)

        #print segment info
        print(bold+"Segment", num, " info:"+end)
        print(green+bold+"Segment id: "+end, segmentID)
        print(green+bold+"Segment length: "+end, segmentLength)
        print(green+bold+"Segment text: "+end, segmentText)
        print(green+bold+"Position start: "+end, positionStart)
        print(green+bold+"Position end: "+end, positionEnd)
        print()

# full text
fileText = ts.loadingText("texts/0_3.txt")
listOfSegments = ts.hierarchicalTextClustering(fileText,8)
textSegmentionWork(listOfSegments)