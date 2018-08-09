from concept import Concept
from tagger.math.range._prerange import _Prerange
import math

class _LtPrerange(_Prerange):
    '''
    less-than prerange: (∞, B) + postmodifier
    
    @since 2018.08.06
    @author tsungjung411@gmail.com
    '''
    
    def _on_custom_interval(self, sentence, concept):
        concept.concept_values[self.FIELD_BOUNDARY_LABEL] = \
            [self.FIELD_BOUNDARY_EXCLUSIVE, self.FIELD_BOUNDARY_EXCLUSIVE]
    # end-of-def
    
    def _on_custom_value_range(self, sentence, concept):
        pretoken = concept.concept_values[self.get_pretoken_label()]
        pretoken_value = pretoken.concept_values['value']
        
        try:
            from_value = -math.inf # from python 3.5
        except AttributeError:
            from_value = -float('inf')
        # end-of-try
        
        to_value = pretoken_value
        concept.concept_values['value'] = [from_value, to_value]
    # end-of-def   
    
# end-of-class
