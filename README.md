# PINNpapers

Contributed by [IDRL lab](https://github.com/idrl-lab).

## Introduction

Physics-Informed Neural Network (PINN) has achieved great success in scientific computing since 2017. In this repo, we list some representative work on PINNs. Feel free to distribute or use it!

Corrections and suggestions are welcomed.

A [script](./ref_convert.py) for converting bibtex to the markdown used in this repo is also provided for your convenience.

## Software


1. **DeepXDE: A Deep Learning Library for Solving Differential Equations**, *Lu Lu, Xuhui Meng, Zhiping Mao, George Em Karniadakis*, SIAM Review, 2021. [[paper](https://epubs.siam.org/doi/pdf/10.1137/19M1274067)][[code](https://github.com/lululxvi/deepxde)]
2. **NVIDIA SimNet™: An AI-Accelerated Multi-Physics Simulation Framework**, *Oliver Hennigh, Susheela Narasimhan, Mohammad Amin Nabian, Akshay Subramaniam, Kaustubh Tangsali, Zhiwei Fang, Max Rietmann, Wonmin Byeon, Sanjay Choudhry*, **ICCS**, 2021. [[paper](https://link.springer.com/chapter/10.1007/978-3-030-77977-1_36)]
3. **SciANN: A Keras wrapper for scientific computations and physics-informed deep learning using artificial neural networks**, *Ehsan Haghighat, Ruben Juanes*, arXiv preprint arXiv:2005.08803, 2020. [[paper](https://www.sciencedirect.com/science/article/pii/S0045782520307374)][[code](https://github.com/sciann/sciann)]
4. **Elvet -- a neural network-based differential equation and variational problem solver**, *Jack Y. Araz, Juan Carlos Criado, Michael Spannowsky*, arXiv:2103.14575 [hep-lat, physics:hep-ph, physics:hep-th, stat], 2021. [[paper](https://arxiv.org/pdf/2103.14575)][[code](https://gitlab.com/elvet/elvet)]
5. **TensorDiffEq: Scalable Multi-GPU Forward and Inverse Solvers for Physics Informed Neural Networks**, *Levi D. McClenny, Mulugeta A. Haile, Ulisses M. Braga-Neto*, arXiv:2103.16034 [physics], 2021. [[paper](https://arxiv.org/pdf/2103.16034)][[code](https://github.com/tensordiffeq/TensorDiffEq)]
6. **PyDEns: a Python Framework for Solving Differential Equations with Neural Networks**, *Alex Koryagin, er, Roman Khudorozkov, Sergey Tsimfer*, arXiv:1909.11544 [cs, stat], 2019. [[paper]()][[code]()]
7. **NeuroDiffEq: A Python package for solving differential equations with neural networks**, *Feiyu Chen, David Sondak, Pavlos Protopapas, Marios Mattheakis, Shuheng Liu, Devansh Agarwal, Marco Di Giovanni*, Journal of Open Source Software, 2020. [[paper](https://joss.theoj.org/papers/10.21105/joss.01931)][[code](https://github.com/analysiscenter/pydens)]
8. **Universal Differential Equations for Scientific Machine Learning**, *Christopher Rackauckas, Yingbo Ma, Julius Martensen, Collin Warner, Kirill Zubov, Rohit Supekar, Dominic Skinner, Ali Ramadhan, Alan Edelman*, arXiv:2001.04385 [cs, math, q-bio, stat], 2020. [[paper](https://arxiv.org/pdf/2001.04385.pdf)][[code](https://github.com/ChrisRackauckas/universal_differential_equations)]
9. **NeuralPDE: Automating Physics-Informed Neural Networks (PINNs) with Error Approximations**, *Kirill Zubov, Zoe McCarthy, Yingbo Ma, Francesco Calisto, Valerio Pagliarino, Simone Azeglio, Luca Bottero, Emmanuel Luján, Valentin Sulzer, Ashutosh Bharambe, N Vinchhi, , Kaushik Balakrishnan, Devesh Upadhyay, Chris Rackauckas*, arXiv:2107.09443 [cs], 2021. [[paper](https://arxiv.org/pdf/2107.09443)][[code](https://github.com/SciML/NeuralPDE.jl)]
10. **IDRLnet: A Physics-Informed Neural Network Library**, *Wei Peng, Jun Zhang, Weien Zhou, Xiaoyu Zhao, Wen Yao, Xiaoqian Chen*, arXiv:2107.04320 [cs, math], 2021. [[paper](https://arxiv.org/pdf/2107.04320.pdf)][[code](https://github.com/idrl-lab/idrlnet)]

## Papers on PINN Models
1. **Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations**, *M. Raissi, P. Perdikaris, G. E. Karniadakis*, Journal of Computational Physics, 2019. [[paper](https://www.sciencedirect.com/science/article/pii/S0021999118307125)]
2. **The deep Ritz method: a deep learning-based numerical algorithm for solving variational problems**, *E Weinan, Bing Yu*, Communications in Mathematics and Statistics, 2018. [[paper](https://link.springer.com/article/10.1007/s40304-018-0127-z)]
3. **DGM: A deep learning algorithm for solving partial differential equations**, *Justin Sirignano, Konstantinos Spiliopoulos*, Journal of Computational Physics, 2018. [[paper](https://www.sciencedirect.com/science/article/pii/S0021999118305527)]
4. **SPINN: Sparse, Physics-based, and partially Interpretable Neural Networks for PDEs**, *Amuthan A. Ramabathiran, Ramach, Prabhu ran*, Journal of Computational Physics, 2021. [[paper](https://www.sciencedirect.com/science/article/pii/S0021999121004952)][[code](https://github.com/nn4pde/SPINN)]
5. **Deep neural network methods for solving forward and inverse problems of time fractional diffusion equations with conformable derivative**, *Yinlin Ye, Yajing Li, Hongtao Fan, Xinyi Liu, Hongbing Zhang*, arXiv:2108.07490 [cs, math], 2021. [[paper](http://arxiv.org/pdf/2108.07490.pdf)]

## Papers on Parallel PINN
1. **Parallel Physics-Informed Neural Networks via Domain Decomposition**, *Khemraj Shukla, Ameya D. Jagtap, George Em Karniadakis*, arXiv:2104.10013 [cs], 2021. [[paper](https://arxiv.org/pdf/2104.10013)]
2. **Finite Basis Physics-Informed Neural Networks (FBPINNs): a scalable domain decomposition approach for solving differential equations**, *Ben Moseley, Andrew Markham, Tarje Nissen-Meyer*, arXiv:2107.07871 [physics], 2021. [[paper](https://arxiv.org/pdf/2107.07871)]
3. **PPINN: Parareal physics-informed neural network for time-dependent PDEs**, *Xuhui Meng, Zhen Li, Dongkun Zhang, George Em Karniadakis*, Computer Methods in Applied Mechanics and Engineering, 2020. [[paper](https://arxiv.org/pdf/2104.10013)]
   
## Papers on PINN Accerleration
1. **Self-adaptive loss balanced Physics-informed neural networks for the incompressible Navier-Stokes equations**, *Zixue Xiang, Wei Peng, Xiaohu Zheng, Xiaoyu Zhao, Wen Yao*, arXiv:2104.06217 [physics], 2021. [[paper](https://arxiv.org/pdf/2104.06217)]
2. **A Dual-Dimer method for training physics-constrained neural networks with minimax architecture**, *Dehao Liu, Yan Wang*, Neural Networks, 2021. [[paper](https://www.sciencedirect.com/science/article/abs/pii/S0893608020304536)]
3. **Adversarial Multi-task Learning Enhanced Physics-informed Neural Networks for Solving Partial Differential Equations**, *Pongpisit Thanasutives, Masayuki Numao, Ken-ichi Fukui*, arXiv:2104.14320 [cs, math], 2021. [[paper](https://arxiv.org/pdf/2104.14320)]
4. **DPM: A Novel Training Method for Physics-Informed Neural Networks in Extrapolation**, *Jungeun Kim, Kookjin Lee, Dongeun Lee, Sheo Yon Jin, Noseong Park*, AAAI, 2021. [[paper](https://www.aaai.org/AAAI21Papers/AAAI-4849.KimJ.pdf)]

## Papers on Model Transfer & Meta-Learning

1. **A physics-aware learning architecture with input transfer networks for predictive modeling**, *Amir Behjat, Chen Zeng, Rahul Rai, Ion Matei, David Doermann, Souma Chowdhury*, Applied Soft Computing, 2020. [[paper](https://www.sciencedirect.com/science/article/abs/pii/S1568494620306037)]
2. **Transfer learning based multi-fidelity physics informed deep neural network**, *Souvik Chakraborty*, Journal of Computational Physics, 2021. [[paper](https://www.sciencedirect.com/science/article/pii/S0021999120307166)]
3. **Transfer learning enhanced physics informed neural network for phase-field modeling of fracture**, *Somdatta Goswami, Cosmin Anitescu, Souvik Chakraborty, Timon Rabczuk*, Theoretical and Applied Fracture Mechanics, 2020. [[paper](https://www.sciencedirect.com/science/article/abs/pii/S016784421930357X)]
4. **Meta-learning PINN loss functions**, *Apostolos F. Psaros, Kenji Kawaguchi, George Em Karniadakis*, arXiv:2107.05544 [cs], 2021. [[paper](https://arxiv.org/pdf/2107.05544.pdf)]

## Papers on Probabilistic PINNs and Uncertainty Quantification
1. **A physics-aware, probabilistic machine learning framework for coarse-graining high-dimensional systems in the Small Data regime**, *Constantin Grigo, Phaedon-Stelios Koutsourelakis*, Journal of Computational Physics, 2019. [[paper](https://www.sciencedirect.com/science/article/pii/S0021999119305261)]
2. **Adversarial uncertainty quantification in physics-informed neural networks**, *Yibo Yang, Paris Perdikaris*, Journal of Computational Physics, 2019. [[paper](https://www.sciencedirect.com/science/article/pii/S0021999119303584)]
3. **B-PINNs: Bayesian physics-informed neural networks for forward and inverse PDE problems with noisy data**, *Liu Yang, Xuhui Meng, George Em Karniadakis*, Journal of Computational Physics, 2021. [[paper](https://www.sciencedirect.com/science/article/pii/S0021999120306872)]
4. **PID-GAN: A GAN Framework based on a Physics-informed Discriminator for Uncertainty Quantification with Physics**, *Arka Daw, M. Maruf, Anuj Karpatne*, arXiv:2106.02993 [cs, stat], 2021. [[paper](https://arxiv.org/pdf/2106.02993)]
5. **Quantifying Uncertainty in Physics-Informed Variational Autoencoders for Anomaly Detection**, *Marcus J. Neuer*, ESTEP, 2020. [[paper](https://link.springer.com/chapter/10.1007/978-3-030-69367-1_3)]

## Papers on Applications
1. **Physics-informed neural networks for high-speed flows**, *Zhiping Mao, Ameya D. Jagtap, George Em Karniadakis*, Computer Methods in Applied Mechanics and Engineering, 2020. [[paper](https://www.sciencedirect.com/science/article/abs/pii/S0045782519306814)]
2. **Surrogate modeling for fluid flows based on physics-constrained deep learning without simulation data**, *Luning Sun, Han Gao, Shaowu Pan, Jian-Xun Wang*, Computer Methods in Applied Mechanics and Engineering, 2020. [[paper](https://www.sciencedirect.com/science/article/abs/pii/S004578251930622X)]
3. **Hidden fluid mechanics: Learning velocity and pressure fields from flow visualizations**, *Maziar Raissi, Alireza Yazdani, George Em Karniadakis*, Science, 2020. [[paper](https://science.sciencemag.org/content/367/6481/1026.full)]
4. **NSFnets (Navier-Stokes flow nets): Physics-informed neural networks for the incompressible Navier-Stokes equations**, *Xiaowei Jin, Shengze Cai, Hui Li, George Em Karniadakis*, Journal of Computational Physics, 2021. [[paper](https://www.sciencedirect.com/science/article/pii/S0021999120307257)]
5. **A High-Efficient Hybrid Physics-Informed Neural Networks Based on Convolutional Neural Network**, *Zhiwei Fang*, IEEE Transactions on Neural Networks and Learning Systems, 2021. [[paper](https://ieeexplore.ieee.org/abstract/document/9403414)]
6. **A Study on a Feedforward Neural Network to Solve Partial Differential Equations in Hyperbolic-Transport Problems**, *Eduardo Abreu, Joao B. Florindo*, ICCS, 2021. [[paper](https://link.springer.com/chapter/10.1007/978-3-030-77964-1_31)]
7. **A Physics Informed Neural Network Approach to Solution and Identification of Biharmonic Equations of Elasticity**, *Mohammad Vahab, Ehsan Haghighat, Maryam Khaleghi, Nasser Khalili*, arXiv:2108.07243 [cs], 2021. [[paper](http://arxiv.org/pdf/2108.07243.pdf)]
8. **Prediction of porous media fluid flow using physics informed neural networks**, *Muhammad M. Almajid, Moataz O. Abu-Alsaud*, Journal of Petroleum Science and Engineering, 2021. [[paper](https://linkinghub.elsevier.com/retrieve/pii/S0920410521008597)]
9. **Investigating a New Approach to Quasinormal Modes: Physics-Informed Neural Networks**, *Anele M. Ncube, Gerhard E. Harmsen, Alan S. Cornell*, arXiv:2108.05867 [gr-qc], 2021. [[paper](http://arxiv.org/pdf/2108.05867.pdf)]
10. **Towards neural Earth system modelling by integrating artificial intelligence in Earth system science**, *Christopher Irrgang, Niklas Boers, Maike Sonnewald, Elizabeth A. Barnes, Christopher Kadow, Joanna Staneva, Jan Saynisch-Wagner*, Nature Machine Intelligence, 2021. [[paper](https://www.nature.com/articles/s42256-021-00374-3)]

## Papers on PINN Analysis
1. **Estimates on the generalization error of physics-informed neural networks for approximating a class of inverse problems for PDEs**, *Siddhartha Mishra, Roberto Molinaro*, IMA Journal of Numerical Analysis, 2021. [[paper](https://academic.oup.com/imajna/advance-article-abstract/doi/10.1093/imanum/drab032/6297946)]
2. **Error analysis for physics informed neural networks (PINNs) approximating Kolmogorov PDEs**, *Tim De Ryck, Siddhartha Mishra*, arXiv:2106.14473 [cs, math], 2021. [[paper](https://arxiv.org/pdf/2106.14473.pdf)]
3. **Error Analysis of Deep Ritz Methods for Elliptic Equations**, *Yuling Jiao, Yanming Lai, Yisu Luo, Yang Wang, Yunfei Yang*, arXiv:2107.14478 [cs, math], 2021. [[paper](https://arxiv.org/pdf/2107.14478.pdf)]