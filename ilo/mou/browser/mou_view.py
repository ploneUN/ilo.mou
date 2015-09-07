from five import grok
from plone.directives import dexterity, form
from ilo.mou.content.mou import Imou

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(Imou)
    grok.require('zope2.View')
    grok.template('mou_view')
    grok.name('view')

