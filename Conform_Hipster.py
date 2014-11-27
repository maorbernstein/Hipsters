#Bayesian Project
#Lizzy's to do list:
#1. Create two suites
# 2. set up flat priors
# 3. writie likelihood function
from __future__ import print_function, division

import csv
import math
import numpy as np
import sys

import matplotlib
import matplotlib.pyplot as plt

import thinkbayes2
import thinkplot



class Hipster(thinkbayes2.Suite):
  """doc strings"""
  
  def __init__(self, N, label=None):
    
    
    pmf = thinkbayes2.Pmf()
    mu_p = .6
    std_p = .1
    for i in range(N):
      o = i/(N-1.0)
      pmf.Set(o,thinkbayes2.EvalNormalPdf(o,mu_p,std_p) )
      
    pmf.Normalize()
    
    thinkbayes2.Suite.__init__(self, pmf, label = label)
  
  def Likelihood(self, data, hypo):
    """Computes likelihood of data under hypothesis.
    
    hypo: Hypo is an opinion, a number between 0 and 1
    data: Data is popular opinion, a tuple (mean,standard deviation)
    """
    opinion = hypo
    (mean,std) = data
    like = thinkbayes2.EvalNormalPdf(hypo,1 - mean,std)
    return like
    
    
class Conformist(thinkbayes2.Suite):
  """doc strings"""
  
  def __init__(self, N, label=None):
  
    pmf = thinkbayes2.Pmf()
    mu_p = .6
    std_p = .1
    for i in range(N):
      o = i/(N-1.0)
      pmf.Set(o, thinkbayes2.EvalNormalPdf(o,mu_p,std_p) )
      
    pmf.Normalize()
    
    thinkbayes2.Suite.__init__(self,pmf,label = label)
  
  def Likelihood(self, data, hypo):
    """Computes likelihood of data under hypothesis.
    
    hypo: Hypo is an opinion, a number between 0 and 1
    data: Data is popular opinion, a tuple (mean,standard deviation)
    """
    opinion = hypo
    (mean,std) = data
    #comp_mean = 1 - mean # completementary mean
    like = thinkbayes2.EvalNormalPdf(hypo,mean,std)
    return like
    
    
def main():
  N = 18 #Number of iterations
  hipfrac = 1
  conffrac = 1 - hipfrac
  hip = Hipster(1000)
  conf = Conformist(1000)
  hipmean = []
  confmean = []
  popmean = []
  
  for i in range(N):
    hipmean.append(hip.Mean())
    hipvar = hip.Var()
    confmean.append(conf.Mean())
    confvar = conf.Var()
    popmean.append(hipmean[i]*hipfrac + confmean[i]*conffrac)
    popvar = hipvar*hipfrac + confvar*conffrac
    popstd = math.sqrt(popvar)

    hip.Update((popmean[i],popstd))
    conf.Update((popmean[i],popstd))
    
  plt.plot(range(N),hipmean)
  plt.plot(range(N),confmean)
  plt.plot(range(N),popmean)
  plt.show()

  

def main_onlyhipsters():
  N = 18 #Number of iterations
  hipfrac = 1
  hip = Hipster(1000)
  hipmean = []

  hipmean.append(hip.Mean())
  hipvar = hip.Var()
  hipstd = math.sqrt(hipvar)
  hip.Update((hipmean[0],hipstd))
    
  for i in range(1,N):
    hipmean.append(hip.Mean())
    hipvar = hip.Var()
    hipstd = math.sqrt(hipvar)
    hip.Update((hipmean[i-1],hipstd))

  plt.plot(range(N),hipmean)
  plt.show()
  

if __name__ == "__main__":
    main_onlyhipsters()