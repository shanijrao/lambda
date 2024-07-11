#(1)
Slicing=lambda x:x[4:]
print(Slicing("amritsar"))

#(2)
var = lambda x:x.rstrip()
print(var("  hello san "))

#(3)
shan = lambda a:a.lstrip()
print(shan("  hello san "))

#(4)
shan = lambda a:a.strip('#')
print(shan("###batala###"))

#(5)
shan = lambda a:a.strip('cmow.')
print(shan("www.example.com"))

#(6)
shan = lambda a:a.lstrip('Arthur: ')
print(shan("Arthur: three!"))

#(7)
shan = lambda a:a.removeprefix('Arthur: ')
print(shan("Arthur: three!"))

shan = lambda a:a.removesuffix('Python')
print(shan("HelloPython"))

#(8)
shan = lambda a:a.replace('\n','')
print(shan(' \n \t hello\n'))

#(9)
shan = lambda a:a.upper()
print(shan("hey how are you!"))

#(10)
shan = lambda a:a.lower()
print(shan("hey how are you!"))

#(11)
shan = lambda a:a.capitalize()
print(shan("hey how are you!"))

#(12)
shan = lambda a:a.islower()
print(shan("HEY HOW ARE YOU!"))

shan = lambda a:a.islower()
print(shan("hey how are you!"))

#(13)
shan = lambda a:a.isupper()
print(shan("HEY HOW ARE YOU!"))

shan = lambda a:a.isupper()
print(shan("hey how are you!"))

#(14)
shan = lambda a:a.count('o')
print(shan("i love batala"))

#(15)
shan = lambda a:a.find('B')
print(shan("BATALA"))

shan = lambda a:a [1:]
print(shan("BATALA"))

#(16)
shan = lambda a:a.rfind('L')
print(shan("BATALA"))

#(17)
shan = lambda a:a.startswith('BAT')
print(shan("BATALA"))

#(18)
shan = lambda a:a.endswith('ALA')
print(shan("BATALA"))

#(19)
shan = lambda s:s.partition('is')
print(shan("chocolate is awesome"))

shan = lambda s:s.partition('was')
print(shan("chocolate is awesome"))

#(20) center
rao = lambda d:d.center(30, '-')
print(rao("Food is delicious!"))

#(21) ljust
rao = lambda d:d.ljust(30, '-')
print(rao("Food is delicious!"))

#(22) rjust
rao = lambda d:d.rjust(30, '-')
print(rao("Food is delicious!"))

#(23) swapcase()
marvel = lambda h:h.swapcase()
print(marvel("HELLO batala"))

#(24)) zfill()
marvel = lambda h:h.zfill(8)
print(marvel("600"))

marvel = lambda h:h.zfill(6)
print(marvel("-900"))

#(25) f-Strings 
let = 'place'
city = 'Amritsar'
marvel = lambda h:h.fstring()
print(f'{city} is the famous {let} in India!')

#(26)
marvel = lambda s:s.split()
print(marvel("batala city is in punjab"))

#(27)rsplit()
marvel = lambda h:h.rsplit()
print(marvel("batala city is in punjab"))

#(28) 
shan = lambda s:s.isalpha()
print(shan("best"))

#(29)
shan = lambda s:s.isnumeric()
print(shan("8084"))

#(30)
shan = lambda s:s.isalnum()
print(shan("best7415"))