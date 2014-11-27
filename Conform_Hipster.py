#Bayesian Project
#Lizzy's to do list:
#1. Create two suites
# 2. set up flat priors
# 3. writie likelihood function
from __future__ import print_function, division

import csv
import math
import numpy
import sys

import matplotlib
import matplotlib.pyplot as pyplot

import thinkbayes2
import thinkplot



class Hipster(thinkbayes2.Suite):
  """doc strings"""
  
  def __init__(self, microPopulation, N):
    
    self.microPopulation = microPopulation
    
    pmf = thinkbayes2.Pmf()
    for i in range(N):
      self.Set(i/(N-1),1)
    self.Normalize()
    
    thinkbayes2.Suite.__init__(self, pmf, label = label1)
  
  def Likelihood(self, data, hypo):
    """Computes likelihood of data under hypothesis.
    
    hypo: Hypo is an opinion, a number between 0 and 1
    data: Data is popular opinion, a tuple (mean,standard deviation)
    """
	opinion = hypo
    (mean,std) = data
    like = thinkbayes2.EvalNormalPdf(hypo,mean,std)
    return like
    
    
class Conformist(thinkbayes2.Suite):
  """doc strings"""
  
  def __init__(self, microPopulation, N):
    self.microPopulation = microPopulation
  
  	pmf = thinkbayes2.Pmf()
    for i in range(N):
      self.Set(i/(N-1),1)
    self.Normalize()
    
    thinkbayes2.Suite.__init__(self,pmf,label = label2)
  
  def Likelihood(self, data, hype):
    """Computes likelihood of data under hypothesis.
    
    hypo: Hypo is an opinion, a number between 0 and 1
    data: Data is popular opinion, a tuple (mean,standard deviation)
    """
	opinion = hypo
    (mean,std) = data
    comp_mean = 1 - mean # completementary mean
    like = thinkbayes2.EvalNormalPdf(hypo,comp_mean,std)
    return like
    
    
def main():
  N = 100 #Number of iterations
  hipsterMicroPopulation = 100
  confromistMicroPopulation = 500
  hip = Hipster(hipsterMicroPopulation, 1000)
  conf = Conformist(conformistMicroPopulation, 1000)
  for i in range(N):
    hipmean = hip.Mean()
    hipvar = hip.Var()
    confmean = conf.Mean()
    confvar = conf.Var()
    hipPop = hip.microPopulation
    confPop = conf.microPopulation
    popmean = (hipmean*hipPop + confmean*confPop)/(hipPop + confPop)
    popvar = (hipvar*hipPop + confvar*confPop)/(hipPop + confPop)
    popstd = math.sqrt(popvar)
    thinkplot.Pdf(hip,label = 'Hipsters')
    thinkplot.Pdf(conf,label = 'Conformists')
    thinkplot.show()
    hip.Update((popmean,popstd))
    conf.Update((popmean,popstd))
