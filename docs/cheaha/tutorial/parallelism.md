# Tutorial on Usage of Parallelization-based Software in Cheaha

## Sequential Execution

Breaking a bigger problem into set of tasks, and executing these tasks one by one on a single CPU.

<!-- markdownlint-disable MD045 -->
![](images/parallelism_serial_execution.drawio)
<!-- markdownlint-enable MD045 -->

## Parallel Execution

Divide a larger problem into a series of smaller tasks and execute these tasks using multiple CPUs. The application should leverage parallelization technology to utilize multicore processors, multiple nodes, multiple GPUs, or a hybrid approach (such as combining CPUs and GPUs).

<!-- markdownlint-disable MD045 -->
![](images/parallelism_parallel_execution.drawio)
<!-- markdownlint-enable MD045 -->

## Types of Parallelization

### Shared Memory Parallelization

In this method, your job executes independent tasks on separate cores within the same compute node. These tasks share the node's resources and communicate by reading from and writing to shared memory.

For instance, OpenMP is a parallel directive that supports shared memory parallelization.

### Distributed Memory Parallelization

Tasks can be distributed on different compute nodes and executed. The tasks communicate each other using message passing. A widely used standard to achieve this kind of parallelism is Message Passing Interface (MPI).

### GPU Parallelization

It divides large computational tasks into smaller subtasks that can be executed concurrently on different GPU cores. This results in significant acceleration compared to traditional CPU-based computations. CUDA (Compute Unified Device Architecture) is a widely used parallel computing platform and programming model developed by NVIDIA, enabling users to utlize the power of GPUs effectively.

### Hybrid Parallelization

It is a computing approach that integrates various parallelization techniques or models to effectively utilize a heterogeneous environment, such as diverse components like CPUs and GPUs. For instance, it combines shared-memory (openMP) and distributed-memory parallelization (MPI) to optimize application execution.

## A Sampling of Parallel Software

### Gromacs

Gromacs is specifically meant for high-performance molecular dynamics and analysis.

```bash
srun --nodes=1 --ntasks-per-node=24 --mem=120GB --time=10:00:00 --partition=intel-dcb --pty /bin/bash
```

Recent Gromacs version available in Cheaha can be loaded as,

```bash
$module load GROMACS/2019-fosscuda-2018b
```

#### Study of Water System - An Example

Some of the simulation examples are covered in the [Gromacs Tutorial Page](http://www.mdtutorials.com/gmx/).We will take the example of water system as a case study. Let us consider the [Gromacs Molecular Example](http://ftp.gromacs.org/pub/benchmarks/water_GMX50_bare.tar.gz). The simulation is meant for study of water system, for instance understanding water properties, molecular dynamics, etc.

Download and extract the example `pdb` dataset using the following commands,

```bash
$DATA_SET=water_GMX50_bare
$wget -c https://ftp.gromacs.org/pub/benchmarks/${DATA_SET}.tar.gz
$tar xf ${DATA_SET}.tar.gz
```

##### Input Parameters

Let us consider the subset of data `1536` from the repo, `water-cut1.0_GMX50_bare`.

```bash
$cd water-cut1.0_GMX50_bare/1536
$ls
conf.gro  pme.mdp  rf.mdp  topol.top
```

- The `.mdp` file is a molecular dynamics parameter (MDP) input file.
- The `.gro` is a coordinate file that contains spatial coordinates of atoms in a system for visualization and structure analysis. It includes box dimensions and number of atoms.
- The `.top` is a topology file that contains the molecular system's structure, including the types of atoms, bonds, angles, force field parameters, etc.

<!-- markdownlint-enable MD046 -->
!!! note
    The `rf.mdp` input file is excluded, as only the PME method is focused for this case study.
<!-- markdownlint-enable MD046 -->

##### Preprocessing

The initial step is to preprocess the input file, `pme.mdp` using the below command,

```bash
gmx grompp -f pme.mdp
```

The above command prepare the input file for the simulation, it reads parameters and combines them into a single output file named `topol.tpr`.

- gmx: gromacs execuable
- grompp: This stands for "GROMACS PreProcessor." It combines the simulation parameters specified in the .mdp file with other input files (like the topology file and the coordinate file) to generate a binary input file (.tpr) that will be used for the actual simulation.
- .tpr - Portable binary run input file.

The ouptut file `topol.tpr` rcontains the settings and parameters for the simulation, such as time step (nsteps), number of atoms (natoms), temperature (ref), and coulombtype, and this example adopts Particle-Mesh Ewald (PME) coulombtype. As this file is in binary format it cannot be read with a normal editor. You can read a portable binary run input file using the below command.

```bash
gmx dump -s topol.tpr > topol.out
```

##### Execution and Scalability

This simulation execution gives detailed information about the settings of the molecular dynamics simulation for a water model,

##### Water System Inputs

- Total Atoms (natoms): 1,536,000
- Number of Steps: 5,000
- Distribution: Domain Decomposition
- MPI Ranks: 6
- Average Atoms per Domain: 256,000
- Domain Decomposition Grid: 6 x 1 x 1

```bash
$export OMP_NUM_THREADS=6
$gmx mdrun -ntmpi 6 -nsteps 5000 -ntomp 4 -s topol.tpr -deffnm md_output.log
```

In the above run command,

- `gmx` is the executable to run the pipeline.
- `-ntmpi 4` Number of MPI processes.
- `-nsteps 5000` Number of steps to run the simulation.
- `-ntomp 6` Number of cores, which will be 10*4 MPI processes i.e, 40 cores
- `-s topol.tpr` is the input parameter.

##### Performance Analysis

{{ read_csv('../software/res/parallelism_gromacs_cpu.csv', keep_default_na=False) }}

The majority of the computational time and resources were spent on force calculations and PME mesh operations, indicating these are the most computationally intensive tasks in this simulation. The system achieved good load balancing, reflected in the distribution of tasks across the available ranks and threads.

{{ read_csv('../software/res/parallelism_gromacs_gpu.csv', keep_default_na=False) }}

{{ read_csv('../software/res/parallelism_gromacs_gpu_hybrid.csv', keep_default_na=False) }}

<!---
### Computational Metrics

Domain decomposition is based on the number of MPI ranks, which in this case is 6. The total number of atoms is divided into 6 distinct domains for parallel processing, enabling the simulation to run more efficiently across multiple processors. On average, each domain contains 256,000 atoms. The Domain Decomposition Grid of 6 x 1 x 1 indicates how the simulation space is divided into separate domains along the X x Y x Z axis for parallel processing

#### Output

The outputs are a .log, .edr, .cpt and .gro files.
The .edr  Energy data for analysis of system dynamics.
file contains spatial coordinates of atoms in a system for visualization and structure analysis.
The .cpt file is for checkpointing data for resuming simulations.

PME advantages in faster parallelism, decrease in grid dimension.

!!!!
Force Calculation:

Since you're using only 1 MPI process and 1 OpenMP thread, all calculations (force evaluations, energy calculations, etc.) will be executed serially on a single core.
For each time step (up to 5,000 steps), GROMACS calculates the forces acting on each of the 1,536,000 atoms based on their positions and interactions (using the defined potential energy functions).
Integration:

After calculating the forces, GROMACS will update the positions and velocities of the atoms using integration methods (like the leapfrog algorithm or velocity Verlet).

### GPU

```bash
$module load rc/GROMACS/2022.3-gpu
```

```bash
$gmx mdrun -nb gpu -s topol.tpr
```

```bash
- `-nb gpu`defines the computation to use GPUs.
```

### Quantum Espresso

Quantum Espresso (QE) is an open-source suite of codes for electronic-structure calculations and materials modeling based on density functional theory (DFT), plane waves, and pseudopotentials. It is used to study the properties of materials at the atomic scale.

Quantum Expresso is available as a module in Cheaha and can be loaded as,

```bash
$module load QuantumESPRESSO/6.3-foss-2018b
```
-->
