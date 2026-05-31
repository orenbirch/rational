"""
The module in this file defines a class for rational numbers. It is intended to be used as a demonstration of packaging python modules.

Author: Oren Birch
Email: orenbirch@gmail.com
Date: 2026-05-31
Version: 1.0beta
"""
from math import gcd

class Rational:
    """A class representing a rational number."""
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero")

        # Keep a canonical representation so equality, hashing, and display are consistent.
        common = gcd(numerator, denominator)
        numerator //= common
        denominator //= common
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        """Return a string representation of the rational number."""
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        """Add two rational numbers."""
        if isinstance(other, Rational):
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Rational(new_numerator, new_denominator)
        else:
            return NotImplemented
        
    def __sub__(self, other):
        """Subtract two rational numbers."""
        if isinstance(other, Rational):
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Rational(new_numerator, new_denominator)
        else:
            return NotImplemented
        
    def __mul__(self, other):
        """Multiply two rational numbers."""
        if isinstance(other, Rational):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Rational(new_numerator, new_denominator)
        else:
            return NotImplemented
        
    def __truediv__(self, other):
        """Divide two rational numbers."""
        if isinstance(other, Rational):
            if other.numerator == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            return Rational(new_numerator, new_denominator)
        else:
            return NotImplemented
        
    def __pow__(self, exponent):
        """Raise the rational number to a power."""
        if isinstance(exponent, int):
            if exponent < 0 and self.numerator == 0:
                raise ZeroDivisionError("0 cannot be raised to a negative power")
            new_numerator = self.numerator ** exponent
            new_denominator = self.denominator ** exponent
            return Rational(new_numerator, new_denominator)
        else:
            raise TypeError("Unsupported type for exponentiation")
        
    def __eq__(self, other):
        """Check if two rational numbers are equal."""
        if isinstance(other, Rational):
            return self.numerator * other.denominator == self.denominator * other.numerator
        else:
            return NotImplemented
        
    def __lt__(self, other):
        """Check if this rational number is less than another."""
        if isinstance(other, Rational):
            return self.numerator * other.denominator < self.denominator * other.numerator
        else:
            return NotImplemented
        
    def __le__(self, other):
        """Check if this rational number is less than or equal to another."""
        if isinstance(other, Rational):
            return self.numerator * other.denominator <= self.denominator * other.numerator
        else:
            return NotImplemented
        
    def __gt__(self, other):
        """Check if this rational number is greater than another."""
        if isinstance(other, Rational):
            return self.numerator * other.denominator > self.denominator * other.numerator
        else:
            return NotImplemented
        
    def __ge__(self, other):
        """Check if this rational number is greater than or equal to another."""
        if isinstance(other, Rational):
            return self.numerator * other.denominator >= self.denominator * other.numerator
        else:
            return NotImplemented
        
    def __neg__(self):
        """Return the negation of the rational number."""
        return Rational(-self.numerator, self.denominator)
    
    def __int__(self):
        """Return the integer part of the rational number."""
        return int(self.numerator / self.denominator)
    
    def __float__(self):
        """Return the floating-point representation of the rational number."""
        return self.numerator / self.denominator
    
    def __abs__(self):
        """Return the absolute value of the rational number."""
        return Rational(abs(self.numerator), self.denominator)
    
    def __hash__(self):
        """Return a hash value for the rational number."""
        return hash((self.numerator, self.denominator))
    
    def __repr__(self):
        """Return a string representation of the rational number for debugging."""
        return f"Rational({self.numerator}, {self.denominator})"
    
    def __copy__(self):
        """Return a copy of the rational number."""
        return Rational(self.numerator, self.denominator)
    
    def __deepcopy__(self, memo):
        """Return a deep copy of the rational number."""
        return Rational(self.numerator, self.denominator)
        
    def __reduce__(self):
        """Return pickling instructions for this object."""
        return (self.__class__, (self.numerator, self.denominator))
    

    def simplify(self):
        """Return a simplified version of the rational number."""
        common = gcd(self.numerator, self.denominator)
        return Rational(self.numerator // common, self.denominator // common)
