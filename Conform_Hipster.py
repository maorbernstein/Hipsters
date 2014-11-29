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
import random

import matplotlib
import matplotlib.pyplot as plt

import thinkbayes2
import thinkplot



class Hipster(thinkbayes2.Suite):
    """ The Hipster type is a whose opinion distribution must match the opposite of the popular opinion. It is initialized at .6"""
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
    like = thinkbayes2.EvalNormalPdf(hypo,1 - mean,std) + .2*random.random()
    return like
    
class Stubborn1(thinkbayes2.Suite):
  """This is the first iteration of a stubborn population for testing purposes. They are absolutely stubborn and never change their opinion."""
  
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
    return 1

class Stubborn2_Repub(thinkbayes2.Suite):
  """The Stubborn2_Repub is a Stubborn person but can be convinced (they just have a cap on how much they can be convinced per time step), and Repub means they start out at .95"""
  
  def __init__(self, N, label=None):
    
    
    pmf = thinkbayes2.Pmf()
    mu_p = .95
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
    
    As you can see, they can only be shifted by .05 maximally at a time.
    """
    opinion = hypo
    (mean,std) = data
    #comp_mean = 1 - mean # completementary mean
    diff = mean - opinion
    if (diff > .05):
        like = thinkbayes2.EvalNormalPdf(opinion,opinion + .05,std)
    elif (diff < -.05):
        like = thinkbayes2.EvalNormalPdf(opinion,opinion - .05,std)
    else:
        like = thinkbayes2.EvalNormalPdf(opinion,mean,std)
        
    return like

class Stubborn2_Democ(thinkbayes2.Suite):
  """The Stubborn2_Democ is a Stubborn person but can be convinced (they just have a cap on how much they can be convinced per time step), and Democ means they start at .05"""
  
  def __init__(self, N, label=None):
    
    
    pmf = thinkbayes2.Pmf()
    mu_p = .05
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
    As you can see, they can only be shifted by .05 maximally at a time.
    """
    opinion = hypo
    (mean,std) = data
    #comp_mean = 1 - mean # completementary mean
    diff = mean - opinion
    if (diff > .05):
        like = thinkbayes2.EvalNormalPdf(opinion,opinion + .05,std)
    elif (diff < -.05):
        like = thinkbayes2.EvalNormalPdf(opinion,opinion - .05,std)
    else:
        like = thinkbayes2.EvalNormalPdf(opinion,mean,std)
        
    return like
     
class FlipFlopper(thinkbayes2.Suite):
  """A Flip Flopper flips a coin, and then decides whether to be a conformist or a hipster. """
  
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
    #comp_mean = 1 - mean # completementary mean
    x = random.random()
    if (x>.5):
        like = thinkbayes2.EvalNormalPdf(hypo,mean,std)
    else:
        like = thinkbayes2.EvalNormalPdf(hypo,1-mean,std)
    return like


class Conformist(thinkbayes2.Suite):
  """A conformist conforms to the population's opinion, in other words they're mean tends to the mean of the population"""
  
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
    """This main was to test 2 micro-populations to see whether stability could be reached"""
  N = 100 #Number of iterations
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

    hip.Update((popmean[i],5*popstd))
    conf.Update((popmean[i],5*popstd))
    
  plt.plot(range(N),hipmean)
  plt.plot(range(N),confmean)
  plt.plot(range(N),popmean)
  plt.show()

  

def main_onlyhipsters():
    """This main was written to see if we could validate our model with Touboul's model"""
  N = 80 #Number of iterations
  delay = 15
  hipfrac = 1
  hip = Hipster(1000)

  hipmean = []
  hipmean.append(hip.Mean())
  hipvar = hip.Var()
  hipstd = math.sqrt(hipvar)
  
  hipmean = delay*hipmean

    
  for i in range(delay,N):
    hipmean.append(hip.Mean())
    hipvar = hip.Var()
    hipstd = math.sqrt(hipvar)
    hip.Update((hipmean[i - delay],2.5*hipstd))

  plt.plot(range(N),hipmean)
  plt.show()
  
  
def main_4_types():
    """This main was written to test whether we could take this model and test something completely different with it (in our case political opinion)"""
  N = 100 #Number of iterations
  delay = 10
  hipfrac = .01
  conffrac = .01
  democfrac = .45
  repubfrac = .45
  flipflopfrac = 1 - hipfrac - conffrac - democfrac - repubfrac
  hip = Hipster(1000)
  conf = Conformist(1000)
  democ = Stubborn2_Democ(1000)
  repub = Stubborn2_Repub(1000)
  flipflop = FlipFlopper(1000)
  hipmean = []
  confmean = []
  democmean = []
  repubmean = []
  flipflopmean = []
  popmean = []
  
  for i in range(delay):
    hipmean.append(hip.Mean())
    hipvar = hip.Var()
    confmean.append(conf.Mean())
    confvar = conf.Var()
    democmean.append(democ.Mean())
    democvar = democ.Var()
    repubmean.append(repub.Mean())
    repubvar = repub.Var()
    flipflopmean.append(flipflop.Mean())
    flipflopvar = flipflop.Var()
    popmean.append(hipmean[i]*hipfrac + confmean[i]*conffrac + democmean[i]*democfrac + repubmean[i]*repubfrac + flipflopmean[i]*flipflopfrac)
    popvar = hipvar*hipfrac + confvar*conffrac + democvar*democfrac + repubvar*repubfrac + flipflopvar*flipflopfrac
    popstd = math.sqrt(popvar)
    
    data = (popmean[i],popstd)
    
    hip.Update(data)
    conf.Update(data)
    democ.Update(data)
    repub.Update(data)
    flipflop.Update(data)

    
  
  for i in range(delay,N):
    hipmean.append(hip.Mean())
    hipvar = hip.Var()
    confmean.append(conf.Mean())
    confvar = conf.Var()
    democmean.append(democ.Mean())
    democvar = democ.Var()
    repubmean.append(repub.Mean())
    repubvar = repub.Var()
    flipflopmean.append(flipflop.Mean())
    flipflopvar = flipflop.Var()
    popmean.append(hipmean[i]*hipfrac + confmean[i]*conffrac + democmean[i]*democfrac + repubmean[i]*repubfrac + flipflopmean[i]*flipflopfrac)
    popvar = hipvar*hipfrac + confvar*conffrac + democvar*democfrac + repubvar*repubfrac + flipflopvar*flipflopfrac
    popstd = math.sqrt(popvar)
    
    data = (popmean[i-delay],popstd)    
    
    hip.Update(data)
    conf.Update(data)
    democ.Update(data)
    repub.Update(data)
    flipflop.Update(data)

  
  plt.plot(range(N),hipmean)
  plt.plot(range(N),confmean)
  plt.plot(range(N),democmean)
  plt.plot(range(N),repubmean)
  plt.plot(range(N),flipflopmean)
  plt.show()
  plt.plot(range(N),popmean)
  plt.show()
  

  
  
  

if __name__ == "__main__":
    main_4_types()