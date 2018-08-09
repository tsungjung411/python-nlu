from tagger.math.unit._unit import _Unit

class _MassUnit(_Unit):
    '''
    Defines the abstract mass-unit class for tagging.
    
    Attention not to confuse mass and weight.

    The mass (kg) is a intrinsic characteristic of the body and is 
    measured in kilogram. (質量是一種身體內在特徵，以公斤為單位。) 

    Weight is a force which depends on terrestrial attraction and it 
    is the equivalent of the mass of a body by the acceleration of 
    gravity (9.80665 at the sea level) and is measured in Newton [N].
    (重量是一種依賴於地球吸引力的力。它相當於身體質量，乘上重力加速度(在海平面為
    9.80665)，並以牛頓[N]為單位。)

    For example a man of 75 kg (it is its mass, and not its weight 
    contrary to the current expression), has a weight of: 
    75 * 9.80665 = 735,5 N on the sea level.
    
    @since 2018.07.23
    @author tsungjung411@gmail.com
    @see http://tw.bestconverter.org/unitconverter_Weight_Mass.php
    '''
    
    pass
# end-of-class
