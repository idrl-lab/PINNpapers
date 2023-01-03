# PINNpapers

Contributed by [IDRL lab](https://github.com/idrl-lab).

- [PINNpapers](#pinnpapers)
  - [Introduction](#introduction)
  - [Software](#software)
  - [Papers on PINN Models](#papers-on-pinn-models)
  - [Papers on Parallel PINN](#papers-on-parallel-pinn)
  - [Papers on PINN Accerleration](#papers-on-pinn-accerleration)
  - [Papers on Model Transfer & Meta-Learning](#papers-on-model-transfer--meta-learning)
  - [Papers on Probabilistic PINNs and Uncertainty Quantification](#papers-on-probabilistic-pinns-and-uncertainty-quantification)
  - [Papers on Applications](#papers-on-applications)
  - [Papers on PINN Analysis](#papers-on-pinn-analysis)

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
6. **PyDEns: a Python Framework for Solving Differential Equations with Neural Networks**, *Alex Koryagin, er, Roman Khudorozkov, Sergey Tsimfer*, arXiv:1909.11544 [cs, stat], 2019. [[paper]()]
7. **NeuroDiffEq: A Python package for solving differential equations with neural networks**, *Feiyu Chen, David Sondak, Pavlos Protopapas, Marios Mattheakis, Shuheng Liu, Devansh Agarwal, Marco Di Giovanni*, Journal of Open Source Software, 2020. [[paper](https://joss.theoj.org/papers/10.21105/joss.01931)][[code](https://github.com/analysiscenter/pydens)]
8. **Universal Differential Equations for Scientific Machine Learning**, *Christopher Rackauckas, Yingbo Ma, Julius Martensen, Collin Warner, Kirill Zubov, Rohit Supekar, Dominic Skinner, Ali Ramadhan, Alan Edelman*, arXiv:2001.04385 [cs, math, q-bio, stat], 2020. [[paper](https://arxiv.org/pdf/2001.04385.pdf)][[code](https://github.com/ChrisRackauckas/universal_differential_equations)]
9. **NeuralPDE: Automating Physics-Informed Neural Networks (PINNs) with Error Approximations**, *Kirill Zubov, Zoe McCarthy, Yingbo Ma, Francesco Calisto, Valerio Pagliarino, Simone Azeglio, Luca Bottero, Emmanuel Luján, Valentin Sulzer, Ashutosh Bharambe, N Vinchhi, , Kaushik Balakrishnan, Devesh Upadhyay, Chris Rackauckas*, arXiv:2107.09443 [cs], 2021. [[paper](https://arxiv.org/pdf/2107.09443)][[code](https://github.com/SciML/NeuralPDE.jl)]
10. **IDRLnet: A Physics-Informed Neural Network Library**, *Wei Peng, Jun Zhang, Weien Zhou, Xiaoyu Zhao, Wen Yao, Xiaoqian Chen*, arXiv:2107.04320 [cs, math], 2021. [[paper](https://arxiv.org/pdf/2107.04320.pdf)][[code](https://github.com/idrl-lab/idrlnet)]
11. **NeuralUQ: A comprehensive library for uncertainty quantification in neural differential equations and operators**, *Zongren Zou, Xuhui Meng, Apostolos F. Psaros, George Em Karniadakis*, **UNKNOWN_JOURNAL**, 2022. [[paper](http://arxiv.org/pdf/2208.11866.pdf)][[code](https://github.com/Crunch-UQ4MI/neuraluq)]

## Papers on PINN Models
1. **Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations**, *M. Raissi, P. Perdikaris, G. E. Karniadakis*, Journal of Computational Physics, 2019. [[paper](https://www.sciencedirect.com/science/article/pii/S0021999118307125)]
2. **The deep Ritz method: a deep learning-based numerical algorithm for solving variational problems**, *E Weinan, Bing Yu*, Communications in Mathematics and Statistics, 2018. [[paper](https://link.springer.com/article/10.1007/s40304-018-0127-z)]
3. **DGM: A deep learning algorithm for solving partial differential equations**, *Justin Sirignano, Konstantinos Spiliopoulos*, Journal of Computational Physics, 2018. [[paper](https://www.sciencedirect.com/science/article/pii/S0021999118305527)]
4. **SPINN: Sparse, Physics-based, and partially Interpretable Neural Networks for PDEs**, *Amuthan A. Ramabathiran, Ramach, Prabhu ran*, Journal of Computational Physics, 2021. [[paper](https://www.sciencedirect.com/science/article/pii/S0021999121004952)][[code](https://github.com/nn4pde/SPINN)]
5. **Deep neural network methods for solving forward and inverse problems of time fractional diffusion equations with conformable derivative**, *Yinlin Ye, Yajing Li, Hongtao Fan, Xinyi Liu, Hongbing Zhang*, arXiv:2108.07490 [cs, math], 2021. [[paper](http://arxiv.org/pdf/2108.07490.pdf)]
1. **NH-PINN: Neural homogenization based physics-informed neural network for multiscale problems**, *Wing Tat Leung, Guang Lin, Zecheng Zhang*, arXiv:2108.12942 [cs, math], 2021. [[paper](http://arxiv.org/pdf/2108.12942.pdf)]
1. **Physics-Augmented Learning: A New Paradigm Beyond Physics-Informed Learning**, *Ziming Liu, Yunyue Chen, Yuanqi Du, Max Tegmark*, arXiv:2109.13901 [physics], 2021. [[paper](http://arxiv.org/pdf/2109.13901.pdf)]
2. **Theory-guided hard constraint projection (HCP): A knowledge-based data-driven scientific machine learning method**, *Yuntian Chen, Dou Huang, Dongxiao Zhang, Junsheng Zeng, Nanzhe Wang, Haoran Zhang, Jinyue Yan*, Journal of Computational Physics, 2021. [[paper](https://linkinghub.elsevier.com/retrieve/pii/S0021999121005192)]
3. **Learning in Sinusoidal Spaces with Physics-Informed Neural Networks**, *Jian Cheng Wong, Chinchun Ooi, Abhishek Gupta, Yew-Soon Ong*, arXiv:2109.09338 [physics], 2021. [[paper](http://arxiv.org/pdf/2109.09338.pdf)]
4. **HyperPINN: Learning parameterized differential equations with physics-informed hypernetworks**, *Filipe de Avila Belbute-Peres, Yi-fan Chen, Fei Sha*, **NIPS**, 2021. [[paper](https://openreview.net/forum?id=LxUuRDUhRjM)]
1. **Physics-informed PointNet: A deep learning solver for steady-state incompressible flows and thermal fields on multiple sets of irregular geometries**, *AliKashefi, TapanMukerji*, Journal of Computational Physics, 2022. [[paper](https://doi.org/10.1016/j.jcp.2022.111510)]
2. **Physics-informed graph neural Galerkin networks: A unified framework for solving PDE-governed forward and inverse problems**, *HanGao, Matthew J.Zahr, Jian-XunWang*, Computer Methods in Applied Mechanics and Engineering, 2022. [[paper](https://doi.org/10.1016/j.cma.2021.114502)]
3. **PhyGNNet: Solving spatiotemporal PDEs with Physics-informed Graph Neural Network**, *Longxiang Jiang, Liyuan Wang, Xinkun Chu, Yonghao Xiao and Hao Zhang*, arXiv:2208.04319 [cs.NE], 2022. [[paper](https://arxiv.org/abs/2208.04319)]
4. **ModalPINN : an extension of Physics-Informed Neural Networks with enforced truncated Fourier decomposition for periodic flow reconstruction using a limited number of imperfect sensors**, * Ga´etan Raynaud , S´ebastien Houde, Fr´ed´erick P Gosselin*, Journal of Computational Physics, 2022. [[paper](https://doi.org/10.1016/j.jcp.2022.111271)]
1. **∆-PINNs: physics-informed neural networks on complex geometries**, *Francisco Sahli Costabal, Simone Pezzuto, Paris Perdikaris*, **Arxiv**, 2022. [[paper](http://arxiv.org/pdf/2209.03984.pdf)]
1. **Robust Regression with Highly Corrupted Data via Physics Informed Neural Networks**, *Wei Peng, Wen Yao, Weien Zhou, Xiaoya Zhang, Weijie Yao*, **ArXiv**, 2022. [[paper](http://arxiv.org/pdf/2210.10646.pdf)][[code](https://github.com/weipengOO98/robust_pinn)]

## Papers on Parallel PINN
1. **Parallel Physics-Informed Neural Networks via Domain Decomposition**, *Khemraj Shukla, Ameya D. Jagtap, George Em Karniadakis*, arXiv:2104.10013 [cs], 2021. [[paper](https://arxiv.org/pdf/2104.10013)]
2. **Finite Basis Physics-Informed Neural Networks (FBPINNs): a scalable domain decomposition approach for solving differential equations**, *Ben Moseley, Andrew Markham, Tarje Nissen-Meyer*, arXiv:2107.07871 [physics], 2021. [[paper](https://arxiv.org/pdf/2107.07871)]
3. **PPINN: Parareal physics-informed neural network for time-dependent PDEs**, *Xuhui Meng, Zhen Li, Dongkun Zhang, George Em Karniadakis*, Computer Methods in Applied Mechanics and Engineering, 2020. [[paper](https://arxiv.org/pdf/2104.10013)]
4. **When Do Extended Physics-Informed Neural Networks (XPINNs) Improve Generalization?**, *Zheyuan Hu, Ameya D. Jagtap, George Em Karniadakis, Kenji Kawaguchi*, arXiv:2109.09444 [cs, math, stat], 2021. [[paper](http://arxiv.org/pdf/2109.09444.pdf)]
5. **Scaling physics-informed neural networks to large domains by using domain decomposition**, *Ben Moseley, Andrew Markham, Tarje Nissen-Meyer*, *NIPS*, 2021. [[paper](https://openreview.net/forum?id=o1WiAZiw_CE)]
6. **Finite Basis Physics-Informed Neural Networks (FBPINNs): a scalable domain decomposition approach for solving differential equations**, *Ben Moseley, Andrew Markham, Tarje Nissen-Meyer*, arXiv:2107.07871 [physics], 2021. [[paper](http://arxiv.org/pdf/2107.07871.pdf)]
1. **Improved Deep Neural Networks with Domain Decomposition in Solving Partial Differential Equations**, *Wei Wu, Xinlong Feng, Hui Xu*, Journal of Scientific Computing, 2022. [[paper](https://doi.org/10.1007/s10915-022-01980-y)]
1. **INN: Interfaced neural networks as an accessible meshless approach for solving interface PDE problems**, *Sidi Wu, Benzhuo Lu*, Journal of Computational Physics, 2022. [[paper](https://www.sciencedirect.com/science/article/pii/S0021999122006507)][[code](https://github.com/bzlu-Group/INN)]

## Papers on PINN Accerleration
1. **Self-adaptive loss balanced Physics-informed neural networks for the incompressible Navier-Stokes equations**, *Zixue Xiang, Wei Peng, Xiaohu Zheng, Xiaoyu Zhao, Wen Yao*, arXiv:2104.06217 [physics], 2021. [[paper](https://arxiv.org/pdf/2104.06217)]
2. **A Dual-Dimer method for training physics-constrained neural networks with minimax architecture**, *Dehao Liu, Yan Wang*, Neural Networks, 2021. [[paper](https://www.sciencedirect.com/science/article/abs/pii/S0893608020304536)]
3. **Adversarial Multi-task Learning Enhanced Physics-informed Neural Networks for Solving Partial Differential Equations**, *Pongpisit Thanasutives, Masayuki Numao, Ken-ichi Fukui*, arXiv:2104.14320 [cs, math], 2021. [[paper](https://arxiv.org/pdf/2104.14320)]
4. **DPM: A Novel Training Method for Physics-Informed Neural Networks in Extrapolation**, *Jungeun Kim, Kookjin Lee, Dongeun Lee, Sheo Yon Jin, Noseong Park*, AAAI, 2021. [[paper](https://www.aaai.org/AAAI21Papers/AAAI-4849.KimJ.pdf)]
5. **Gradient-enhanced physics-informed neural networks for forward and inverse PDE problems**, *Jeremy Yu, Lu Lu, Xuhui Meng, George Em Karniadakis*, Arxiv, 2021.  [[paper](https://arxiv.org/abs/2111.02801)]
6. **CAN-PINN: A Fast Physics-Informed Neural Network Based on Coupled-Automatic-Numerical Differentiation Method**, *Pao-Hsiung Chiu, Jian Cheng Wong, Chinchun Ooi, My Ha Dao, Yew-Soon Ong*, Arxiv, 2021. [[paper](https://arxiv.org/abs/2110.15832)]
7. **A hybrid physics-informed neural network for nonlinear partial differential equation**, *Chunyue Lv, Lei Wang, Chenming Xie*, Arxiv, 2021. [[paper](https://arxiv.org/abs/2112.01696)]
8. **Multi-Objective Loss Balancing for Physics-Informed Deep Learning**, *Rafael Bischof, Michael Kraus*, Arxiv, 2021. [[paper](http://rgdoi.net/10.13140/RG.2.2.20057.24169)]
9. **A High-Efficient Hybrid Physics-Informed Neural Networks Based on Convolutional Neural Network**,  *Zhiwei Fang*,  IEEE Transactions on Neural Networks and Learning Systems, 2021. [[paper](https://ieeexplore.ieee.org/document/9403414)]
10. **RPINNs: Rectified-physics informed neural networks for solving stationary partial differential equations**,  *Pai Peng, Jiangong Pan, Hui Xu, Xinlong Feng*,  Computers & Fluids, 2022. [[paper](https://doi.org/10.1016/j.compfluid.2022.105583)]
11. **A comprehensive study of non-adaptive and residual-based adaptive sampling for physics-informed neural networks**,  *Chenxi Wu,Min Zhu,Qinyang Tan,Yadhu Kartha,Lu Lu*, arXiv:2207.10289 [cs], 2022. [[paper](https://arxiv.org/pdf/2207.10289.pdf)]
12. **A Novel Adaptive Causal Sampling Method for Physics-Informed Neural Networks**,  *Jia Guo, Haifeng Wang, Chenping Hou*, 	arXiv:2210.12914 [cs], 2022. [[paper](https://arxiv.org/pdf/2210.12914.pdf)]
13. **Accelerated Training of Physics-Informed Neural Networks (PINNs) using Meshless Discretizations**,  *Ramansh Sharma, Varun Shankar*, 	NeurIPS, 2022. [[paper](https://arxiv.org/abs/2205.09332)]
14. **Is L2 Physics-Informed Loss Always Suitable for Training Physics-Informed Neural Network**,  *Chuwei Wang, Shanda Li, Di He, Liwei Wang*, 	NeurIPS, 2022. [[paper](https://arxiv.org/abs/2206.02016)]


## Papers on Model Transfer & Meta-Learning
1. **A physics-aware learning architecture with input transfer networks for predictive modeling**, *Amir Behjat, Chen Zeng, Rahul Rai, Ion Matei, David Doermann, Souma Chowdhury*, Applied Soft Computing, 2020. [[paper](https://www.sciencedirect.com/science/article/abs/pii/S1568494620306037)]
2. **Transfer learning based multi-fidelity physics informed deep neural network**, *Souvik Chakraborty*, Journal of Computational Physics, 2021. [[paper](https://www.sciencedirect.com/science/article/pii/S0021999120307166)]
3. **Transfer learning enhanced physics informed neural network for phase-field modeling of fracture**, *Somdatta Goswami, Cosmin Anitescu, Souvik Chakraborty, Timon Rabczuk*, Theoretical and Applied Fracture Mechanics, 2020. [[paper](https://www.sciencedirect.com/science/article/abs/pii/S016784421930357X)]
4. **Meta-learning PINN loss functions**, *Apostolos F. Psaros, Kenji Kawaguchi, George Em Karniadakis*, arXiv:2107.05544 [cs], 2021. [[paper](https://arxiv.org/pdf/2107.05544.pdf)]
5. **Meta-PDE: Learning to Solve PDEs Quickly Without a Mesh**, *Tian Qin,Alex Beatson,Deniz Oktay,Nick McGreivy,Ryan P. Adams*, 	arXiv:2211.01604 [cs], 2022. [[paper](https://arxiv.org/pdf/2211.01604.pdf)]
5. **Physics-Informed Neural Networks (PINNs) for Parameterized PDEs: A Metalearning Approach**, *Michael Penwarden, Sh Zhe, ian, Akil Narayan, Robert M. Kirby*, Arxiv, 2021. [[paper](https://arxiv.org/abs/2110.13361)]

## Papers on Probabilistic PINNs and Uncertainty Quantification
1. **A physics-aware, probabilistic machine learning framework for coarse-graining high-dimensional systems in the Small Data regime**, *Constantin Grigo, Phaedon-Stelios Koutsourelakis*, Journal of Computational Physics, 2019. [[paper](https://www.sciencedirect.com/science/article/pii/S0021999119305261)]
2. **Adversarial uncertainty quantification in physics-informed neural networks**, *Yibo Yang, Paris Perdikaris*, Journal of Computational Physics, 2019. [[paper](https://www.sciencedirect.com/science/article/pii/S0021999119303584)]
3. **B-PINNs: Bayesian physics-informed neural networks for forward and inverse PDE problems with noisy data**, *Liu Yang, Xuhui Meng, George Em Karniadakis*, Journal of Computational Physics, 2021. [[paper](https://www.sciencedirect.com/science/article/pii/S0021999120306872)]
4. **PID-GAN: A GAN Framework based on a Physics-informed Discriminator for Uncertainty Quantification with Physics**, *Arka Daw, M. Maruf, Anuj Karpatne*, arXiv:2106.02993 [cs, stat], 2021. [[paper](https://arxiv.org/pdf/2106.02993)]
5. **Quantifying Uncertainty in Physics-Informed Variational Autoencoders for Anomaly Detection**, *Marcus J. Neuer*, ESTEP, 2020. [[paper](https://link.springer.com/chapter/10.1007/978-3-030-69367-1_3)]
6. **A Physics-Data-Driven Bayesian Method for Heat Conduction Problems**, *Xinchao Jiang, Hu Wang, Yu li*, arXiv:2109.00996 [cs, math], 2021. [[paper](http://arxiv.org/pdf/2109.00996.pdf)]
7. **Wasserstein Generative Adversarial Uncertainty Quantification in Physics-Informed Neural Networks**, *Yihang Gao, Michael K. Ng*, arXiv:2108.13054 [cs, math], 2021. [[paper](http://arxiv.org/pdf/2108.13054.pdf)]
8. **Flow Field Tomography with Uncertainty Quantification using a Bayesian Physics-Informed Neural Network**, *Joseph P. Molnar, Samuel J. Grauer*, arXiv:2108.09247 [physics], 2021. [[paper](http://arxiv.org/pdf/2108.09247.pdf)]
9. **Stochastic Physics-Informed Neural Networks (SPINN): A Moment-Matching Framework for Learning Hidden Physics within Stochastic Differential Equations**, *Jared O'Leary, Joel A. Paulson, Ali Mesbah*, arXiv:2109.01621 [cs], 2021. [[paper](http://arxiv.org/pdf/2109.01621.pdf)]
10. **Spectral PINNs: Fast Uncertainty Propagation with Physics-Informed Neural Networks**, *Björn Lütjens, Catherine H. Crawford, Mark Veillette, Dava Newman*, *NIPS*, 2021. [[paper](https://openreview.net/forum?id=218sl_mPChc)]
11. **Robust Learning of Physics Informed Neural Networks**, *Ch Bajaj, rajit, Luke McLennan, Timothy Andeen, Avik Roy*, Arxiv, 2021. [[paper](https://arxiv.org/abs/2110.13330)]
1. **Bayesian Physics Informed Neural Networks for real-world nonlinear dynamical systems**,  *Kevin Linka, Amelie Schäfer, Xuhui Meng, Zongren Zou, George EmKarniadakis, Ellen Kuhl*,  Computer Methods in Applied Mechanics and Engineering, 2022. [[paper](https://doi.org/10.1016/j.cma.2022.115346)]
2. **Multi-output physics-informed neural networks for forward and inverse PDE problems with uncertainties**,  *Mingyuan Yang, John T.Foster*,  Computer Methods in Applied Mechanics and Engineering, 2022. [[paper](https://doi.org/10.1016/j.cma.2022.115041)]

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
11. **Physics-informed Neural Network for Nonlinear Dynamics in Fiber Optics**, *Xiaotian Jiang, Danshi Wang, Qirui Fan, Min Zhang, Chao Lu, Alan Pak Tao Lau*, arXiv:2109.00526 [physics], 2021. [[paper](http://arxiv.org/pdf/2109.00526.pdf)]
12. **On Theory-training Neural Networks to Infer the Solution of Highly Coupled Differential Equations**, *M. Torabi Rad, A. Viardin, M. Apel*, arXiv:2102.04890 [physics], 2021. [[paper](http://arxiv.org/pdf/2102.04890.pdf)]
13. **Theory-training deep neural networks for an alloy solidification benchmark problem**, *M. Torabi Rad, A. Viardin, G. J. Schmitz, M. Apel*, arXiv:1912.09800 [physics], 2019. [[paper](http://arxiv.org/pdf/1912.09800.pdf)]
14. **Explicit physics-informed neural networks for nonlinear closure: The case of transport in tissues**, *Ehsan Taghizadeh, Helen M. Byrne, Brian D. Wood*, Journal of Computational Physics, 2022. [[paper](https://linkinghub.elsevier.com/retrieve/pii/S0021999121006768)]
1. **A mixed formulation for physics-informed neural networks as a potential solver for engineering problems in heterogeneous domains: comparison with finite element method**, *Shahed Rezaei, Ali Harandi, Ahmad Moeineddin, Bai-Xiang Xu, Stefanie Reese*, arXiv:2206.13103 [cs.CE], 2022. [[paper](https://arxiv.org/abs/2206.13103)]
2. **A generalized framework for unsupervised learning and data recovery in computational fluid dynamics using discretized loss functions**,  *Jot Singh Aulakh, Steven B. Beale,  and Jon G. Pharoah*,  Physics of Fluids, 2022. [[paper](https://doi.org/10.1063/5.0097480)]
3. **Physics-Informed Neural Networks for AC Optimal Power Flow**, *Rahul Nellikkath, Spyros Chatzivasileiadis*,  Electric Power Systems Research, 2022. [[paper](https://doi.org/10.1016/j.epsr.2022.108412)]
4. **Physics-informed neural networks for the shallow-water equations on the sphere**, *Alex Bihlo, Roman O.Popovych*,  Journal of Computational Physics, 2022. [[paper](https://doi.org/10.1016/j.jcp.2022.111024)]
5. **A Physics-Informed Machine Learning Approach for Estimating Lithium-Ion Battery Temperature**, *Gyouho Cho, Mengqi Wang, Youngki Kim, Jaerock Kwon, Wencong Su*, IEEE Access, 2022. [[paper](https://ieeexplore.ieee.org/document/9858911/)]
1. **Physically guided deep learning solver for time-dependent Fokker–Planck equation**, *Yang Zhang, Ka-Veng Yuen*, International Journal of Non-Linear Mechanics, 2022. [[paper](https://www.sciencedirect.com/science/article/pii/S0020746222001792)]
1. **A Physically Consistent Framework for Fatigue Life Prediction using Probabilistic Physics-Informed Neural Network**, *Taotao Zhou, Shan Jiang, Te Han, Shun-Peng Zhu, Yinan Cai*, International Journal of Fatigue, 2022. [[paper](https://www.sciencedirect.com/science/article/pii/S0142112322004844)]
1. **Inverse modeling of nonisothermal multiphase poromechanics using physics-informed neural networks**, *Danial Amini, Ehsan Haghighat, Ruben Juanes*, **Arxiv**, 2022. [[paper](http://arxiv.org/pdf/2209.03276.pdf)][[code](https://github.com/sciann/sciann-applications/tree/master/SciANN-PoroElasticity))]

## Papers on PINN Analysis
1. **Estimates on the generalization error of physics-informed neural networks for approximating a class of inverse problems for PDEs**, *Siddhartha Mishra, Roberto Molinaro*, IMA Journal of Numerical Analysis, 2021. [[paper](https://academic.oup.com/imajna/advance-article-abstract/doi/10.1093/imanum/drab032/6297946)]
2. **Error analysis for physics informed neural networks (PINNs) approximating Kolmogorov PDEs**, *Tim De Ryck, Siddhartha Mishra*, arXiv:2106.14473 [cs, math], 2021. [[paper](https://arxiv.org/pdf/2106.14473.pdf)]
3. **Error Analysis of Deep Ritz Methods for Elliptic Equations**, *Yuling Jiao, Yanming Lai, Yisu Luo, Yang Wang, Yunfei Yang*, arXiv:2107.14478 [cs, math], 2021. [[paper](https://arxiv.org/pdf/2107.14478.pdf)]
4. **Learning Partial Differential Equations in Reproducing Kernel Hilbert Spaces**, *George Stepaniants*, arXiv:2108.11580 [cs, math, stat], 2021. [[paper](http://arxiv.org/pdf/2108.11580.pdf)]
5. **Simultaneous Neural Network Approximations in Sobolev Spaces**, *Sean Hon, Haizhao Yang*, arXiv:2109.00161 [cs, math], 2021. [[paper](http://arxiv.org/pdf/2109.00161.pdf)]
6. **Characterizing possible failure modes in physics-informed neural networks**, *Aditi S. Krishnapriyan, Amir Gholami, Sh Zhe, ian, Robert M. Kirby, Michael W. Mahoney*, arXiv:2109.01050 [physics], 2021. [[paper](http://arxiv.org/pdf/2109.01050.pdf)]
7. **Understanding and Mitigating Gradient Flow Pathologies in Physics-Informed Neural Networks**, *Sifan Wang, Yujun Teng, Paris Perdikaris*, SIAM Journal on Scientific Computing, 2021. [[paper](https://epubs.siam.org/doi/10.1137/20M1318043)]
8. **Variational Physics Informed Neural Networks: the role of quadratures and test functions**, *Stefano Berrone, Claudio Canuto, Moreno Pintore*, arXiv:2109.02035 [cs, math], 2021. [[paper](http://arxiv.org/pdf/2109.02035.pdf)]
9. **Convergence Analysis for the PINNs**, *Yuling Jiao, Yanming Lai, Dingwei Li, Xiliang Lu, Yang Wang, Jerry Zhijian Yang*, arXiv:2109.01780 [cs, math], 2021. [[paper](http://arxiv.org/pdf/2109.01780.pdf)]
10. **Characterizing possible failure modes in physics-informed neural networks**, *Aditi Krishnapriyan, Amir Gholami, Sh Zhe, ian, Robert Kirby, Michael W. Mahoney*, *NIPS*, 2021. [[paper](https://openreview.net/forum?id=a2Gr9gNFD-J)]
11. **Convergence rate of DeepONets for learning operators arising from advection-diffusion equations**, *Beichuan Deng, Yeonjong Shin, Lu Lu, Zhongqiang Zhang, George Em Karniadakis*, arXiv:2102.10621 [math], 2021. [[paper](https://arxiv.org/abs/2102.10621)]
12. **Estimates on the generalization error of physics-informed neural networks for approximating PDEs**, *Siddhartha Mishra, Roberto Molinaro*, IMA Journal of Numerical Analysis, 2022. [[paper](https://academic.oup.com/imajna/advance-article/doi/10.1093/imanum/drab093/6503953)]
1. **Investigating and Mitigating Failure Modes in Physics-informed Neural Networks (PINNs)**, *Shamsulhaq Basir*, **arXiv:2209.09988v1[cs]**, **2022**. [[paper](https://arxiv.org/pdf/2209.09988.pdf)][[code](https://github.com/shamsbasir/investigating_mitigating_failure_modes_in_pinns)]
