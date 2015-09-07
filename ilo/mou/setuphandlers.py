from collective.grok import gs
from ilo.mou import MessageFactory as _

@gs.importstep(
    name=u'ilo.mou', 
    title=_('ilo.mou import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('ilo.mou.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
