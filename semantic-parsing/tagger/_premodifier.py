from concept import Concept
from tagger._token import _Token

class _Premodifier(_Token): # 前修飾子
    '''
    Pattern: premodifier + posttoken
    
    Defines the abstract universal-object class that is used as 
    a pre-modifer.
    
    In English grammar, a premodifier is a modifier that is placed in
    the front of the word or phrase it limits or qualifies. 
    Modification by a premodifier is called premodification. 
    
    Four Major Types of Premodifiers
    "There are four major structural types of premodification in 
    English:
     - general adjective: big pillow, new pants, official 
       negotiations, political isolation
     - -ed participial modifier: restricted area, improved growth, 
       fixed volume, established tradition
     - -ing participial modifier: flashing lights, growing problem, 
       exhausting task
     - noun: staff room, pencil case, market forces, maturation 
       period
    @see https://www.thoughtco.com/premodifier-grammar-1691527
    
    A modifier placed before the head is called a premodifier; 
    one placed after the head is called a postmodifier.
    @see https://en.wikipedia.org/wiki/Grammatical_modifier
    
    @since 2018.08.02
    @author tsungjung411@gmail.com
    '''
    
    FIELD_PREMODIFIER = 'premodifier'
    FIELD_POSTTOKEN = 'posttoken'
    
    def get_premodifier_label(self):
        return self.FIELD_PREMODIFIER 
    # end-of-def
    
    def get_posttoken_label(self):
        return self.FIELD_POSTTOKEN
    # end-of-def
    
    def get_posttoken_concept_list(self):
        raise Exception(
            "need to implement 'get_posttoken_concept_list(self)' on "
            + str(self.__class__))
    # end-of-def
    
    def _tag(self, sentence, index = 0):
        region_start = None
        region_end = None
        at = 0
        synonym_list = self.get_synonym_list()
        
        # posttoekn might be at len(s) - 1, 
        # so premodifier should ends with len(s) - 2
        for i in range(index, sentence.length() - 1):
            
            synonym = self.match_prefix_synonym_at(
                sentence, i, synonym_list)
            if synonym == None:
                continue
            # end-of-if
            
            if type(synonym) == Concept:
                at = i + len(synonym.entity)
            else:
                at = i + len(synonym)
            # end-of-if
            if at >= sentence.length():
                continue # next i
            # end-of-if
            
            at = self._skip_whitespaces(sentence, at)
            if at >= sentence.length():
                continue # next i
            # end-of-if
            
            posttoken_concept_list = self.get_posttoken_concept_list()
            posttoken_concept = sentence.get_prefix_dominated_concept(
                at, *posttoken_concept_list)
            
            if posttoken_concept == None:
                continue
            # end-of-if
            
            region_start = i
            region_end = posttoken_concept.end
            self._tagging(
                sentence, 
                region_start, region_end, 
                synonym, posttoken_concept)
        # end-of-for
    # end-of-def
    
    def _tagging(self, sentence, 
                 region_start, region_end, 
                 premodifier: 'e.g. a number, like 至少 of "至少22k"', 
                 posttoken: 'e.g. a , like 22k of "至少22k"'):
        
        entity = sentence[region_start : region_end]
        entity = "".join(entity)

        # handled class: the derived class itself
        derived_class = self.__class__
        
        concept_values = {
            self.get_premodifier_label(): premodifier,
            self.get_posttoken_label(): posttoken
        }
        
        # creates a concept to wrap the above info
        concept = Concept(
            region_start, region_end, 
            entity, derived_class, concept_values)
        concept.sign(_Premodifier)
        self._on_create_concept(sentence, concept)

        sentence.add_concept(concept)
        self._on_add_concept(sentence, concept)
    # end-of-def
    
# end-of-class
