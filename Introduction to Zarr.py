#!/usr/bin/env python
# coding: utf-8

# #### Introduction to Zarr

# Learning Objectives: By the end of this lesson, students should be able to determine Zarr's goal.
# (ii) Have the ability to install and run zarr on their workstation.

# ##### What is Zarr?

# Zarr is a Python package for creating compressed, chunked N-dimensional arrays for parallel computation. It is a file format that is used to store chunked, compressed N-dimensional arrays. The initial launch raster API or the newer multidimensional API can be utilized to read and write to this format.

# ##### Installing Zarr

# ###### To install Zarr on your working environment;

# If you are not using Anaconda, put the text below into your terminal.
# 
# 
# ---> pip install jupyter
# 
# 
# After a successful installation, enter the line below to access your jupyter notebook from your IDE.
# 
# 
# ---> jupyter-lab 
# 
# 
# You will be transferred to your browser, where you may access jupyter notebook
# 
# ###### If you use Anaconda as your workstation(IDE) or you have jupyter istalled already, put the text below into your terminal.
# ---> pip install zarr 
# ###### Alternative installation via conda
# ---> conda install -c conda-forge zarr
# ###### To verify that Zarr has been fully installed, run the test suite:
# ---> pip install pytest
# 
# 
# ---> python -m pytest -v --pyargs zarr
# 

# In[ ]:




