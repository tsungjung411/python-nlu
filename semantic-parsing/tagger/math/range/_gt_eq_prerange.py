from concept import Concept
from tagger.math.range._gt_prerange import _GtPrerange
import math

class _GtEqPrerange(_GtPrerange):
    '''
    greater-than or equal-to prerange: [A, ∞) + postmodifier
    
    @since 2018.08.01
    @author tsungjung411@gmail.com
    '''
    
    def _on_custom_interval(self, sentence, concept):
        concept.concept_values[self.FIELD_BOUNDARY_LABEL] = \
            [self.FIELD_BOUNDARY_INCLUSIVE, self.FIELD_BOUNDARY_EXCLUSIVE]
    # end-of-def
    
# end-of-class
