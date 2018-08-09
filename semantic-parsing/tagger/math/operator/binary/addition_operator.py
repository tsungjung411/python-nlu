from concept import Concept
from tagger._tagger import _Tagger
from tagger.math.operator.binary._binary_operator import _BinaryOperator

class AdditionOperator(_BinaryOperator):
    '''
    @since 2018.08.06
    @author tsungjung411@gmail.com
    '''
    
    def get_synonym_list(self):
        return ['+', '＋', '﹢']
    # end-of-def
    
    def get_formal_operator(self):
        return '+'
    # end-of-if
    
    def evaluate(self, num1, num2):
        return num1 + num2
    # end-of-if
    
    @classmethod
    def get_precedence(klass):
        return klass.PRECEDENCE_ADDITION
    # end-of-def
    
# end-of-class
