from concept import Concept
from tagger.object import _Object, _Postmodifier
from tagger.math.real_number import RealNumber
from tagger.math.integer_number import IntegerNumber

class _Range(_Object):
    '''
    @since 2018.08.01
    @author tsungjung411@gmail.com
    '''
    
    def get_entity_label(self):
        return 'range'
    # end-of-def
    
    def _get_head_concept_list(self):
        return [IntegerNumber, RealNumber]
    # end-of-def
    
    def _on_create_concept(self, sentence, concept):
        raise Exception(
            "need to implement '_on_create_concept(self)' on "
            + str(self.__class__))
    # end-of-def
    
    @classmethod
    def get_precedence(klass):
        return klass.PRECEDENCE_RANGE
    # end-of-def
    
# end-of-class

# ===================================================================

class _Prerange(_Range, _Postmodifier):
    
    def _on_create_concept(self, sentence, concept):
        raise Exception(
            "need to implement '_on_create_concept(self)' on "
            + str(self.__class__))
    # end-of-def
    
# end-of-class


    
