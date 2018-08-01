from tagger.math.unit.metric_prefix.metric_prefix_unit import _MetricPrefixUnit

class hecto(_MetricPrefixUnit):
    '''
    Define the hecto unit.
    
    @since 2018.07.25
    @author tsungjung411@gmail.com
    '''
    
    def get_synonym_list(self):
        return ['h', 'hecto']
    # end-of-def
    
    def get_unit_size(self):
        return 1e2 # =100
    # end-def
    
# end-of-class
