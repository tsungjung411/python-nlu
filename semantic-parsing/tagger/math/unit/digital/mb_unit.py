from concept import Concept
from tagger.math.unit.digital.digital_unit import _DigitalUnit

class MbUnit(_DigitalUnit):
    '''
    Defines the mega-byte-unit class for tagging.
    
    @since 2018.07.23
    @author tsungjung411@gmail.com
    '''
    
    def get_synonym_list(self):
        return ["mb"]
    # end-of-def
    
# end-of-class
