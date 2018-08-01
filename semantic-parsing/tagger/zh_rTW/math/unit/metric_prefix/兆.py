from tagger.zh_rTW.math.unit.metric_prefix.metric_prefix_unit import _MetricPrefixUnit
from tagger.zh_rTW.math.unit.metric_prefix.億 import 億

class 兆(_MetricPrefixUnit):
    '''
    @since 2018.07.25
    @author tsungjung411@gmail.com
    '''
    
    def get_synonym_list(self):
        return ['兆']
    # end-of-def
    
    def get_unit_size(self):
        return 1e12 # =1000000000000
    # end-def
    
    def get_dependent_tagger_list(self):
        return [億]
    # end-of-def
    
# end-of-class
