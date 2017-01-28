from distutils.core import setup, Extension

module1 = Extension( 
	'my_plus', # module name in interpreter
	sources = ['plus.c'] 
)

setup( 
	name = 'my_plus',
	version = '1.1',
	description = 'Simple module',
	ext_modules= [module1]
)