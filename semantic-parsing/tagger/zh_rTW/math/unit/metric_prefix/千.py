from tagger.zh_rTW.math.unit.metric_prefix._metric_prefix_unit import _MetricPrefixUnit
from tagger.zh_rTW.math.unit.metric_prefix.百 import 百

class 千(_MetricPrefixUnit):
    '''
    @since 2018.07.25
    @author tsungjung411@gmail.com
    '''
    
    def get_synonym_list(self):
        return ['千']
    # end-of-def
    
    def get_unit_size(self):
        return 1e3 # =1000
    # end-def
    
    def get_dependent_tagger_list(self):
        return [百]
    # end-of-def
    
# end-of-class
