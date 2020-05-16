# --------------------------------------------------------
# (c) Copyright 2014, 2020 by Jason DeLaat.
# Licensed under BSD 3-clause licence.
# --------------------------------------------------------
""" Implements the Monad base class.

The Monad base class is an abstract class which defines the operations
available on all monad instances. To create a new Monad instance,
users should create a class which inherits from Monad and provides
implementations for the methods fmap, amap, bind, and class method
unit. See the documentation for those methods for more information on
how to implement them properly.
"""

class Monad:
    """
    Represents a "context" in which calculations can be executed.

    You won't create 'Monad' instances directly. Instead, sub-classes implement
    specific contexts. Monads allow you to bind together a series of calculations
    while maintaining the context of that specific monad.

    """
    def __init__(self, value):
        """ Wraps 'value' in the Monad's context. """
        self.value = value
        self.is_monad_value = True

    def fmap(self, function):
        """ Applies 'function' to the contents of the functor and returns a new functor value. """
        raise NotImplementedError("'fmap' not defined.")

    def __rmul__(self, a_function):
        """ The 'fmap' operator.
        The following are equivalent:

            aFunctor.fmap(a_function)
            a_function * aFunctor

        """

        return self.fmap(a_function)

    @classmethod
    def unit(cls, value):
        """ Returns an instance of the Functor with 'value' in a minimum context.  """
        raise NotImplementedError

    def amap(self, functor_value):
        """ Applies the function stored in the functor to the value inside 'functor_value'
        returning a new functor value.

        """
        raise NotImplementedError

    def __and__(self, functor_value):
        """ The 'amap' operator. """
        return self.amap(functor_value)

    def get_value(self):
        """ Returns the value held by the Container. """
        return self.value

    def __eq__(self, other):
        return self.value == other.value

    def bind(self, function):
        """ Applies 'function' to the result of a previous monadic calculation. """
        raise NotImplementedError

    def then(self, function):
        """ Combines the functionality of bind and fmap.

        Instead of worrying about whether to use bind or fmap,
        users can just use the then method to chain function
        calls together. The then method uses attempts to use
        bind first and if that doesn't work, uses fmap
        instead.

        Args:
        function: A python function or lambda expression
        which returns either a build-in type (int, string,
        etc.) or an appropriate monad type (Maybe, Either,
        etc.)

        Returns:
        A monad value of the same type as 'self'
        """

        result = self.bind(function)
        try:
            result.is_monad_value # pylint: disable=pointless-statement
            return result
        except AttributeError:
            return self.fmap(function)

    def __rshift__(self, function):
        """ The 'bind' operator. The following are equivalent:
            monadValue >> someFunction
            monadValue.bind(someFunction)

        """
        if callable(function): # pylint: disable=no-else-return
            result = self.bind(function)
            if not isinstance(result, Monad):
                raise TypeError("Operator '>>' must return a Monad instance.")
            return result
        else:
            if not isinstance(function, Monad):
                raise TypeError("Operator '>>' must return a Monad instance.")
            return self.bind(lambda _: function)

def unit(a_class, value):
    """ Calls the 'unit' method of 'a_class' with 'value'.  """
    return a_class.unit(value)
