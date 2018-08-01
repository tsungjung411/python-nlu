from tagger.zh_rTW.math.unit.metric_prefix.metric_prefix_unit import _MetricPrefixUnit
from tagger.zh_rTW.math.unit.metric_prefix.京 import 京

class 垓(_MetricPrefixUnit):
    '''
    @since 2018.07.25
    @author tsungjung411@gmail.com
    '''
    
    def get_synonym_list(self):
        return ['垓']
    # end-of-def
    
    def get_unit_size(self):
        return 1e20 # =100000000000000000000
    # end-def
    
    def get_dependent_tagger_list(self):
        return [京]
    # end-of-def
    
# end-of-class
