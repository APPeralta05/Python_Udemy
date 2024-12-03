from collections import namedtuple
from collections import Counter
from collections import defaultdict 


serie = Counter([1,1,2,3,3,3,3,3,1,1,2,3,6,4,5,4,])
print(serie.most_common(1))


Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
alejo = Persona('Alejo', 1.80, 79)

print(alejo.altura)


mi_dic = defaultdict(lambda: 'nada')

mi_dic['uno'] = 'verde'
print(['dos'])