# --------------------------------------------------------
# (c) Copyright 2014, 2020 by Jason DeLaat.
# Licensed under BSD 3-clause licence.
# --------------------------------------------------------
import unittest

import common_tests
from pymonad.either import Either, Left, Right
from pymonad.either import Error, Result


class EitherTests(unittest.TestCase):
    def test_repr(self):
        self.assertEqual(str(Right(9)), 'Right 9')
        self.assertEqual(str(Left(9)), 'Left 9')

    def test_insert(self):
        self.assertEqual(Either.insert(1), Right(1))

class ErrorTests(unittest.TestCase):
    def test_repr(self):
        self.assertEqual(str(Result(9)), 'Result: 9')
        self.assertEqual(str(Error(9)), 'Error: 9')

    def test_insert(self):
        self.assertEqual(Error.insert(1), Result(1))
        self.assertEqual(str(Error.insert(1)), 'Result: 1')

class EitherFunctor(common_tests.FunctorTests, unittest.TestCase):
    def setUp(self):
        self._class = Either

class EitherApplicative(common_tests.ApplicativeTests, unittest.TestCase):
    def setUp(self):
        self._class = Either

class EitherMonad(common_tests.MonadTests, unittest.TestCase):
    def setUp(self):
        self._class = Either

class EitherThen(common_tests.ThenTests, unittest.TestCase):
    def setUp(self):
        self._class = Either
