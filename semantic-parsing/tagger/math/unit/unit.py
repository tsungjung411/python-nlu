from concept import Concept
from tagger.object import _Object

class _Unit(_Object):
    '''
    Defines the abstract unit class for tagging.
    
    @since 2018.07.23
    @author tsungjung411@gmail.com
    @see http://tw.bestconverter.org
    @see https://www.thermexcel.com/english/tables/unit_con.htm
    '''
    
    def get_entity_label(self):
        return 'unit'
    # end-of-def
    
    @classmethod
    def get_precedence(klass):
        return klass.PRECEDENCE_UNIT
    # end-of-def
    
# end-of-class
