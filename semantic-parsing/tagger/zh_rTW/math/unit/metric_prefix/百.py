from tagger.zh_rTW.math.unit.metric_prefix.metric_prefix_unit import _MetricPrefixUnit
from tagger.zh_rTW.math.unit.metric_prefix.十 import 十

class 百(_MetricPrefixUnit):
    '''
    @since 2018.07.25
    @author tsungjung411@gmail.com
    '''
    
    def get_synonym_list(self):
        return ['百']
    # end-of-def
    
    def get_unit_size(self):
        return 1e2 # =100
    # end-def
    
    def get_dependent_tagger_list(self):
        return [十]
    # end-of-def
    
# end-of-class
