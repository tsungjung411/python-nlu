from concept import Concept
from tagger.math.range.range import _Prerange
import math

class _GtEqPrerange(_Prerange):
    '''
    greater-than or equal-to prerange = [A, ] + suffix_modifier
    
    @since 2018.08.01
    @author tsungjung411@gmail.com
    '''
    
    def _on_create_concept(self, sentence, concept):
        head = concept.concept_values[self.FIELD_HEAD]
        head_value = head.concept_values['value']
        
        from_value = head_value
        to_value = math.inf
        concept.concept_values['value'] = [from_value, to_value]
    # end-of-def
    
# end-of-class
