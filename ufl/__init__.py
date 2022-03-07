# -*- coding: utf-8 -*-
# flake8: noqa
"""The Unified Form Language is an embedded domain specific language
for definition of variational forms intended for finite element
discretization. More precisely, it defines a fixed interface for choosing
finite element spaces and defining expressions for weak forms in a
notation close to the mathematical one.

This Python module contains the language as well as algorithms to work
with it.

* To import the language, type::

    from ufl import *

* To import the underlying classes an UFL expression tree is built
  from, type
  ::

    from ufl.classes import *

* Various algorithms for working with UFL expression trees can be
  accessed by
  ::

    from ufl.algorithms import *

Classes and algorithms are considered implementation details and
should not be used in form definitions.

For more details on the language, see

  http://www.fenicsproject.org

and

  http://arxiv.org/abs/1211.4047

The development version can be found in the repository at

  https://www.bitbucket.org/fenics-project/ufl

A very brief overview of the language contents follows:

* Cells::

    - AbstractCell
    - Cell
    - TensorProductCell
    - vertex
    - interval
    - triangle
    - tetrahedron
    - quadrilateral
    - hexahedron
    - prism
    - pyramid

* Domains::

    - AbstractDomain
    - Mesh
    - MeshView
    - TensorProductMesh

* Sobolev spaces::

    - L2
    - H1
    - H2
    - HDiv
    - HCurl

* Elements::

    - FiniteElement
    - MixedElement
    - VectorElement
    - TensorElement
    - EnrichedElement
    - NodalEnrichedElement
    - RestrictedElement
    - TensorProductElement
    - HDivElement
    - HCurlElement
    - BrokenElement
    - FacetElement
    - InteriorElement

* Function spaces::

    - FunctionSpace
    - MixedFunctionSpace

* Arguments::

    - Argument
    - TestFunction
    - TrialFunction
    - Arguments
    - TestFunctions
    - TrialFunctions

* Coefficients::

    - Coefficient
    - Constant
    - VectorConstant
    - TensorConstant

* Splitting form arguments in mixed spaces::

    - split

* Literal constants::

    - Identity
    - PermutationSymbol

* Geometric quantities::

    - SpatialCoordinate
    - FacetNormal
    - CellNormal
    - CellVolume
    - CellDiameter
    - Circumradius
    - MinCellEdgeLength
    - MaxCellEdgeLength
    - FacetArea
    - MinFacetEdgeLength
    - MaxFacetEdgeLength
    - Jacobian
    - JacobianDeterminant
    - JacobianInverse

* Indices::

    - Index
    - indices
    - i, j, k, l
    - p, q, r, s

* Scalar to tensor expression conversion::

    - as_tensor
    - as_vector
    - as_matrix

* Unit vectors and matrices::

    - unit_vector
    - unit_vectors
    - unit_matrix
    - unit_matrices

* Tensor algebra operators::

    - outer, inner, dot, cross, perp
    - det, inv, cofac
    - transpose, tr, diag, diag_vector
    - dev, skew, sym

* Elementwise tensor operators::

    - elem_mult
    - elem_div
    - elem_pow
    - elem_op

* Differential operators::

    - variable
    - diff,
    - grad, nabla_grad
    - div, nabla_div
    - curl, rot
    - Dx, Dn

* Nonlinear functions::

    - max_value, min_value
    - abs, sign
    - sqrt
    - exp, ln, erf
    - cos, sin, tan
    - acos, asin, atan, atan_2
    - cosh, sinh, tanh
    - bessel_J, bessel_Y, bessel_I, bessel_K

* Complex operations::

    - conj, real, imag
    conjugate is an alias for conj

* Discontinuous Galerkin operators::

    - v('+'), v('-')
    - jump
    - avg
    - cell_avg, facet_avg

* Conditional operators::

    - eq, ne, le, ge, lt, gt
    - <, >, <=, >=
    - And, Or, Not
    - conditional

* Integral measures::

    - dx, ds, dS, dP
    - dc, dC, dO, dI, dX
    - ds_b, ds_t, ds_tb, ds_v, dS_h, dS_v

* Form transformations::

    - rhs, lhs
    - system
    - functional
    - replace, replace_integral_domains
    - adjoint
    - action
    - energy_norm,
    - sensitivity_rhs
    - derivative
"""

# Copyright (C) 2008-2016 Martin Sandve Alnæs and Anders Logg
#
# This file is part of UFL (https://www.fenicsproject.org)
#
# SPDX-License-Identifier:    LGPL-3.0-or-later
#
# Modified by Kristian B. Oelgaard, 2009, 2011
# Modified by Anders Logg, 2009.
# Modified by Johannes Ring, 2014.
# Modified by Andrew T. T. McRae, 2014
# Modified by Lawrence Mitchell, 2014
# Modified by Massimiliano Leoni, 2016
# Modified by Cecile Daversin-Catty, 2018

import pkg_resources

__version__ = pkg_resources.get_distribution("fenics-ufl").version

# README
# Imports here should be what the user sees when doing "from ufl import *",
# which means we should _not_ import f.ex. "Grad", but "grad".
# This way we expose the language, the operation "grad", but less
# of the implementation, the particular class "Grad".
##########

# Useful constants
from math import e, pi

# Special functions for expression base classes
# (ensure this is imported, since it attaches operators to Expr)
import ufl.exproperators as __exproperators
# Special functions for Measure class
# (ensure this is imported, since it attaches operators to Measure)
import ufl.measureoperators as __measureoperators
# Arguments
from ufl.argument import (Argument, Arguments, TestFunction, TestFunctions,
                          TrialFunction, TrialFunctions)
from ufl.cell import AbstractCell, Cell, TensorProductCell, as_cell
# Coefficients
from ufl.coefficient import Coefficient, Coefficients
from ufl.constant import Constant, TensorConstant, VectorConstant
# Literal constants
from ufl.constantvalue import Identity, PermutationSymbol, as_ufl, zero
# Indexing of tensor expressions
from ufl.core.multiindex import Index, indices
from ufl.domain import (AbstractDomain, Mesh, MeshView, TensorProductMesh,
                        as_domain)
# Finite elements classes
from ufl.finiteelement import (BrokenElement, EnrichedElement, FacetElement,
                               FiniteElement, FiniteElementBase, HCurlElement,
                               HDivElement, InteriorElement, MixedElement,
                               NodalEnrichedElement, RestrictedElement,
                               TensorElement, TensorProductElement,
                               VectorElement, WithMapping)
# Hook to extend predefined element families
from ufl.finiteelement.elementlist import register_element  # , ufl_elements
from ufl.finiteelement.elementlist import show_elements
# Form class
from ufl.form import Form, replace_integral_domains
# Representations of transformed forms
from ufl.formoperators import (action, adjoint,  # , dirichlet_functional
                               derivative, energy_norm, extract_blocks,
                               functional, lhs, replace, rhs, sensitivity_rhs,
                               system)
# Function spaces
from ufl.functionspace import FunctionSpace, MixedFunctionSpace
from ufl.geometry import (CellDiameter, CellNormal, CellVolume, Circumradius,
                          FacetArea, FacetNormal, Jacobian,
                          JacobianDeterminant, JacobianInverse,
                          MaxCellEdgeLength, MaxFacetEdgeLength,
                          MinCellEdgeLength, MinFacetEdgeLength,
                          SpatialCoordinate)
# Integral classes
from ufl.integral import Integral
# Output control
from ufl.log import (CRITICAL, DEBUG, ERROR, INFO, WARNING, UFLException,
                     add_logfile, get_handler, get_logger, set_handler,
                     set_level)
# Measure classes
from ufl.measure import (Measure, custom_integral_types, integral_types,
                         register_integral_type)
# Predefined convenience objects
from ufl.objects import (dc, dC, dI, dO, dP, ds, dS, ds_b, dS_h, ds_t, ds_tb,
                         ds_v, dS_v, dx, dX, facet, hexahedron, i, interval, j,
                         k, l, p, prism, pyramid, q, quadrilateral, r, s,
                         tetrahedron, triangle, vertex)
# Operators
from ufl.operators import (And, Dn, Dx, Max, Min, Not, Or, acos, asin, atan,
                           atan_2, avg, bessel_I, bessel_J, bessel_K, bessel_Y,
                           cell_avg, cofac, conditional, conj, cos, cosh,
                           cross, curl, det, dev, diag, diag_vector, diff, div,
                           dot, elem_div, elem_mult, elem_op, elem_pow, eq,
                           erf, exp, exterior_derivative, facet_avg, ge, grad,
                           gt, imag, inner, inv, jump, le, ln, lt, max_value,
                           min_value, nabla_div, nabla_grad, ne, outer, perp,
                           rank, real, rot, shape, sign, sin, sinh, skew, sqrt,
                           sym, tan, tanh, tr, transpose, variable)
# Sobolev spaces
from ufl.sobolevspace import H1, H2, L2, HCurl, HDiv
# Split function
from ufl.split_functions import split
# Containers for expressions with value rank > 0
from ufl.tensors import (as_matrix, as_tensor, as_vector, relabel,
                         unit_matrices, unit_matrix, unit_vector, unit_vectors)
# Utility functions (product is the counterpart of the built-in
# python function sum, can be useful for users as well?)
from ufl.utils.sequences import product

# Types for geometric quantities






















# Define ufl.* namespace
__all__ = [
    'product',
    'get_handler', 'get_logger', 'set_handler', 'set_level', 'add_logfile',
    'UFLException', 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL',
    'as_cell', 'AbstractCell', 'Cell', 'TensorProductCell',
    'as_domain', 'AbstractDomain', 'Mesh', 'MeshView', 'TensorProductMesh',
    'L2', 'H1', 'H2', 'HCurl', 'HDiv',
    'SpatialCoordinate',
    'CellVolume', 'CellDiameter', 'Circumradius',
    'MinCellEdgeLength', 'MaxCellEdgeLength',
    'FacetArea', 'MinFacetEdgeLength', 'MaxFacetEdgeLength',
    'FacetNormal', 'CellNormal',
    'Jacobian', 'JacobianDeterminant', 'JacobianInverse',
    'FiniteElementBase', 'FiniteElement',
    'MixedElement', 'VectorElement', 'TensorElement', 'EnrichedElement',
    'NodalEnrichedElement', 'RestrictedElement', 'TensorProductElement',
    'HDivElement', 'HCurlElement',
    'BrokenElement', 'FacetElement', 'InteriorElement', "WithMapping",
    'register_element', 'show_elements',
    'FunctionSpace', 'MixedFunctionSpace',
    'Argument', 'TestFunction', 'TrialFunction',
    'Arguments', 'TestFunctions', 'TrialFunctions',
    'Coefficient', 'Coefficients',
    'Constant', 'VectorConstant', 'TensorConstant',
    'split',
    'PermutationSymbol', 'Identity', 'zero', 'as_ufl',
    'Index', 'indices',
    'as_tensor', 'as_vector', 'as_matrix', 'relabel',
    'unit_vector', 'unit_vectors', 'unit_matrix', 'unit_matrices',
    'rank', 'shape', 'conj', 'real', 'imag',
    'outer', 'inner', 'dot', 'cross', 'perp',
    'det', 'inv', 'cofac',
    'transpose', 'tr', 'diag', 'diag_vector', 'dev', 'skew', 'sym',
    'sqrt', 'exp', 'ln', 'erf',
    'cos', 'sin', 'tan',
    'acos', 'asin', 'atan', 'atan_2',
    'cosh', 'sinh', 'tanh',
    'bessel_J', 'bessel_Y', 'bessel_I', 'bessel_K',
    'eq', 'ne', 'le', 'ge', 'lt', 'gt', 'And', 'Or', 'Not',
    'conditional', 'sign', 'max_value', 'min_value', 'Max', 'Min',
    'variable', 'diff',
    'Dx', 'grad', 'div', 'curl', 'rot', 'nabla_grad', 'nabla_div', 'Dn', 'exterior_derivative',
    'jump', 'avg', 'cell_avg', 'facet_avg',
    'elem_mult', 'elem_div', 'elem_pow', 'elem_op',
    'Form',
    'Integral', 'Measure', 'register_integral_type', 'integral_types', 'custom_integral_types',
    'replace', 'replace_integral_domains', 'derivative', 'action', 'energy_norm', 'rhs', 'lhs', 'extract_blocks',
    'system', 'functional', 'adjoint', 'sensitivity_rhs',
    'dx', 'ds', 'dS', 'dP',
    'dc', 'dC', 'dO', 'dI', 'dX',
    'ds_b', 'ds_t', 'ds_tb', 'ds_v', 'dS_h', 'dS_v',
    'vertex', 'interval', 'triangle', 'tetrahedron',
    'prism', 'pyramid',
    'quadrilateral', 'hexahedron', 'facet',
    'i', 'j', 'k', 'l', 'p', 'q', 'r', 's',
    'e', 'pi',
]
