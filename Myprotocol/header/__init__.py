class Header:
    #头部域
    def __init__(self, Content_Type, Content_Encoding):
        self.Content_Type = Content_Type
        self.Content_Encoding = Content_Encoding
    def showType(self):
        return self.Content_Type
    def showEncoding(self):
        return self.Content_Encoding