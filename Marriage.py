class Mariage(object):
    def __init__(self, item = None):
        if item is not None:
            self.item = item
        else:
            self.item = None
        self.parentLinks = []
        self.childLinks = []
        self.sideLinks = []

    def addLinkToParent(self, parent):
        status = 0
        status = status + self.addLinkToParentOneWay(parent)
        status = status + parent.addLinkToChildOneWay(self)

        return status

    def addLinkToParentOneWay(self, parent):
        status = 0
        if self.containsParentLink(parent) is True:
            status = 1
        else:
            self.parentLinks.append(parent)

        return status

    def removeLinkToParent(self, parent):
        status = 0
        status = status + self.removeLinkToParentOneWay(parent)
        status = status + parent.removeLinkToChildOneWay(self)

        return status

    def removeLinkToParentOneWay(self, parent):
        status = 0
        if self.containsLinkToParent(parent):
            self.parentLinks.remove(parent)
        else:
            status = 1

        return status

    def addLinkToChild(self, child):
        status = 0
        status = status + self.addLinkToChildOneWay(child)
        status = status + child.addLinkToParentOneWay(self)

        return status

    def addLinkToChildOneWay(self, child):
        status = 0
        if self.containsLinkToChild(child) is True:
            self.childLinks.append(child)
        else:
            status = 1

        return status


    def removeLinkToChild(self, child):
        status = 0
        status = status + self.removeLinkToChildOneWay(child)
        status = status + child.removeLinkToParentOneWay(self)

        return status

    def removeLinkToChildOneWay(self, child):
        status = 0
        if self.containsLinkToChild(child) is True:
            self.childLinks.remove(child)
        else:
            status = 1

        return status

    def addSideLink(self, side):
        status = 0
        self.addSideLinkOneWay(side)
        side.addSideLinkOneWay(self)

        return status


    def addSideLinkOneWay(self, side):
        status = 0
        if self.containsSideLink(side) is not True:
            self.sideLinks.append(side)
        else:
            status = 1

        return status

    def removeSideLink(self, side):
        status = 0
        status = status + self.removeSideLinkOneWay(side)
        status = status + side.removeSideLinkOneWay(self)

        return status

    def removeSideLinkeOneWay(self, side):
        status = 0
        if self.containsSideLink(side) is True:
            self.sideLinks.remove(side)
        else:
            status = 1

        return status

    def containstLinkToParent(self, parent):
        contains = False
        if parent in self.parentLinks:
            contains = True

        return contains

    def containsLinkToChild(self, child):
        contains = False
        if child in self.childLinks:
            contains = True

        return contains

    def containsSideLink(self, side):
        contains = False
        if side in self.sideLinks:
            contains = True

        return contains

    def sideLinksIsEmpty(self):
        return not self.sideLinks

    def linksToChildIsEmpty(self):
        return not self.childLinks

    def linksToParentIsEmpty(self):
        return not self.parentLinks

    def equals(self, comparedNode):
        return self.item.equals(comparedNode.item)

    def getItem(self):
        return self.item

    def setItem(self, item):
        self.item = item

    def getChildLinks(self):
        return self.childLinks

    def setChildLinks(self, childLinks):
        self.childLinks = childLinks

    def getParentLinks(self):
        return self.parentLinks

    def setParentLinks(self, parentLinks):
        self.parentLinks = parentLinks

    def getSideLinks(self):
        return self.sideLinks

    def setSideLinks(self, sideLinks):
        self.sideLinks = sideLinks