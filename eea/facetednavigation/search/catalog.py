import logging
from zope.interface import implements
from Products.CMFCore.utils import getToolByName
from interfaces import IFacetedCatalog
logger = logging.getLogger('eea.facetednavigation.search.catalog')

class FacetedCatalog(object):
    """ Get adapted catalog if eea.reports installed
    """
    implements(IFacetedCatalog)

    def __call__(self, context, **query):
        ctool = getToolByName(context, 'portal_faceted', None)
        if ctool:
            search = ctool.search
        else:
            logger.debug('portal_faceted not present, using portal_catalog')
            ctool = getToolByName(context, 'portal_catalog')
            search = ctool.searchResults
        return search(**query)
