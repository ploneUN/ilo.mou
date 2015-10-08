from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

from plone.autoform.directives import write_permission
#from plone.multilingualbehavior.directives import languageindependent
from collective import dexteritytextindexer
from plone.formwidget.multifile import MultiFileFieldWidget

from ilo.mou import MessageFactory as _


# Interface class; used to define content-type schema.

class Imou(form.Schema, IImageScaleTraversable):
    """
    mou
    """

    document_link = schema.TextLine(
           title=_(u"Document Link"),
           required=False,
        )

    sender_country = schema.Choice(
           title=_(u"Sending Country"),
           description=_(u"Country of Origin"),
           vocabulary="ilo.mou.country",
           required=True,
        )

    receiving_country = schema.Choice(
           title=_(u"Receiving Country"),
           description=_(u"Destination Country"),
           vocabulary="ilo.mou.country",
           required=True,
        )

#    sector = schema.TextLine(
#           title=_(u"Sector"),
#           required=False,
#        )

    year_signed = schema.TextLine(
           title=_(u"Year Signed"),
           required=False,
        )

    write_permission(multifile='cmf.ReviewPortalContent')
    form.widget(multifile=MultiFileFieldWidget)
    multifile = schema.List(
            title=_(u"File Attachment"),
            required=False,
            value_type=NamedFile(),
        )

    @invariant
    def validate_countries(self):
        if self.receiving_country and self.sender_country:
            if self.receiving_country == self.sender_country:
                raise Invalid(u"Same countries are selected on the country fields.")
    pass

alsoProvides(Imou, IFormFieldProvider)
