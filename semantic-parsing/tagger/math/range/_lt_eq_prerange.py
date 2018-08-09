from concept import Concept
from tagger.math.range._lt_prerange import _LtPrerange
import math

class _LtEqPrerange(_LtPrerange):
    '''
    less-than or equal-to prerange: (∞, B] + postmodifier
    
    @since 2018.08.01
    @author tsungjung411@gmail.com
    '''
    
    def _on_custom_interval(self, sentence, concept):
        concept.concept_values[self.FIELD_BOUNDARY_LABEL] = \
            [self.FIELD_BOUNDARY_EXCLUSIVE, self.FIELD_BOUNDARY_INCLUSIVE]
    # end-of-def
    
# end-of-class
