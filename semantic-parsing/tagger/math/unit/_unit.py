from concept import Concept
from tagger._token import _Token

class _Unit(_Token):
    '''
    Defines the abstract unit class for tagging.
    
    @since 2018.07.23
    @author tsungjung411@gmail.com
    @see http://tw.bestconverter.org
    @see https://www.thermexcel.com/english/tables/unit_con.htm
    '''
    
    @classmethod
    def get_precedence(klass):
        return klass.PRECEDENCE_UNIT
    # end-of-def
    
    def create_virtual_concept(self):
        '''
        Creates a virtual concept for some adjectives.
        '''
        
        entity = self.get_synonym_list()[0]
        return Concept(
            start = -1, end = -1, 
            entity = entity, 
            concept_type = self.__class__,
            concept_values = {'unit': entity}
        )
    # end-of-def
# end-of-class
