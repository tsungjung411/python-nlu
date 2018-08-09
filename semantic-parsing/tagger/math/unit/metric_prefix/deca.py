from tagger.math.unit.metric_prefix._metric_prefix_unit import _MetricPrefixUnit

class deca(_MetricPrefixUnit):
    '''
    Define the deca unit.
    
    @since 2018.07.25
    @author tsungjung411@gmail.com
    '''
    
    def get_synonym_list(self):
        return ['da', 'deca', 'deka']
    # end-of-def
    
    def get_unit_size(self):
        return 1e1 # =10
    # end-def
    
# end-of-class
