from tagger.math.unit.metric_prefix._metric_prefix_unit import _MetricPrefixUnit

class mega(_MetricPrefixUnit):
    '''
    Define the mega unit.
    
    @since 2018.07.25
    @author tsungjung411@gmail.com
    '''
    
    def get_synonym_list(self):
        return ['m', 'mega'] 
    # end-of-def
    
    def get_unit_size(self):
        return 1e6
    # end-def
    
# end-of-class
