class TemplatesStorage:
    def __init__(self):
        self.Data = dict()
        self.Types = list()

    def addtemplate(self, template, name, type):
        if type in self.Types:
            self.Data[type][name] = template
        else:
            self.Types.append(type)
            self.Data[type] = dict()
            self.Data[type][name] = template

    def getbyname(self, name):
        for key, val in self.Data:
            if name in val:
                return val[name]

        return None

    def gettypenames(self, type):
        if type in self.Data:
            return self.Data[type]
        else:
            return None