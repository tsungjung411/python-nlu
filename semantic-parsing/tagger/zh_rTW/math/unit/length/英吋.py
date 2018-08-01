from tagger.math.unit.length.inch_unit import InchUnit

class 英吋(InchUnit):
    '''
    Defines the inch-unit class for tagging.
    
    @since 2018.07.22
    @author tsungjung411@gmail.com
    '''
    
    @classmethod
    def new_instance(klass):
        return 英吋()
    # end-of-def
    
    def get_synonym_list(self):
        return ['吋', '英吋']
    # end-of-def
    
# end-of-class
