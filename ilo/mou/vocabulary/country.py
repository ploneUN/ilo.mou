from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility

from p01.vocabulary.country import ISO3166Alpha2CountryVocabulary
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
import copy

class Country(grok.GlobalUtility):
    grok.name('ilo.mou.country')
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        results = []
        data = []
        vocabs = ISO3166Alpha2CountryVocabulary(context)
        for vocab in vocabs:
            title = vocab.title
            if title in ('Hong Kong', 'Taiwan'):
                title += ' (China)'
            results.append({'title':title, 'token':vocab.token, 'value':vocab.value})
        if results:
            results.sort(key=lambda k: k['title'])
        for result in results:
            data.append(SimpleTerm(value=result['value'], token=result['token'], title=result['title']))
        return SimpleVocabulary(data)
            