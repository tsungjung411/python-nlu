from tagger.math.unit.metric_prefix.metric_prefix_unit import _MetricPrefixUnit

class kilo(_MetricPrefixUnit):
    '''
    Define the kilo unit.
    
    @since 2018.07.25
    @author tsungjung411@gmail.com
    '''
    
    def get_synonym_list(self):
        return ['k', 'kilo']
    # end-of-def
    
    def get_unit_size(self):
        return 1e3 # =1000
    # end-def
    
# end-of-class
