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


    #print text info
    print("Text info:")
    print("Full text:")
    start = 0
    for line_number, sentence in enumerate(listOfSegments, start=start + 1):
        sentence = sentence.strip("\n")
        print(f"{line_number:2}: {sentence}")
    print()
    print("Text id: ", textID)
    print("Text length: ", textLength)
    print("List of segments: ", listOfSegments)
    print("Text title: ", textTitle)
    print("Text body: ", textBody)

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
        print("Segment", num, " info:")
        print("Segment id: ", segmentID)
        print("Segment length: ", segmentLength)
        print("Segment text: ", segmentText)
        print("Position start: ", positionStart)
        print("Position end: ", positionEnd)
        print()

# full text
fileText = ts.loadingText("texts/0_3.txt")
listOfSegments = ts.hierarchicalTextClustering(fileText,8)
textSegmentionWork(listOfSegments)
