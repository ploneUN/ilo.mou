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
#from plone.multilingualbehavior.directives import languageindependent
from collective import dexteritytextindexer

from plone.autoform.directives import write_permission
from collective import dexteritytextindexer
from plone.formwidget.multifile import MultiFileFieldWidget

from ilo.mou import MessageFactory as _


# Interface class; used to define content-type schema.

class ISEC(form.Schema, IImageScaleTraversable):
    """
    Standard Employment Contracts
    """
    document_link = schema.TextLine(
           title=_(u"Document Link"),
           required=False,
        )

    source_info = schema.Text(
           title=_(u"Source"),
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

    sector = schema.TextLine(
           title=_(u"Sector"),
           required=False,
        )

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

    form.fieldset(
        'contract_conditions',
        label=u"Contract Conditions",
        fields=['employment_site','contract_duration','travel_home','min_wage','work_hrs','emp_injury','termination_grounds','dispute_settlmt','addtl_benefits']
    )
    
    employment_site = schema.Text(
           title=_(u"Site of Employment"),
           required=False,
        )

    contract_duration = schema.Text(
           title=_(u"Contract Duration"),
           required=False,
        )

    travel_home = schema.Text(
           title=_(u"Travel to from Home Country"),
           required=False,
        )

    min_wage = schema.Text(
           title=_(u"Minimum Wage"),
           required=False,
        )

    work_hrs = schema.Text(
           title=_(u"Working Hours"),
           required=False,
        )

    emp_injury = schema.Text(
           title=_(u"Employment Injury Sickness"),
           required=False,
        )

    termination_grounds = schema.Text(
           title=_(u"Grounds for Termination"),
           required=False,
        )

    dispute_settlmt = schema.Text(
           title=_(u"Dispute settlement"),
           required=False,
        )

    addtl_benefits = schema.Text(
           title=_(u"Additional Benefits"),
           required=False,
        )

    @invariant
    def validate_countries(self):
        if self.receiving_country and self.sender_country:
            if self.receiving_country == self.sender_country:
                raise Invalid(u"Same countries are selected on the country fields.")

    pass

alsoProvides(ISEC, IFormFieldProvider)
