from five import grok
from plone.directives import dexterity, form
from ilo.mou.content.sec import ISEC

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(ISEC)
    grok.require('zope2.View')
    grok.template('sec_view')
    grok.name('view')

