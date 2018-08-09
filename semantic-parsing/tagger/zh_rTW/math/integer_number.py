from concept import Concept
#from tagger.math.integer_number import IntegerNumber as rawIntegerNumber
import tagger.math.integer_number

class IntegerNumber(tagger.math.integer_number.IntegerNumber):
    '''
    Defines the integer class for tagging.
    
    @since 2018.07.13
    @author tsungjung411@gmail.com
    '''
    
    def __init__(self):
        self.__CLASS = IntegerNumber
        super(self.__CLASS, self).__init__()
    # end-of-def
    
    def _tag(self, sentence, index = 0):
        region_start = index
        region_end = None
        ch = None
        digit_buffer = []
        
        for i in range(index, sentence.length()):
            ch = sentence[i]
            
            # cht: 零、壹、貳、參、肆、伍、陸、柒、捌、玖
            # chs: 零，壹，贰，参，肆，伍，陆，柒，捌，玖
            if ch in '零0０OＯ': 
                # digit: 0,０
                # alpha: O(half-width)Ｏ(full-width)
                digit_buffer.append('0')
                continue
            elif ch in '一壹ㄧ':
                # 一: 19968, 0x4e00
                # ㄧ: 12583, 0x3127 (注音符號 ㄧ　ㄨ　ㄩ)
                digit_buffer.append('1')
                continue
            elif ch in '二貳贰':
                digit_buffer.append('2')
                continue
            elif ch in '三參叁参':
                digit_buffer.append('3')
                continue
            elif ch in '四肆':
                digit_buffer.append('4')
                continue
            elif ch in '五伍':
                digit_buffer.append('5')
                continue
            elif ch in '六陸陆':
                digit_buffer.append('6')
                continue
            elif ch in '七柒':
                digit_buffer.append('7')
                continue
            elif ch in '八捌':
                digit_buffer.append('8')
                continue
            elif ch in '九玖':
                digit_buffer.append('9')
                continue
            else:
                region_end = i
                break;
            # end-of-if
        # end-of-for
        
        if region_end == None:
            region_end = sentence.length()
        # end-of-if
        
        if region_end > region_start:
            entity = sentence[region_start : region_end]
            entity = "".join(entity)
            concept_values = {
                'tagger': self.__class__,
                'value': int(''.join(digit_buffer)),
            }
            
            concept = Concept(
                region_start, region_end, 
                entity, self.__CLASS, concept_values)
            sentence.add_concept(concept)
        # end-of-if
        
        # not meet the ending, continue to tag?
        if region_end < sentence.length():
            if region_start == region_end:
                # not found the entity
                self._tag(sentence, region_end + 1)
            else:
                # found the entity
                self._tag(sentence, region_end)
        # end-of-if
    # end-of-def
    
    @classmethod
    def get_precedence(klass):
        return klass.PRECEDENCE_INTEGER_NUMBER
    # end-of-def
    
# end-of-class
