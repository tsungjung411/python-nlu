from tagger.math.unit.metric_prefix.metric_prefix_unit import _MetricPrefixUnit

class giga(_MetricPrefixUnit):
    '''
    Define the giga unit.
    
    @since 2018.07.25
    @author tsungjung411@gmail.com
    '''
    
    def get_synonym_list(self):
        return ['g', 'giga'] 
    # end-of-def
    
    def get_unit_size(self):
        return 1e9
    # end-def
    
# end-of-class
