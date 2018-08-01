class _Tagger:
    '''
    Defines the base class for tagging.
    
    @since 2018.07.13
    @author tsungjung411@gmail.com
    '''
    
    def __init__(self):
        self.__check_state()
    # end-of-def
    
    def __check_state(self):
        if hasattr(self.__class__, '_get_instance_flag') == False:
            raise Exception(
                "You cannot overwrite 'get_instance(klass)' on "
                + str(self.__class__))
        # end-of-if
    # end-of-def
    
    @classmethod
    def get_instance(klass, force = False):
        '''
        Input:
            klass: 
                the derived class, not this class
            force:
                force to create a new instance
                in general, this is used to test something changes
        '''
        klass._get_instance_flag = True
        
        field_name = '_{}__instance'.format(klass.__class__)
        if hasattr(klass, field_name) == False or force:
            klass._instance = klass.new_instance()
        # end-of-if
        return klass._instance
    # end-of-def
    
    @classmethod
    def new_instance(klass):
        #raise Exception(
        #    "need to implement 'new_instance(klass)' on "
        #    + str(klass))
        return klass()
    # end-of-def
    
    def tag(self, sentence, start = 0):
        self.__trigger_dependencies(sentence, start)
        
        __CLASS = self.__class__
        if sentence.has_tagged_by(__CLASS):
            return False
        # end-of-if
        
        # method reflection
        #method_name = '_{}__tag'.format(__CLASS.__name__)
        #method_pointer = self.__getattribute__(method_name)
        #method_pointer(sentence, start)
        self._tag(sentence, start) # run the implementation
        
        # indicates that the class has been executed
        sentence.register_tagger(__CLASS)
        return True
    # end-of-if
    
    def get_dependent_tagger_list(self):
        return None # default: no dependent
    # end-of-def
    
    def __trigger_dependencies(self, sentence, start):
        '''
        runs the dependent tagger first
        
        [target]: [dependency1, dependency2, ..., dependencyN]
        '''
        tagger_list = self.get_dependent_tagger_list()
        
        if tagger_list == None:
            return
        # end-of-if
        
        # casting from tuple/others to list
        tagger_list_type = type(tagger_list)
        if tagger_list_type == tuple:
            
            # the return type is tuple, let's cast it to list
            tagger_list = list(tagger_list)
            
        elif tagger_list_type != list:
            
            # the return type is a non-list-object type
            # let's cast it to list
            tagger_list = list(tagger_list)
            
        # end-of-if
        
        for tagger in tagger_list:
            instance = tagger.get_instance()
            if instance == None:
                raise Exception(
                    "The instance which gets from " + str(tagger)
                    + " should not be None")
            else:
                instance.tag(sentence, start)
            # end-of-if
        # end-of-if
    # end-of-def
    
    def _tag(self):
        raise Exception("need to implement '_tag(self)'")
    # end-of-def
    
    def _skip_whitespaces(self, sentence, at):
        '''
        Skips the whitespace from the give position(=at), and returns
        the next position where the character is a non-whitespace.
        
        Input:
            sentence: 
                the sentence object
            at:
                the start index from where to skip
        Usage:
            ```
                at = self._skip_whitespaces(sentence, at)
                if at >= sentence.length():
                    break
                # end-of-if
            ```
        
        @since 2018.07.25
        @author tsungjung411@gmail.com
        '''
        length = sentence.length()
        char = None
        
        while at < length:
            char = sentence[at]
            if char.isspace():
                # meets a whitespace character
                at += 1
            else:
                # meets an non-whitespace character
                break
            # end-of-if
        # end-of-while
        return at
    # end-of-def
    
    def _skip_whitespaces_reversely(self, sentence, at):
        '''
        Skips the whitespace reversely from the give position(=at), and returns
        the previous position where the character is a non-whitespace.
        
        Input:
            sentence: 
                the sentence object
            at:
                the start index from where to skip
        Usage:
            ```
                at = self._skip_whitespaces_reversely(sentence, at)
                if at < 0:
                    break
                # end-of-if
            ```
        
        @since 2018.07.25
        @author tsungjung411@gmail.com
        '''
        char = None
        
        while at >= 0:
            char = sentence[at]
            if char.isspace():
                # meets a whitespace character
                at -= 1
            else:
                # meets an non-whitespace character
                break
            # end-of-if
        # end-of-while
        return at
    # end-of-def
    
    @classmethod
    def get_precedence(klass):
        '''
        Defines the precedence of a tagger. For example,
        === from top ===
        - ...
        - Multiplication, Division, Remainder
        - Addition, Subtraction
        - Relation operators: <, <=, >, >=, ==, !=
        - ...
        - etc. See https://goo.gl/2f8ycY
        === to down ===
        
        We will sort these taggers by precedence to avoid dependency 
        issues.
        
        @since 2018.07.32
        @author tsungjung411@gmail.com
        '''
        return 0 # by default, no dependency
    # end-of-def
    
    PRECEDENCE_INTEGER_NUMBER = 99 # 123
    PRECEDENCE_REAL_NUMBER = 98    # 123.456
    PRECEDENCE_NUMBER_SCALE = 97   # 22k, 1.234k
    PRECEDENCE_UNIT = 96           # 100k USD
    PRECEDENCE_RANGE = 95          # around 100k USD
    
# end-of-class
