from concept import Concept
from tagger.math.unit.length.length_unit import _LengthUnit

class InchUnit(_LengthUnit):
    '''
    Defines the inch-unit class for tagging.
    
    @since 2018.07.18
    @author tsungjung411@gmail.com
    '''
    
    def get_synonym_list(self):
        return ["''", '"']
    # end-of-def
    
# end-of-class
