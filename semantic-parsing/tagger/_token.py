from concept import Concept
from tagger._tagger import _Tagger

class _Token(_Tagger):
    '''
    Defines the abstract universal-object class for tagging.
    
    @since 2018.07.24
    @author tsungjung411@gmail.com
    '''
    
    def get_synonym_list(self):
        raise Exception(
            "need to implement 'get_synonym_list(self)' on "
            + str(self.__class__))
    # end-of-def
    
    def match_prefix_synonym_at(self, sentence, at, 
            synonym_list = None) -> Concept or str:
        '''
        Matches the concrete prefix-synonym at runtime, and return 
        the matched synonym.
        
        where the synpnym can be a general concept, like '_Unit'
        '''
        
        if synonym_list == None:
            synonym_list = self.get_synonym_list()
        # end-of-if
        
        for synonym in synonym_list:
            synonym_type = type(synonym)
            
            if synonym_type == type: # inspect.isclass(synonym)
                # synonym is a general concept, like '_Unit'
                # synonym will be decided runtime
                concept = sentence.get_prefix_dominated_concept(at, synonym)
                if concept != None:
                    return concept
                # end-of-if
                
            elif synonym_type == str:
                if sentence.startswith(at, synonym):
                    return synonym
                # end-of-if
                
            else:
                raise Exception('not support this type of synonym'
                    + '\n - synonym: ' + str(synonym)
                    + '\n - type: ' + str(synonym_type))
            # end-of-if
        # end-of-for
        
        return None
    # end-of-def
    
    def _tag(self, sentence, index = 0):
        region_start = None
        region_end = None
        ch = length = None
        
        synonym_list = self.get_synonym_list()
        for i in range(index, sentence.length()):
            
            length = 0 # the length of a synonym
            for synonym in synonym_list:
                if sentence.startswith(i, synonym):
                    length = len(synonym)
                    break
                # end-of-if
            # end-of-for
            
            if length == 0:
                continue
            # end-of-if
            
            region_start = i
            region_end = i + length
            
            # entity: '公', '尺' -> '公尺'
            entity = sentence[region_start : region_end]
            entity = "".join(entity)
            
            # handled class
            derived_class = self.__class__
            concept_type = derived_class
            
            # creates an empty values (i.e. no meaning)
            concept_values = {}
            
            # creates a concept to wrap the above info
            concept = self._create_concept(
                region_start, region_end, 
                entity, derived_class, concept_values)
            if concept == None:
                continue # the concept is rejected
            # end-of-if
            self._on_create_concept(sentence, concept)
            
            # adds the concept on the sentence
            sentence.add_concept(concept)
            self._on_add_concept(sentence, concept)
    # end-of-def
    
    def _create_concept(self, region_start, region_end, 
            entity, concept_type, concept_values) -> Concept:
        '''
        Creates a concept to wrap the above info.
        
        If the concept is None, it means the concept is rejected.
        '''
        return Concept(region_start, region_end, 
                    entity, concept_type, concept_values)
    # end-of-def
    
    def _on_create_concept(self, sentence, concept) -> None:
        '''
        Define the callback to let the clients have a chance to 
        update the concept, such as:
        
          - metric_prefix_unit (30k->30000)
          - adds the meaning for the current token
        
        @since 2018.07.24
        @author tsungjung411@gmail.com
        '''
    # end-of-def
    
    def _on_add_concept(self, sentence, concept) -> None:
        '''
        Define the callback to let the clients have a chance to 
        listen to the add-concept event, such as:
        
            - 2萬5, concept='2萬', we also need to handle '5'
              where 5 means 5000 (=5*10000/10)
              
            - 2千5, concept='2千', we also need to handle '5'
              where 5 means 500 (=5*1000/10)
        
        @since 2018.07.26
        @author tsungjung411@gmail.com
        '''
    # end-of-def
        
# end-of-class
