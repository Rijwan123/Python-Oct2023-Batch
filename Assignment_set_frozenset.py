Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> #What is frozenset?
>>> #A frozenset in Python is an immutable set, which means that once you create a frozenset, you cannot change its elements (add, remove, or modify them).
>>> a= frozenset([1, 2, 3, 4, 5])
>>> a
frozenset({1, 2, 3, 4, 5})
>>> #-------------------------------------------------------
>>> #What is difference between set and frozenset?
>>> #Set:
>>>
>>> Sets are mutable, meaning you can add, remove, or update elements in a set after it has been created.
  File "<stdin>", line 1
    Sets are mutable, meaning you can add, remove, or update elements in a set after it has been created.
         ^^^
SyntaxError: invalid syntax
>>> Sets are defined using curly braces or the set() constructor.
  File "<stdin>", line 1
    Sets are defined using curly braces or the set() constructor.
         ^^^
SyntaxError: invalid syntax
>>> Sets are not hashable and cannot be used as elements in other sets or as keys in dictionaries.
  File "<stdin>", line 1
    Sets are not hashable and cannot be used as elements in other sets or as keys in dictionaries.
         ^^^
SyntaxError: invalid syntax
>>> #------------------------------------------------------------------------------
>>>  #What is difference between set and frozenset?
>>> #Sets are mutable, meaning you can add, remove, or update elements in a set after it has been created.
>>> #Sets are defined using curly braces or the set() constructor.
>>> #Sets are not hashable and cannot be used as elements in other sets or as keys in dictionarie
>>> set = {1, 2, 3}
>>> set
{1, 2, 3}
>>> set.add(4)
>>> set
{1, 2, 3, 4}
>>>
>>> #Frozenset:
>>> #Frozensets are immutable, meaning once a frozenset is created, you cannot add, remove, or modify its elements.
>>> #Frozensets are defined using the frozenset() constructor.
>>> #Frozensets are hashable and can be used as elements in other sets or as keys in dictionaries.
>>>
>>> frozenset = frozenset([1, 2, 3])
>>> frosenset
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'frosenset' is not defined. Did you mean: 'frozenset'?
>>> frozenset
frozenset({1, 2, 3})
>>> frozenset.add(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'frozenset' object has no attribute 'add'
>>> #============================================================================================================