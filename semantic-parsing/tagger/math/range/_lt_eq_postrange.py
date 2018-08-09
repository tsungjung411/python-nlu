from concept import Concept
from tagger.math.range._lt_postrange import _LtPostrange
import math

class _LtEqPostrange(_LtPostrange):
    '''
    less-than or equal-to postrange =  premodifier + (∞, B]
    
    @since 2018.08.07
    @author tsungjung411@gmail.com
    '''
    
    def _on_custom_interval(self, sentence, concept):
        concept.concept_values[self.FIELD_BOUNDARY_LABEL] = \
            [self.FIELD_BOUNDARY_EXCLUSIVE, self.FIELD_BOUNDARY_INCLUSIVE]
    # end-of-def
    
# end-of-class
