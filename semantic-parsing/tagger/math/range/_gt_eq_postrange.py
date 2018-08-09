from concept import Concept
from tagger.math.range._gt_postrange import _GtPostrange
import math

class _GtEqPostrange(_GtPostrange):
    '''
    greater-than or equal-to postrange: premodifier + [A, ∞)
    
    @since 2018.08.07
    @author tsungjung411@gmail.com
    '''
    
    def _on_custom_interval(self, sentence, concept):
        concept.concept_values[self.FIELD_BOUNDARY_LABEL] = \
            [self.FIELD_BOUNDARY_INCLUSIVE, self.FIELD_BOUNDARY_EXCLUSIVE]
    # end-of-def
    
# end-of-class
